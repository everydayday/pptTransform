import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.setWindowIcon(QIcon("D:\바탕화면\web.png"))
        self.resize(400, 200)

        self.statusBar().showMessage('Ready')
        # mainWindow = QMainWindow()
        # mainWindow.statusBar().showMessage('Ready')


        btn = QPushButton('Quit', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        QToolTip.setFont(QFont('SansSerif', 10))
        btn.setToolTip('This is a <b>QQuitButton</b> widget')

        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())