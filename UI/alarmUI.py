import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Slide.slidemain import slide_main # ppt 생성 이미지 만듬
global got_lyric_str



class MiniApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.btn1.clicked.connect(QCoreApplication.instance().quit)


    def initUI(self):
        self.setWindowTitle('Alarm')
        self.move(300, 300)
        self.resize(200, 100)

        self.lbl1 = QLabel("값을 입력해 주세요.")
        self.lbl1.setStyleSheet("color: black;"
                                "border-style: solid;"
                                "border-width: 2px;"
                                "font: 30pt'맑은 고딕';"  # 글자 폰트 설정
                                "border-color: #26C5A5;"
                                "border-radius: 3px")
        self.lbl_title.setAlignment(Qt.AlignCenter)  # 가운데 맞춤

        self.btn1 = QPushButton("창닫기")
        self.btn1.resize(100, 100)
        print("show 위")
        self.show()




