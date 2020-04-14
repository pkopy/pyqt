from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import MenuButton

class SecondWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dialog")
        self.setFixedSize(1024, 600)
        self.layout = QGridLayout()
        self.parent = parent

    def on_click1(self):
        self.close()
    def menus(self):
        i = 0
        j = 0
        for w in range(100):
#             if (w['Name']):
#             print(w['Name'])
            button = MenuButton.MenuButton(str(w), self, self.parent)

            # button.move(0, -200)
            self.layout.addWidget(button,i,j)
            j += 1
            if (j == 5):
                i += 1
                j = 0

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        # self.show()

if __name__ == "__main__":
    pass