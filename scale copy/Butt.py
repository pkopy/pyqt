from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Butt(QWidget):
    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        button_action = QPushButton(QIcon('kolo.svg'),"Tara", self)
        # button_action.sizeHint()
        # x = button_action.keyPressEvent(e)
        # print(x)
        # button_action.setGeometry(QRect(200, 150, 93, 28))\
        button = QPushButton('New Window', self)
        # @pyqtSlot()
#         self.dialog = SecondWindow()
        def on_click1():
            window.show()
#             thread.WS.send("{COMMAND: 'EXECUTE_ACTION', PARAM: 'actSetup'}")
        def on_click():
            print('cliclll')
#             thread.WS.send("{COMMAND: 'EXECUTE_ACTION', PARAM: 'actTarring'}")

        button_action.clicked.connect(on_click)
        button.clicked.connect(on_click1)
        button_action.resize(100,50)
        button.resize(100,50)
        button_action.move(500,10)