import os
import time
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWebKitWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from sqlalchemy.sql.expression import except_

getJsValue = """ 
w = document.getElementById('p');
myWindow.showMessage(w.innerHTML);
"""  

class myWindow(QtWebKitWidgets.QWebView):  
    def __init__(self, parent=None):
        super(myWindow, self).__init__(parent)
        self.jsValue=0

        self.page().mainFrame().addToJavaScriptWindowObject("myWindow", self)

        self.loadFinished.connect(self.on_loadFinished)
        
        self.path_now = os.getcwd()
        self.url = os.path.join(self.path_now, "trainview.html", )
        self.load(QtCore.QUrl("file:///"+self.url))

    @QtCore.pyqtSlot(str)  
    def showMessage(self, message):
    
        self.jsValue=message
        print ("Message from website:", message)
           
    @QtCore.pyqtSlot()
    def on_loadFinished(self):
        
        self.thread = threading.Thread(target=self.evaluateJS())
        self.thread.start()
    
    

    
    def evaluateJS(self):
              
        while self.jsValue !='Door Open':
            self.page().mainFrame().evaluateJavaScript(getJsValue) 
            time.sleep(15)
        
                 
    def getjsValue(self):
        return self.jsValue

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('myWindow')

    main = myWindow()

    main.show()

    sys.exit(app.exec_())
    