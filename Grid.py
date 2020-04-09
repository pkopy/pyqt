from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class Mass(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = 'text'
        # self.vertLayout = QVBoxLayout()
        self._label = QLabel(self)
        self._label.setText(self.text)
        # self.vertLayout.addWidget(self._label)

    def setText(self, text1):
        print(text1)
        self._label.setText(text1)

class _Progress(QWidget):
    def __init__(self, pixmap, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = 'text'
        # self.vertLayout = QVBoxLayout()
        self._label = QLabel(self)
        self._label.setMargin(1)
        
        pixmap1 = pixmap.scaledToHeight(49)
        # pixmap.scaled(2,2, Qt.IgnoreAspectRatio)
        self._label.setPixmap(pixmap1)
        # self.vertLayout.addWidget(self._label)
        self._label.setFixedWidth(0)
        # self.setSizePolicy(
        #     QSizePolicy.MinimumExpanding,
        #     QSizePolicy.MinimumExpanding
        # )
        # self.paintEvent()
        
    def sizeHint(self):
        return QtCore.QSize(400,120)

    def setText(self, text1):
        print(text1)
        self._label.setText(text1)

    def setWidth(self, w):
        if(w >= 0):
            self._label.setFixedWidth(w)
        else:
            self._label.setFixedWidth(0)

    def paintEvent(self,e):
        painter = QPainter(self)
        brush = QBrush()
        brush.setColor(QColor('black'))
        brush.setStyle(Qt.SolidPattern)
        rect = QRect(0, 0, 600, 50)
        painter.drawRect(rect)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("My Awesome App")
        # layout = QGridLayout()
        # layout.addWidget(Color('red'), 0, 0)
        # layout.addWidget(Color('yellow'), 0, 1)
        # layout.addWidget(Color('green'), 1, 0)
        # layout.addWidget(Color('blue'), 1, 1)
        # layout.addWidget(Color('purple'), 2, 1)

        layout = QVBoxLayout()

        mass = Mass()
        pixmap = QPixmap('progress.png')
        prog = _Progress(pixmap)
        layout.addWidget(mass)
        layout.addWidget(prog)
        layout.addWidget(Color('blue'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()