#MAIN CLASS
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import GUI_CryptoCoin
import urllib.request, json, datetime
import os  

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
        self.volume_24h_eu = float(json_results["24h_volume_eur"])
        self.percent_change_1h = float(json_results["percent_change_1h"])
        self.percent_change_24h = float(json_results["percent_change_24h"])
        self.percent_change_7d = float(json_results["percent_change_7d"])
        self.price_eur = float(json_results["price_eur"])        
        
class CryptoCoin(QMainWindow, GUI_CryptoCoin.Ui_MainWindow):
    def __init__(self, parent=None):
        super(CryptoCoin, self).__init__(parent)
        file = open(os.path.realpath(__file__).replace("CryptoCoin.py", "location.loc"), "r")
        f = file.read()
        file.close()
        self.showWindow = False
        self.move(QPoint(int(f.split(";")[0]), int(f.split(";")[1])))
        self.setupUi(self)
        
        self.widget_close.hide()    
        
        self.iota_wallet = 24.4 #MIOTA
        self.ltc_wallet = 0.05418583
        
        self.Updater()
        
        self.timer = QTimer(self)
        self.timer.setInterval(60000)
        self.timer.timeout.connect(self.Updater)
        self.timer.start()
        
        
        self.connect(self.btn_close, SIGNAL("clicked()"), self.exitApp)
     
    def Updater(self):
        try:
            try:
                self.IOTA.update()
                self.LTC.update()
            except:
                self.IOTA = coin_realtime("https://api.coinmarketcap.com/v1/ticker/iota/?convert=EUR")
                self.LTC = coin_realtime("https://api.coinmarketcap.com/v1/ticker/litecoin/?convert=EUR")
            self.ltc_updated.setText(str(self.LTC.last_updated))
            self.iota_updated.setText(str(self.IOTA.last_updated))
            self.Calculate_IOTA_Value()
            self.Calculate_LTC_Value()
            self.Calculate_Total()
            
        except:
            print("No connection.")

    def Calculate_Total(self):
        total = self.IOTA.price_eur*self.iota_wallet + self.LTC.price_eur*self.ltc_wallet
        self.total_eur.setText("€ {:.2f} / 103.60".format(int(total*100)/100))

    def Calculate_IOTA_Value(self):
        val = "€ {:.2f} (".format(int(self.IOTA.price_eur*100)/100)
        if self.IOTA.percent_change_24h < 0:
            val += "<font color='#FF0000'>" + "{:.2f}% ↓".format(self.IOTA.percent_change_24h) + "</font>)"

            self.iota_value.setText(val)
        else:
            val += " <font color='#50D050'>" + "{:.2f}% ↑".format(self.IOTA.percent_change_24h) + "</font>)"

            self.iota_value.setText(val)
            
    def Calculate_LTC_Value(self):
        val = "€ {:.2f} (".format(int(self.LTC.price_eur*100)/100)
        if self.LTC.percent_change_24h < 0:
            val += "<font color='#FF0000'>" + "{:.2f}% ↓".format(self.LTC.percent_change_24h) + "</font>)"
            self.ltc_value.setText(val)
        else:
            val += " <font color='#50D050'>" + "{:.2f}% ↑".format(self.LTC.percent_change_24h) + "</font>)"
            self.ltc_value.setText(val)  

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
        file = open(os.path.realpath(__file__).replace("CryptoCoin.py", "location.loc"), "w")
        file.write(str(self.pos().x()) + ";" + str(self.pos().y()))
        file.close()
        super(CryptoCoin, self).mouseReleaseEvent(event)
        
    def exitApp(self):
        sys.exit()
        
###############################################################################
app = QApplication(sys.argv)
dialog = CryptoCoin()
dialog.setWindowFlags(Qt.WindowStaysOnBottomHint | Qt.FramelessWindowHint | Qt.Tool) #Tool makes sure there is no icon in the task bar
dialog.setAttribute(Qt.WA_TranslucentBackground)
dialog.show()
app.exec_()
###############################################################################
