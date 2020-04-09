from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from PyQt5 import QtWebSockets

from pprint import pprint
import websocket
import sys
import json
import threading
from time import sleep
from threading import Timer

class Mass(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = '8888888'
        # self.vertLayout = QVBoxLayout()
        self._label = QLabel(self)
        self._label.setMargin(10)
        self._label.setAlignment(Qt.AlignRight)
        self.color = '#000000'
        
        self._label.setText('<p style="color:#000000; font-size:150pt">'+self.text+'</p>')
        # self.vertLayout.addWidget(self._label)

    def setText(self, text1):
        print(text1)
        # color = '#000000'
        if (int(text1) < 0):
            self.color = '#ff0000'
        else:
            self.color='#000000'
        self._label.setText('<p style="color:'+ self.color +'; font-size:150pt">'+text1+'</p>')

class _Progress(QWidget):
    def __init__(self, pixmap, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = 'text'
        self.vertLayout = QVBoxLayout()
        self._label = QLabel(self)
        self._label.setMargin(1)
        
        pixmap1 = pixmap.scaledToHeight(49)
        pixmap.scaled(2,2, Qt.KeepAspectRatioByExpanding)
        # pixmap.
        self._label.setPixmap(pixmap1)
        # self.vertLayout.addWidget(self._label)
        self._label.setFixedWidth(0)
        # self.setSizePolicy(
        #     QSizePolicy.MinimumExpanding,
        #     QSizePolicy.MinimumExpanding
        # )
        # self.paintEvent()
        
    def sizeHint(self):
        return QSize(400,120)

    def setText(self, text1):
        print(text1)
        self._label.setText(text1)

    def setWidth(self, w):
        if(w > 0):
            self._label.setFixedWidth((w/3000)*600)
        else:
            self._label.setFixedWidth(0)

    def paintEvent(self,e):
        painter = QPainter(self)
        brush = QBrush()
        brush.setColor(QColor('black'))
        brush.setStyle(Qt.SolidPattern)
        rect = QRect(0, 0, 600, 50)
        painter.drawRect(rect)
    
class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.windowTitleChanged.connect(self.onWindowTitleChange)
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))
        self.setWindowTitle("My window")
        self.setFixedSize(1024, 600)
        # self.label = QLabel("THIS IS AWESOME!!!")
        # self.label.setTextFormat(Qt.RichText)
        # self.setCentralWidget(self.label)
        # self.label.setAlignment(Qt.AlignCenter)
        
        # self.label1 = QLabel("THIS IS AWESOME!!!")
        # self.label1.setAlignment(Qt.AlignCenter)
        # self.setCentralWidget(self.label1)
        # toolbar = QToolBar("My main toolbar")
        # toolbar.iconSize
        # self.addToolBar(toolbar)

        self.mainLayout = QVBoxLayout()
        self.thread = ListenWebsocket()
        self.thread.start()

        pixmap = QPixmap('progress.png')
        self.progress = _Progress(pixmap)
        self.label = Mass()
        # self.setCentralWidget(self.progress)
        # self.setCentralWidget(self.label)
        
        
        self.mainLayout.addWidget(self.label)
        self.mainLayout.addWidget(self.progress)
        self.setLayout(self.mainLayout)
        widget = QWidget()
        widget.setLayout(self.mainLayout)
        self.setCentralWidget(widget)
        
        # self.client = QtWebSockets.QWebSocket("",QtWebSockets.QWebSocketProtocol.Version13,None)
        # self.client.open(QUrl("ws://10.10.3.60:4101"))
        # self.client.sendTextMessage('{"COMMAND": "REGISTER_LISTENER", "PARAM": "MENU"}')
        # text = self.client.textMessageReceived
        # text.connect(self.onWindowTitleChange)
        # pprint(text)
        # for attr in dir(text):
        #     print("obj.%s = %r" % (attr, getattr(text, attr)))
        # button_action = QAction(QIcon("kolo.svg"),"Your button", self)
        # button_action2 = QAction(QIcon("kolo.svg"),"Second", self)
        # toolbar.setToolButtonStyle(Qt.ToolButtonTextOnly)
        # button_action.setStatusTip("This is your button")
        # button_action.triggered.connect(self.onMyToolBarButtonClick)
        # button_action.setCheckable(True)
        # toolbar.addAction(button_action)
        # toolbar.addSeparator()
        # button_action2.setStatusTip("Second")
        # button_action2.triggered.connect(self.onMyToolBarButtonClick)
        # button_action2.setCheckable(True)
        # toolbar.addAction(button_action2)
        # toolbar.addWidget(QLabel("Hello"))
        # toolbar.addWidget(QCheckBox())
        # toolbar.setIconSize(QSize(50,50))
        self.color = '#ff0000'

        self.setStatusBar(QStatusBar(self))

        # menu = self.menuBar()
        # file_menu = menu.addMenu("&File")
        # file_menu.addAction(button_action)
        # file_menu.addSeparator()
        # file_menu.addAction(button_action2)
        # socket = QtWebSockets.QWebSocket('test')

        self.xman = self.thread.getMessage()
        # print('dddd'+xman)
        # self.label.setText(self.xman)


    def onWindowTitleChange(self, s):
        print("processTextMessage - message: {}".format(s))

    def my_custom_fn(self, a="HELLLO!", b=5):
        print(a, b)
    
    def onMyToolBarButtonClick(self, s):
        self.color = '#000000'
        
        # print(self.thread.getMessage())
    def send(self):
        self.thread.WS.send("{COMMAND: 'GET_MOD_INFO'}")
        x = json.loads(self.thread.getMessage())
        self.progress.setWidth(int(x['RECORD']['Mass'][0]['NetAct']['Value']))

        self.label.setText(str(x['RECORD']['Mass'][0]['NetAct']['Value']))
        # if (int(x['RECORD']['Mass'][0]['NetAct']['Value'])>300):
        #     self.color = '#0000ff'
        # else:
        #     self.color = '#ff0000'
        # self.label.setText('<p style="color:#000000; font-size:150pt">'+x['RECORD']['Mass'][0]['NetAct']['Value']+'</p>')
        # self.label.setText(self.thread.getMessage().RECORD.Mass[0].NetAct.Value)
    

class ListenWebsocket(QThread):
    def __init__(self, parent=None):
        super(ListenWebsocket, self).__init__(parent)

        websocket.enableTrace(True)

        self.WS = websocket.WebSocketApp("ws://10.10.3.60:4101",
                                on_message = self.on_message,
                                on_error = self.on_error,
                                on_close = self.on_close) 
                                
        self.test ='SSSS'
        self.mass = 0
    def getMessage(self):
        return self.test
    def setMessage(self, text):
        self.test = text

    def run(self):
        self.WS.on_open = self.on_open

        self.WS.run_forever()


    def on_message(self, message):
        y = json.loads(message)
        # print('text: '+self.text)
        # print("test:" + y)
        self.test = message
        
        # print('text: '+test)


    def on_error(ws, error):
        print(error)


    def on_open(self):
        self.WS.send('{"COMMAND": "REGISTER_LISTENER", "PARAM": "MENU"}')
    def on_close(ws):
        print("### closed ###")

    
class Xman():
    def __init__(self):
        self.x = 'pppp'

    def getMessage(self):
        return self.x


app = QApplication(sys.argv)
window = MainWindow()
window.show()

rt = RepeatedTimer(0.2, window.send)
# try:
#     sleep(5) # your long-running job goes here...
# finally:
#     rt.stop() 


app.exec_()