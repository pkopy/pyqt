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

class Icon(QWidget):
    def __init__(self, pixmap, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.vertLayout = QVBoxLayout()
        self._labelI = QLabel(self)
        self._labelI.setAlignment(Qt.AlignLeft)
        # self._label= QLabel(self)
        # self._label.setAlignment(Qt.AlignLeft)
        # self.pixmap = QPixmap('stable_black.svg')
            # self.pixmap = QPixmap('stable_black.svg')
        self.pixmap1 = pixmap.scaledToHeight(20)
        self._labelI.setPixmap(self.pixmap1)
        # self._label.setText('TTTT')
        
        # self.vertLayout.addWidget(self._labelI)
        # self.vertLayout.addWidget(self._label)
        # self.pixmap = QPixmap()
        # widget = QWidget()
        # widget.setLayout(self.vertLayout)
        # self.setCentralWidget(widget)
    
    def setVis(self, isVisible):
        # print(isVisible)
        if (isVisible == False):
            # self.pixmap1.detach()
            self._labelI.setFixedWidth(0)
        else:
            # self.pixmap1.detach()
            self._labelI.setFixedWidth(100)

            
            
        # else:
        #     # pixmap = QPixmap('stable_black.svg')
        #     pixmap1.detach()
        #     # self.pixmap = QPixmap()
        # # self.pixmap1 = self.pixmap.scaledToHeight(20)
        
class Mass(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = 'INIT SCALE'
        # self.vertLayout = QVBoxLayout()
        self._label = QLabel(self)
        self._label.setMargin(0)
        self._label.setAlignment(Qt.AlignLeft)
        self.color = '#000000'
        
        self._label.setText('<p style="color:#000000; font-size:130pt">'+self.text+'</p>')
        # self.vertLayout.addWidget(self._label)

    def setText(self, text1):
        # print(text1)
        # color = '#000000'
        if (int(text1) < 0):
            self.color = '#ff0000'
        else:
            self.color='#000000'
        self._label.setText('<p style="color:'+ self.color +'; font-size:130pt">'+text1+'</p>')

class _Progress(QWidget):
    def __init__(self, pixmap, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = 'text'
        self.vertLayout = QVBoxLayout()
        self._label = QLabel(self)
        self._label.setMargin(1)
        
        pixmap1 = pixmap.scaledToHeight(49)
        # pixmap.scaled(2,2, Qt.KeepAspectRatioByExpanding)
        # pixmap.
        self._label.setPixmap(pixmap1)
        # self.vertLayout.addWidget(self._label)
        self._label.setFixedWidth(0)
        # self.setSizePolicy(
        #     QSizePolicy.MinimumExpanding,
        #     QSizePolicy.MinimumExpanding
        # )
        # self.paintEvent()
        # self._label.move(0,50)
    def sizeHint(self):
        return QSize(605,120)

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

class Butt(QWidget):
    def __init__(self, thread, *args, **kwargs):
        super().__init__(*args, **kwargs)
        button_action = QPushButton(QIcon('kolo.svg'),"Tara", self)
        # button_action.sizeHint()
        # x = button_action.keyPressEvent(e)
        # print(x)
        # button_action.setGeometry(QRect(200, 150, 93, 28))\
        button = QPushButton('New Window', self)
        # @pyqtSlot()
        self.dialog = SecondWindow()
        def on_click1():
            # self.dialog.show()
            thread.WS.send("{COMMAND: 'EXECUTE_ACTION', PARAM: 'actSetup'}")
        def on_click(button_action):
            print('cliclll')
            thread.WS.send("{COMMAND: 'EXECUTE_ACTION', PARAM: 'actTarring'}")

        button_action.clicked.connect(on_click)
        button.clicked.connect(on_click1)
        button_action.resize(100,50)
        button.resize(100,50)
        button_action.move(500,10)

class SecondWindow(QMainWindow):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.setWindowTitle("Dialog")
        self.setFixedSize(1024, 600)
        self.layout = QGridLayout()
    def menus(self, array):
        i = 0
        j = 0
        for w in array:
            if (w['Name']):
                button = QPushButton(w['Name'])
                # button.move(0, -200)
                self.layout.addWidget(button,i,j)
                j += 1
                if (j == 5):
                    i += 1
                    j = 0
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        self.show()
    
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
        self.layout1 = QHBoxLayout()
        self.layout1_1 = QVBoxLayout()
        self.layout1_2 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layout3 = QHBoxLayout()
        self.thread = ListenWebsocket()
        self.thread.start()

        pixmap = QPixmap('progress.png')
        self.progress = _Progress(pixmap)
        self.label = Mass()
        # self.setCentralWidget(self.progress)
        # self.setCentralWidget(self.label)
        stableIcon = QPixmap('stable_black.svg')
        taraIcon = QPixmap('tara_black.svg')
        zeroIcon = QPixmap('zero.svg')
        self.iconS = Icon(stableIcon)
        self.iconT = Icon(taraIcon)
        self.iconZ = Icon(zeroIcon)
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
        button_action = Butt(self.thread)
        self.layout3.addWidget(button_action)
        # self.layout3.addWidget(button)
        self.mainLayout.addLayout(self.layout1)
        self.mainLayout.addLayout(self.layout2)
        self.mainLayout.addLayout(self.layout3)
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
        self.dialog = SecondWindow()
        x = json.loads(self.thread.getMessage())
        # print(x['COMMAND'])
        try:
            self.progress.setWidth(int(x['RECORD']['Mass'][0]['NetAct']['Value']))
        except:
            print('coś nie tak')
        if (x['COMMAND'] == 'EDIT_MESSAGE' and x['PARAM'] == 'SHOW' and x['RECORD']['Type'] == 'Catalog'):
            print(x['RECORD']['Items'])
            # self.dialog.show()
            self.dialog.menus(x['RECORD']['Items'])
            
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