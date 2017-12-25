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
getJsValue =""" 
w = document.getElementById('p');
myWindow.showMessage(w.innerHTML);

y=myWindow.doorstatus2;
myWindow.showMessage(y);

z=myWindow.getdoorstatus();
myWindow.showMessage(z);

if(myWindow.getdoorstatus()==0){myWindow.showMessage("Door Open");}
if(myWindow.getdoorstatus()==1){myWindow.showMessage("Door Close");}

"""  

class myWindow(QtWebKitWidgets.QWebView):
    doorstatus2="1"
      
    def __init__(self, parent=None):
        super(myWindow, self).__init__(parent)

        self.page().mainFrame().addToJavaScriptWindowObject("myWindow", self)
        self.loadFinished.connect(self.on_loadFinished)
        
        self.path_now = os.getcwd()
        self.url = os.path.join(self.path_now, "trainview.html", )
        self.load(QtCore.QUrl("file:///"+self.url))
        
        self.doorstatus=1
       
    #    thread = threading.Thread(target=self.changeDoorStatus)
     #   thread.start()
     #   time.sleep(5000)
     
    @QtCore.pyqtSlot()
    def getdoorstatus (self):
        return self.doorstatus
       
    def changeDoorStatus(self):
        self.doorstatus=self.doorstatus^1 
        
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