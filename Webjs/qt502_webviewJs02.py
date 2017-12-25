# -*- coding: utf-8 -*- 

'''
    【简介】pyqt与js的双向传输
    QWebEngineView只能在pyqt5.6+里用
	QWebView中网页加载html+js
	pyqt点击事件调用js里的方法
	js点击事件传值到pyqt
	
  
'''
import sys
import os
from Webjs.MySharedObject  import MySharedObject

from PyQt5.QtWidgets  import QApplication , QWidget , QVBoxLayout , QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl  

from PyQt5.QtWebChannel import  QWebChannel 


# 创建一个 application实例
app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle('Web页面中的JavaScript与 QWebEngineView交互例子')

# 创建一个垂直布局器
layout = QVBoxLayout()
win.setLayout(layout)

# 创建一个 QWebEngineView 对象
view =  QWebEngineView()
htmlUrl = '.index.html'

#path_now = os.getcwd()
#url = os.path.join(path_now, "index.html", )
#view.load( QUrl("file:///"+url))
view.load( QUrl('file:///D:/JavaWeb/eclipse_workspace/FirstPy/Webjs/web/index.html'))

# 创建一个 QWebChannel对象，用来传递pyqt参数到JavaScript
channel =  QWebChannel( )
myObj = MySharedObject()   
channel.registerObject( "bridge", myObj )  
view.page().setWebChannel(channel)

# 创建一个按钮去调用 JavaScript代码
button = QPushButton('设置全名')

def js_callback(result):
    print(result)
    
def complete_name():
   print('complete_name function')
   view.page().runJavaScript('javascriptFunction();', js_callback)

# 按钮连接 'complete_name'槽，当点击按钮是会触发信号
button.clicked.connect(complete_name)

 
# 把QWebView和button加载到layout布局中
layout.addWidget(view)
layout.addWidget(button)

           
# 显示窗口和运行app
win.show()
sys.exit(app.exec_())
