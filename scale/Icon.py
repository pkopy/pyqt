from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

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