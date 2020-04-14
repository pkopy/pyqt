from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from PyQt5 import QtWebSockets

from pprint import pprint
import websocket
import sys
import json
import threading
import Butt
import Icon
import Progress
import SecondWindow
import DisplayMass
from time import sleep
from threading import Timer


        



    
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
        super().__init__(*args, **kwargs)
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
        self.layout1 = QHBoxLayout()
        self.layout1_1 = QVBoxLayout()
        self.layout1_2 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.thread = ListenWebsocket()
        self.thread.start()

        pixmap = QPixmap('progress.png')
        self.progress = Progress.Progress(pixmap)
        self.label = DisplayMass.Mass()
        # self.setCentralWidget(self.progress)
        # self.setCentralWidget(self.label)
        stableIcon = QPixmap('stable_black.svg')
        taraIcon = QPixmap('tara_black.svg')
        zeroIcon = QPixmap('zero.svg')
        self.iconT = Icon.Icon(taraIcon)
        self.iconS = Icon.Icon(stableIcon)
        self.iconZ = Icon.Icon(zeroIcon)
        self.layout1_1.addWidget(self.iconS)
        self.layout1_1.addWidget(self.iconT)
        self.layout1_1.addWidget(self.iconZ)
        # self.layout1.addWidget(self.icons)
        self.layout2.addWidget(self.progress)
        
        self.layout2.setAlignment(Qt.AlignCenter)
        self.layout1.addLayout(self.layout1_1)
        self.layout1_2.addWidget(self.label)
        self.layout1.addLayout(self.layout1_2)

        # button = QPushButton('New', self)
        # self.second = '',
        # second.menus()
        button_action = Butt.Butt( self.thread)
        # self.second.menus([])
        self.layout3.addWidget(button_action)
        # self.layout3.addWidget(button)
        self.mainLayout.addLayout(self.layout1)
        self.mainLayout.addLayout(self.layout2)
        self.mainLayout.addLayout(self.layout3)
#         self.setLayout(self.mainLayout)
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
        self.second = SecondWindow.SecondWindow(self)
        x = json.loads(self.thread.getMessage())
        # print(x['COMMAND'])
        try:
            self.progress.setWidth(int(x['RECORD']['Mass'][0]['NetAct']['Value']))
        except:
            print('coś nie tak')
        if (x['COMMAND'] == 'EDIT_MESSAGE' and x['PARAM'] == 'SHOW' and x['RECORD']['Type'] == 'Catalog'):
            # print(x['RECORD']['Items'])
            # self.dialog.show()
            self.second.menus(x['RECORD']['Items'])
            
        visible = x['RECORD']['Mass'][0]
        self.iconS.setVis(visible['isStab'])
        self.iconT.setVis(visible['isTare'])
        self.iconZ.setVis(visible['isZero'])
        self.label.setText(str(x['RECORD']['Mass'][0]['NetAct']['Value']))
        # print(x['RECORD']['Mass'][0]['isStab'])
        
        # if (int(x['RECORD']['Mass'][0]['NetAct']['Value'])>300):
        #     self.color = '#0000ff'
        # else:
        #     self.color = '#ff0000'
        # self.label.setText('<p style="color:#000000; font-size:150pt">'+x['RECORD']['Mass'][0]['NetAct']['Value']+'</p>')
        # self.label.setText(self.thread.getMessage().RECORD.Mass[0].NetAct.Value)
    

class ListenWebsocket(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)

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


    def on_error(self, ws, error):
        print(error)


    def on_open(self):
        self.WS.send('{"COMMAND": "REGISTER_LISTENER", "PARAM": "MENU"}')
    def on_close(self, ws):
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