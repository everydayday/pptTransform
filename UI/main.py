import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 창 Title, Icon 설정
        self.setWindowTitle('PPT 변환기')
        self.move(300, 300)
        self.setWindowIcon(QIcon("D:\바탕화면\web.png"))
        self.resize(400, 200)

        #self.statusBar().showMessage('Ready')
        # mainWindow = QMainWindow()
        # mainWindow.statusBar().showMessage('Ready')

        # 제목 박스
        lbl_title = QLabel('PPT 변환기')
        lbl_title.setStyleSheet("color: black;"             ## 글자 폰트 설정,
                              "border-style: solid;"        ## 가운데 맞춤
                              "border-width: 2px;"
                              "font: 50pt;"
                              "font-style: normal;"
                              "border-color: #26C5A5;"
                              "border-radius: 3px")

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_title)

        self.setLayout(vbox)


        # btn = QPushButton('Quit', self)
        # btn.move(50, 50)
        # btn.resize(btn.sizeHint())
        # btn.clicked.connect(QCoreApplication.instance().quit)
        #
        # QToolTip.setFont(QFont('SansSerif', 10))
        # btn.setToolTip('This is a <b>QQuitButton</b> widget')



        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())