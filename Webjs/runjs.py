# -*- coding: utf-8 -*- 

'''
    【简介】
    QWebView中网页调用JavaScript 
  
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
view.setHtml('''
<html>
    <head>
      <title>A Demo Page</title>
      <meta charset="UTF-8">
      <script src="./web/qwebchannel.js"></script>
      <script language="javascript">
        function javascriptFunction() {
              
              alert('Call javascriptFunction' );
              
             
              return 'Back javascriptFunction';
            }

        function completeAndReturnName() {
          var fname = document.getElementById('fname').value;
          var lname = document.getElementById('lname').value;
          var full = fname + ' ' + lname;

          document.getElementById('fullname').value = full;
          document.getElementById('submit-btn').style.display = 'block';

          return full;
        }
                      
       
        
          function onShowMsgBox() {
            alert('window.bridge=' + window.bridge);
            
            if ( window.bridge) {
                alert('点击事件：bridge.strValue=' + window.bridge.strValue ) ;
             
                var fname = document.getElementById('fname').value;
                 alert('fname=' + fname )
                window.bridge.strValue = fname;//call method _setStrValue in MySharedObject Class
                
                
            }
            
        }

      </script>     
    </head>

    <body>
      <form>
        <label for="姓名">user name:</label>
        <input type="text" name="fname" id="fname"></input>
        <br />
        <input type="button" value="传递参数到pyqt" onclick="onShowMsgBox()">
        <input type="reset" value='重置'/>
      </form>
    </body>
  </html>

''')



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
