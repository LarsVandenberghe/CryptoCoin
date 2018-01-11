#MAIN CLASS
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import GUI_CryptoCoin
import urllib.request, json, datetime
import os  

coin_dict = {"BTC":"bitcoin", "ETH": "ethereum", "LTC": "litecoin", "MIOTA": "iota", "XRP": "ripple"}
#local_coin_dict = {"EUR":"€", "GBP": "£", "USD": "$"}

def shortnotation(value):
    if value > 1000000:
        return "{:.2f}m".format(int(value/10000)/100)
    elif value > 1000:
        return "{:.2f}k".format(int(value/10)/100)
    else:
        return "{:.2f}".format(value)
        
#Download Data to json
class coin_realtime(object):
    def __init__(self, api_url):
        self.api_url = api_url
        self.update()

    def update(self):
        url = urllib.request.Request(self.api_url)
        search_response = urllib.request.urlopen(url).read()
        search_results = search_response.decode("utf8")
        json_results = json.loads(search_results)[0]
        
        self.id = json_results["id"]
        self.name = json_results["name"]
        self.symbol = json_results["symbol"]
        self.rank = int(json_results["rank"])
        self.last_updated = datetime.datetime.fromtimestamp(int(json_results["last_updated"]))
        #self.volume_24h_eu = float(json_results["24h_volume_eur"])
        self.percent_change_1h = float(json_results["percent_change_1h"])
        self.percent_change_24h = float(json_results["percent_change_24h"])
        self.percent_change_7d = float(json_results["percent_change_7d"])
        try:
            self.EUR = float(json_results["price_eur"])
        except:
            pass
        try:
            self.GBP = float(json_results["price_gbp"])
        except:
            pass
        try:
            self.USD = float(json_results["price_usd"])
        except:
            pass

        
class CryptoCoin(QMainWindow, GUI_CryptoCoin.Ui_MainWindow):
    def __init__(self, parent=None):
        super(CryptoCoin, self).__init__(parent)
        
        #Read JsonSettings
        file = open(os.path.realpath(__file__).replace("CryptoCoin.py", "saved.json"), "r")
        self.settings = json.load(file)
        file.close()
        
        
        self.showWindow = False
        self.move(QPoint(self.settings["x"], self.settings["y"]))
        self.setupUi(self)
        
        #Adjust settings
        self.widget_close.hide()
        
        local_currencies = ["USD", "EUR", "GBP"]
        crypto_currencies = ["BTC", "LTC", "MIOTA", "ETH", "XRP"]
        
        for i in local_currencies:
            self.comboBox.addItem(i)
        for i in crypto_currencies:
            self.slt1_cb.addItem(i)
            self.slt2_cb.addItem(i)
            
        self.slt1_bal.setValidator(QDoubleValidator())
        self.slt2_bal.setValidator(QDoubleValidator())
        
        self.slt1_bal.setText(str(self.settings["slt1_value"]))
        temp = self.slt1_cb.findText(self.settings["slt1_coin"], Qt.MatchFixedString)
        if temp != -1:
           self.slt1_cb.setCurrentIndex(temp)
 
        self.slt2_bal.setText(str(self.settings["slt2_value"]))
        temp = self.slt2_cb.findText(self.settings["slt2_coin"], Qt.MatchFixedString)
        if temp != -1:
           self.slt2_cb.setCurrentIndex(temp)
        
        temp = self.comboBox.findText(self.settings["local_currency"], Qt.MatchFixedString)
        if temp != -1:
            self.comboBox.setCurrentIndex(temp)
        
        self.Updater()
        
        self.timer = QTimer(self)
        self.timer.setInterval(60000)
        self.timer.timeout.connect(self.Updater)
        self.timer.start()
        
        
        self.connect(self.btn_close, SIGNAL("clicked()"), self.exitApp)
        self.connect(self.btn_save, SIGNAL("clicked()"), self.saveData)
     
    def Updater(self):
        try:
            try:
                self.SLOT1.update()
                self.SLOT2.update()
            except:
                self.reloadSlots()
            self.slt1_updated.setText(str(self.SLOT1.last_updated))
            self.slt2_updated.setText(str(self.SLOT2.last_updated))
            self.Calculate_SLOT1_Value()
            self.Calculate_SLOT2_Value()
            self.Calculate_Total()
            
        except:
            print("No connection.")
            
    def reloadSlots(self):
        #Set images
        coin_slot1 = self.slt1_cb.currentText()
        coin_slot2 = self.slt2_cb.currentText()
        self.slt1_name.setText(coin_slot1)
        self.slt2_name.setText(coin_slot2)
        self.slt1_logo.setPixmap(QPixmap("logos/" + coin_slot1 + ".png"))
        self.slt2_logo.setPixmap(QPixmap("logos/" + coin_slot2 + ".png"))
        if self.comboBox.currentText() == "USD":
            self.SLOT1 = coin_realtime("https://api.coinmarketcap.com/v1/ticker/" + coin_dict[self.slt1_cb.currentText()])
            self.SLOT2 = coin_realtime("https://api.coinmarketcap.com/v1/ticker/" + coin_dict[self.slt2_cb.currentText()])
        else:
            self.SLOT1 = coin_realtime("https://api.coinmarketcap.com/v1/ticker/" + coin_dict[self.slt1_cb.currentText()] + "/?convert=" + self.comboBox.currentText())
            self.SLOT2 = coin_realtime("https://api.coinmarketcap.com/v1/ticker/" + coin_dict[self.slt2_cb.currentText()] + "/?convert=" + self.comboBox.currentText())

    def Calculate_Total(self):        
        if self.comboBox.currentText() == "USD":
            total = self.SLOT1.USD*float(self.slt1_bal.text()) + self.SLOT2.USD*float(self.slt2_bal.text())
            self.total_value.setText("$ {:.2f}".format(int(total*100)/100))
        elif self.comboBox.currentText() == "EUR":
            total = self.SLOT1.EUR*float(self.slt1_bal.text()) + self.SLOT2.EUR*float(self.slt2_bal.text())
            self.total_value.setText("€ {:.2f}".format(int(total*100)/100))
