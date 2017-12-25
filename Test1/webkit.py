'''
Created on 2017年12月14日

@author: QiLing
'''
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWebKitWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

class App(QtWebKitWidgets.QWebView):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 1000
        self.path_now = os.getcwd()
        self.url = os.path.join(self.path_now, "trainview.html", )
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

      
        
        self.web = QWebView()
        self.web.load(QUrl("file:///"+self.url))
        #self.web.load(QUrl("https://pythonspot.com"))
       
        vbbox = QVBoxLayout()
        vbbox.addWidget(self.web)
        main = QHBoxLayout()
        main.addLayout(vbbox)
        main.setStretch(0,1)
        main.setStretch(1,8)
        
        self.setLayout(main)
        
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())




 

