from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import typing

class MenuButton(QWidget):
    def __init__(self, name, window, parent=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        button = QPushButton(name, self)
        button.resize(150,20)
        
        def on_click2():
            print(name)
            print(parent)
            if (parent):
                parent.label.setText(name)
                parent.progress.setWidth(int(name) * 30)
        button.clicked.connect(on_click2)