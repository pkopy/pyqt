from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

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