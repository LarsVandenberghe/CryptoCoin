# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\X-Tra Lars\Desktop\Programming\Python\Projects\CryptoCoin Widget\CryptoCoin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(198, 170)
        MainWindow.setStyleSheet(_fromUtf8("background:transparent;"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("background-color: rgba(0, 0, 0, 127);\n"
"border-radius: 5px;\n"
"border: 1px solid grey;"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1, 1, 196, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet(_fromUtf8("border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"background-color: rgba(0, 0, 0, 100);\n"
"color: rgb(214, 214, 214);\n"
"border: 0px;"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.slt1_logo = QtGui.QLabel(self.centralwidget)
        self.slt1_logo.setGeometry(QtCore.QRect(10, 40, 30, 30))
        self.slt1_logo.setStyleSheet(_fromUtf8("border: 0px;\n"
"background-color: transparent;"))
        self.slt1_logo.setText(_fromUtf8(""))
        self.slt1_logo.setScaledContents(True)
        self.slt1_logo.setObjectName(_fromUtf8("slt1_logo"))
        self.slt2_logo = QtGui.QLabel(self.centralwidget)
        self.slt2_logo.setGeometry(QtCore.QRect(10, 100, 30, 30))
        self.slt2_logo.setStyleSheet(_fromUtf8("border: 0px;\n"
"background-color: transparent;"))
        self.slt2_logo.setText(_fromUtf8(""))
        self.slt2_logo.setScaledContents(True)
        self.slt2_logo.setObjectName(_fromUtf8("slt2_logo"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 39, 1, 100))
        self.line.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 89, 178, 1))
        self.line_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.slt1_updated = QtGui.QLabel(self.centralwidget)
        self.slt1_updated.setGeometry(QtCore.QRect(55, 73, 135, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.slt1_updated.setFont(font)
        self.slt1_updated.setStyleSheet(_fromUtf8("border: 0px;\n"
"background-color: transparent;\n"
"color: rgb(150, 150, 150);"))
        self.slt1_updated.setAlignment(QtCore.Qt.AlignCenter)
        self.slt1_updated.setObjectName(_fromUtf8("slt1_updated"))
        self.slt2_updated = QtGui.QLabel(self.centralwidget)
        self.slt2_updated.setGeometry(QtCore.QRect(55, 133, 135, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.slt2_updated.setFont(font)
        self.slt2_updated.setStyleSheet(_fromUtf8("border: 0px;\n"
"background-color: transparent;\n"
"color: rgb(150, 150, 150);"))
        self.slt2_updated.setAlignment(QtCore.Qt.AlignCenter)
        self.slt2_updated.setObjectName(_fromUtf8("slt2_updated"))
        self.total_value = QtGui.QLabel(self.centralwidget)
        self.total_value.setGeometry(QtCore.QRect(1, 150, 196, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.total_value.setFont(font)
        self.total_value.setStyleSheet(_fromUtf8("color: rgba(235,170,0,255);\n"
"background-color: rgba(0, 0, 0, 100);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border: 0;"))
        self.total_value.setText(_fromUtf8(""))
        self.total_value.setAlignment(QtCore.Qt.AlignCenter)
        self.total_value.setObjectName(_fromUtf8("total_value"))
        self.slt2_name = QtGui.QLabel(self.centralwidget)
        self.slt2_name.setGeometry(QtCore.QRect(0, 132, 51, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setBold(True)
        font.setWeight(75)
        self.slt2_name.setFont(font)
        self.slt2_name.setAutoFillBackground(False)
        self.slt2_name.setStyleSheet(_fromUtf8("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"border: 0px;"))
        self.slt2_name.setText(_fromUtf8(""))
        self.slt2_name.setAlignment(QtCore.Qt.AlignCenter)
        self.slt2_name.setObjectName(_fromUtf8("slt2_name"))
        self.slt1_name = QtGui.QLabel(self.centralwidget)
        self.slt1_name.setGeometry(QtCore.QRect(0, 72, 51, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setBold(True)
        font.setWeight(75)
        self.slt1_name.setFont(font)
        self.slt1_name.setAutoFillBackground(False)
        self.slt1_name.setStyleSheet(_fromUtf8("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"border: 0px;"))
        self.slt1_name.setText(_fromUtf8(""))
        self.slt1_name.setAlignment(QtCore.Qt.AlignCenter)
        self.slt1_name.setObjectName(_fromUtf8("slt1_name"))
        self.slt1_value = QtGui.QLabel(self.centralwidget)
        self.slt1_value.setGeometry(QtCore.QRect(55, 40, 136, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.slt1_value.setFont(font)
        self.slt1_value.setStyleSheet(_fromUtf8("border: 0px;\n"
"background-color: transparent;\n"
"color: rgb(214, 214, 214);"))
        self.slt1_value.setText(_fromUtf8(""))
        self.slt1_value.setAlignment(QtCore.Qt.AlignCenter)
        self.slt1_value.setObjectName(_fromUtf8("slt1_value"))
        self.slt2_value = QtGui.QLabel(self.centralwidget)
        self.slt2_value.setGeometry(QtCore.QRect(55, 100, 136, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.slt2_value.setFont(font)
        self.slt2_value.setStyleSheet(_fromUtf8("border: 0px;\n"
"background-color: transparent;\n"
"color: rgb(214, 214, 214);"))
        self.slt2_value.setText(_fromUtf8(""))
        self.slt2_value.setAlignment(QtCore.Qt.AlignCenter)
        self.slt2_value.setObjectName(_fromUtf8("slt2_value"))
        self.widget_close = QtGui.QWidget(self.centralwidget)
        self.widget_close.setEnabled(True)
        self.widget_close.setGeometry(QtCore.QRect(0, 0, 198, 170))
        self.widget_close.setStyleSheet(_fromUtf8("background-color: rgba(0, 0, 0, 240);"))
        self.widget_close.setObjectName(_fromUtf8("widget_close"))
        self.btn_close = QtGui.QPushButton(self.widget_close)
        self.btn_close.setEnabled(True)
        self.btn_close.setGeometry(QtCore.QRect(174, 5, 20, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setBold(True)
        font.setWeight(75)
        self.btn_close.setFont(font)
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setMouseTracking(True)
        self.btn_close.setStyleSheet(_fromUtf8("background-color: rgb(190, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 0px;"))
        self.btn_close.setObjectName(_fromUtf8("btn_close"))
        self.comboBox = QtGui.QComboBox(self.widget_close)
        self.comboBox.setGeometry(QtCore.QRect(125, 30, 69, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255, 200);\n"
"border-radius: 0px;\n"
""))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_6 = QtGui.QLabel(self.widget_close)
        self.label_6.setGeometry(QtCore.QRect(5, 30, 131, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("background-color: transparent;\n"
"color: white;\n"
"border-radius: 0px;\n"
"border: 0px;"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.widget_close)
        self.label_7.setGeometry(QtCore.QRect(5, 55, 131, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("background-color: transparent;\n"
"color: white;\n"
"border-radius: 0px;\n"
"border: 0px;"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.slt1_cb = QtGui.QComboBox(self.widget_close)
        self.slt1_cb.setGeometry(QtCore.QRect(110, 75, 80, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setBold(True)
        font.setWeight(75)
        self.slt1_cb.setFont(font)
        self.slt1_cb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.slt1_cb.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255, 200);\n"
"border-radius: 0px;\n"
""))
        self.slt1_cb.setObjectName(_fromUtf8("slt1_cb"))
        self.slt1_bal = QtGui.QLineEdit(self.widget_close)
        self.slt1_bal.setGeometry(QtCore.QRect(10, 75, 91, 20))
        self.slt1_bal.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255, 200);\n"
"border-radius: 0px;\n"
""))
        self.slt1_bal.setObjectName(_fromUtf8("slt1_bal"))
        self.label_8 = QtGui.QLabel(self.widget_close)
        self.label_8.setGeometry(QtCore.QRect(5, 100, 131, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("background-color: transparent;\n"
"color: white;\n"
"border-radius: 0px;\n"
"border: 0px;"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.slt2_cb = QtGui.QComboBox(self.widget_close)
        self.slt2_cb.setGeometry(QtCore.QRect(110, 120, 80, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setBold(True)
        font.setWeight(75)
        self.slt2_cb.setFont(font)
        self.slt2_cb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.slt2_cb.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255, 200);\n"
"border-radius: 0px;\n"
""))
        self.slt2_cb.setObjectName(_fromUtf8("slt2_cb"))
        self.slt2_bal = QtGui.QLineEdit(self.widget_close)
        self.slt2_bal.setGeometry(QtCore.QRect(10, 120, 91, 20))
        self.slt2_bal.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255, 200);\n"
"border-radius: 0px;\n"
""))
        self.slt2_bal.setObjectName(_fromUtf8("slt2_bal"))
        self.btn_save = QtGui.QPushButton(self.widget_close)
        self.btn_save.setGeometry(QtCore.QRect(57, 146, 75, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255, 200);"))
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "CRYPTO CURRENCY", None))
        self.slt1_updated.setText(_translate("MainWindow", "loading...", None))
        self.slt2_updated.setText(_translate("MainWindow", "loading...", None))
        self.btn_close.setText(_translate("MainWindow", "X", None))
        self.label_6.setText(_translate("MainWindow", "Your local currency: ", None))
        self.label_7.setText(_translate("MainWindow", "Crypto balance slot 1:", None))
        self.label_8.setText(_translate("MainWindow", "Crypto balance slot 2:", None))
        self.btn_save.setText(_translate("MainWindow", "Save", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

