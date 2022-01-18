import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

        self.btn1.clicked.connect(self.button1Function)

    def initUI(self):
        # 창 Title, Icon 설정
        self.setWindowTitle('PPT 변환기')
        self.move(300, 300)
        self.setWindowIcon(QIcon("D:\바탕화면\web.png"))
        self.resize(800, 400)

        # QLabel 생성
        self.lbl_title = QLabel('PPT 변환기')
        self.lbl_title.setStyleSheet("color: black;"
                                     "border-style: solid;"
                                     "border-width: 2px;"
                                     "font: 30pt'맑은 고딕';"  # 글자 폰트 설정
                                     "border-color: #26C5A5;"
                                     "border-radius: 3px")
        self.lbl_title.setAlignment(Qt.AlignCenter)  # 가운데 맞춤

        # QLineEdit를 생성한다.
        self.le = QLineEdit()
        # QLineEdit의 자리표지자를 지정한다
        self.le.setPlaceholderText('가사를 입력하세요.')

        # btn 그룹
        self.btn_group = QGroupBox()

        # btn 추가
        self.btn1 = QPushButton('미리보기')
        self.btn1.resize(100, 100)

        self.btn2 = QPushButton('생성하기')
        self.btn2.resize(100, 100)

        # btn layout
        self.btn_group_layout = QHBoxLayout()
        self.btn_group_layout.addWidget(self.btn1)
        self.btn_group_layout.addWidget(self.btn2)

        self.btn_group.setLayout(self.btn_group_layout)

        #  layout
        self.layout = QVBoxLayout()
        # 기준
        self.layout.addWidget(self.lbl_title)
        self.layout.addWidget(self.le)
        self.layout.addWidget(self.btn_group)

        self.setLayout(self.layout)

        self.show()

    def button1Function(self) :
        print(self.le.text())

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())