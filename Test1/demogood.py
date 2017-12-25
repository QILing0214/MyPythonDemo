import os
import time,threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWebKitWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
'''
    【简介】
    QtWebKit只能在pyqt5.6-里用
    QWebView中网页加载html+js
    pyqt调用js里的方法
    
    
  
'''
getJsValue =""" 
w = document.getElementById('p');
myWindow.showMessage(w.innerHTML);
"""  

class myWindow(QtWebKitWidgets.QWebView):  
    def __init__(self, parent=None):
        super(myWindow, self).__init__(parent)

        self.page().mainFrame().addToJavaScriptWindowObject("myWindow", self)
        self.loadFinished.connect(self.on_loadFinished)
        
        self.path_now = os.getcwd()
        self.url = os.path.join(self.path_now, "trainview.html", )
        self.load(QtCore.QUrl("file:///"+self.url))


    @QtCore.pyqtSlot(str)  
    def showMessage(self, message):
        print ("Message from website:",message)

    @QtCore.pyqtSlot()
    def on_loadFinished(self):
        self.page().mainFrame().evaluateJavaScript(getJsValue) 

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('myWindow')

    main = myWindow()
    def f():
        #while (1):
            main.page().mainFrame().evaluateJavaScript(getJsValue)
            time.sleep(5)
    main.show()
    #time.sleep(5)
    #thread = threading.Thread(target=f)
    #thread.start()
    sys.exit(app.exec_())