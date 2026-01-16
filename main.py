import sys
from time import sleep

from PyQt6 import QtWidgets, uic
from UI import Ui_MainWindow

from start_minecraft import MCUtils


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)


        self.startButton.clicked.connect(startMC)


def startMC():
    mc = MCUtils()
    mc.download()
    window.hide()
    mc.start()
    window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
