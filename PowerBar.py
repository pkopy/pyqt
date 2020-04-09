from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
class _Bar(QtWidgets.QWidget):
    pass

class _Progress(QtWidgets.QWidget):
    def __init__(self, pixmap, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = 'text'
        self.vertLayout = QtWidgets.QVBoxLayout()
        self._label = QLabel(self)
        self._label.setMargin(1)
        self.setWidth
        # self._label.setText(self.text)
        pixmap1 = pixmap.scaledToHeight(49)
        # pixmap.scaled(2,2, Qt.IgnoreAspectRatio)
        self._label.setPixmap(pixmap1)
        self.vertLayout.addWidget(self._label)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )
    def sizeHint(self):
        return QtCore.QSize(400,120)

    def setText(self, text1):
        print(text1)
        self._label.setText(text1)

    def setWidth(self, w):
        self._label.setFixedWidth(w)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor('black'))
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, 200, 50)
        painter.drawRect(rect)

class PowerBar(QtWidgets.QWidget):
    def __init__(self, steps=5, *args, **kwargs):
        super(PowerBar, self).__init__(*args, **kwargs)
        self.setFixedSize(1024, 600)
        self.vertLayout = QtWidgets.QVBoxLayout()
        self.layout1 = QtWidgets.QHBoxLayout()
        self.layout2 = QtWidgets.QHBoxLayout()
        self._bar = _Bar()
        # self.layout.addWidget(self._bar)
        # self._dial = QtWidgets.QDial()
        
        # layout.addWidget(self._dial)
        style = """.QSlider {
            min-height: 68px;
            max-height: 68px;
            background: #5F4141;
            }

            .QSlider::groove:horizontal {
                border: 1px solid #262626;
                height: 5px;
                background: #393939;
                margin: 40px 12px;
            }

            .QSlider::handle:horizontal {
                background: #22B14C;
                border: 5px solid #B5E61D;
                width: 23px;
                height: 100px;
                margin: -24px -12px;
            }"""
        
        
        self._slider = QtWidgets.QSlider(Qt.Horizontal, self)
        self._label = QLabel(self)
        
        self._slider.setStyleSheet(style)
        # self._label.setStyleSheet(style1)
        # self._slider.setStyleSheet(".QSlider {min-height: 68px;max-height: 68px; background:#5f4141} .QSlider::groove:horizontal {height: 5px; background:#393939;border: 1px solid #262626; margin: 48px} .QSlider::handle:horizontal {margin: -24px -12px;background: #22B14C; width: 40px; border: 5px solid #B5E61D;height: 100px; background:#5f4141;border: 5px solid #00ff00;}")
        # self._slider.setStyleSheet("QSlider::groove:horizontal {height: 25px; background:#5f4141;border: 2px solid #00ff00;}")

        # self._slider.setStyleSheet("QSlider::handle:horizontal {height: 150px; background:#5f4141;border: 5px solid #00ff00;}")
        pixmap = QPixmap('progress.png')
        
        self._bar = _Progress(pixmap)
        
        self.layout2.addWidget(self._bar)
        # self.layout.addWidget(self._label)
        self.layout1.addWidget(self._slider)
        self.vertLayout.addLayout(self.layout1)
        self.vertLayout.addLayout(self.layout2)
        self.setLayout(self.vertLayout)
        
        value = self._slider.value()
        self._slider.valueChanged.connect(self.prii)   
        

    def prii(self, s):
        style1 = """Qlabel {
                bacground: #000000;
                border: 5px solid red
            }"""
        pixmap = QPixmap('progress.png')
        # matrix = QMatrix2x2()
        self.pixmap1 = pixmap
        # self._label.setGeometry(0,0, 1000, 50)
        # self._label.setStyleSheet(style1)
        # self._label.setAlignment(Qt.AlignLeft)
        # self.layout2.addWidget(self._label)
        # self._bar.setText(str(s))
        self._bar.setWidth(s)
        # self.pixmap1.transformed(matrix.translate(),s, s)
        # self._label.setPixmap(self.pixmap1)
        # self._label.setText(str(s))
        # self._label.setFixedWidth(s*10)
        # self.setLayout(self.vertLayout)
        # self.layout.addWidget(self._slider)
        
        # self.setLayout(self.layout)
        # print(pixmap.rect())

        
