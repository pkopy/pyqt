from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Progress(QWidget):
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