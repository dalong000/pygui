import sys
from PyQt5.QtWidgets import *



class GUi(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.win = QWidget()
        self.win.setWindowTitle('窗口')
        self.resize(400,100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUi()
    gui.show()
    sys.exit(app.exec_())