#            self.total_value.setText("Test")
        elif self.comboBox.currentText() == "GBP":
            total = self.SLOT1.GBP*float(self.slt1_bal.text()) + self.SLOT2.GBP*float(self.slt2_bal.text())
            self.total_value.setText("£ {:.2f}".format(int(total*100)/100))
            
    def Calculate_SLOT1_Value(self):
        if self.comboBox.currentText() == "USD":
            val = "$ {:s} (".format(shortnotation(self.SLOT1.USD))
        elif self.comboBox.currentText() == "EUR":
            val = "€ {:s} (".format(shortnotation(self.SLOT1.EUR))
        elif self.comboBox.currentText() == "GBP":
            val = "£ {:s} (".format(shortnotation(self.SLOT1.GBP))
            
        if self.SLOT1.percent_change_24h < 0:
            val += "<font color='#FF0000'>" + "{:.2f}% ↓".format(self.SLOT1.percent_change_24h) + "</font>)"
            
        else:
            val += "<font color='#50D050'>" + "{:.2f}% ↑".format(self.SLOT1.percent_change_24h) + "</font>)"

        self.slt1_value.setText(val)
        
    def Calculate_SLOT2_Value(self):
        if self.comboBox.currentText() == "USD":
            val = "$ {:s} (".format(shortnotation(self.SLOT2.USD))
        elif self.comboBox.currentText() == "EUR":
            val = "€ {:s} (".format(shortnotation(self.SLOT2.EUR))
        elif self.comboBox.currentText() == "GBP":
            val = "£ {:s} (".format(shortnotation(self.SLOT2.GBP))
            
        if self.SLOT2.percent_change_24h < 0:
            val += "<font color='#FF0000'>" + "{:.2f}% ↓".format(self.SLOT2.percent_change_24h) + "</font>)"
            
        else:
            val += "<font color='#50D050'>" + "{:.2f}% ↑".format(self.SLOT2.percent_change_24h) + "</font>)"

        self.slt2_value.setText(val)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.windowPos = self.pos()
            self.mousePos = event.globalPos()
            super(CryptoCoin, self).mousePressEvent(event)
        elif event.button() == Qt.RightButton:
            if self.showWindow == False:
                self.showWindow = True
                print(self.showWindow)
                self.widget_close.show()  
            else:
                self.showWindow = False
                print(self.showWindow)
                self.widget_close.hide()  
                
    def mouseMoveEvent(self, event):
        self.move(self.windowPos + event.globalPos() - self.mousePos)
        super(CryptoCoin, self).mouseMoveEvent(event)
    
    def mouseReleaseEvent(self, event):
        self.settings["x"]= self.pos().x()
        self.settings["y"]= self.pos().y()
        file = open(os.path.realpath(__file__).replace("CryptoCoin.py", "saved.json"), "w")
        file.write(json.dumps(self.settings, sort_keys=True, indent=4, separators=(',', ': ')))
        file.close()
        super(CryptoCoin, self).mouseReleaseEvent(event)
    
    def saveData(self):
        self.settings["local_currency"] = self.comboBox.currentText()
        self.settings["slt1_coin"] = self.slt1_cb.currentText()
        self.settings["slt1_value"] = float(self.slt1_bal.text())
        self.settings["slt2_coin"] = self.slt2_cb.currentText()
        self.settings["slt2_value"] = float(self.slt2_bal.text())
        self.showWindow = False
        self.widget_close.hide()
        file = open(os.path.realpath(__file__).replace("CryptoCoin.py", "saved.json"), "w")
        file.write(json.dumps(self.settings, sort_keys=True, indent=4, separators=(',', ': ')))
        file.close()
        self.reloadSlots()
        self.slt1_updated.setText(str(self.SLOT1.last_updated))
        self.slt2_updated.setText(str(self.SLOT2.last_updated))
        self.Calculate_SLOT1_Value()
        self.Calculate_SLOT2_Value()
        self.Calculate_Total()
        
    def exitApp(self):
        sys.exit()
        
###############################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = CryptoCoin()
    dialog.setWindowFlags(Qt.WindowStaysOnBottomHint | Qt.FramelessWindowHint | Qt.Tool) #Tool makes sure there is no icon in the task bar
    dialog.setAttribute(Qt.WA_TranslucentBackground)
    dialog.show()
    app.exec_()
###############################################################################
