import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Slide.slidemain import slide_main # ppt 생성 이미지 만듬
from alarmUI import MiniApp
global got_lyric_str


class MyApp2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.btn1.clicked.connect(self.btn1Function)
        self.btn2.clicked.connect(self.btn2Function)
        self.btn3.clicked.connect(QCoreApplication.instance().quit)

    def initUI(self):
        self.setWindowTitle('PPT 변환기')
        self.setWindowIcon(QIcon("D:\바탕화면\web.png"))
        self.resize(800, 400)


        ##------------- UI -------------- ##

        # ---1. <combobox> ---
        #
        self.cb1_text = QLabel('글꼴')
        self.cb1 = QComboBox()
        self.cb1.addItem('궁서체')
        self.cb1.addItem('굴림체')
        self.cb1.addItem('돋음체')

        self.cb2_text = QLabel('크기')
        self.cb2 = QComboBox()
        self.cb2.addItem('10')
        self.cb2.addItem('15')
        self.cb2.addItem('20')

        self.cb3_text = QLabel('색상')
        self.cb3 = QComboBox()
        self.cb3.addItem('red')
        self.cb3.addItem('blue')
        self.cb3.addItem('white')
        self.cb3.addItem('black')


        #  1-2  <combo_Label group>
        self.cb_text_group = QGroupBox()
        self.cb_text_group_layout = QHBoxLayout()

        self.cb_text_group_layout.addWidget(self.cb1_text)
        self.cb_text_group_layout.addWidget(self.cb2_text)
        self.cb_text_group_layout.addWidget(self.cb3_text)
        self.cb_text_group.setLayout(self.cb_text_group_layout)

        # combo group
        self.cb_group = QGroupBox()
        self.cb_group_layout = QHBoxLayout()


        self.cb_group_layout.addWidget(self.cb1)
        self.cb_group_layout.addWidget(self.cb2)
        self.cb_group_layout.addWidget(self.cb3)
        self.cb_group.setLayout(self.cb_group_layout)

        #


        '''self.lbl_titlea = QLabel('다음 페이지 입니다.')
        self.lbl_titlea.setStyleSheet("color: black;"
                                     "border-style: solid;"
                                     "border-width: 2px;"
                                     "font: 30pt'맑은 고딕';"  # 글자 폰트 설정
                                     "border-color: #26C5A5;"
                                     "border-radius: 3px")
        '''

        # 2. --- img 그룹 ---
        i = 1
        self.pixmap = QPixmap(r'C:\Users\김대희\PycharmProjects\pythonProject2\slideImagefolder\pptimage{}.jpg'.format(i))
        self.lbl_img = QLabel()
        self.lbl_img.setPixmap(self.pixmap)

        # 3. ---btn 그룹 ---
        self.btn_group = QGroupBox()

        # btn 추가
        self.btn1 = QPushButton('뒤로가기')
        self.btn1.resize(100, 100)

        self.btn2 = QPushButton('재생성하기')
        self.btn2.resize(100, 100)

        self.btn3 = QPushButton('이대로하기')
        self.btn3.resize(100, 100)


        # btn layout
        self.btn_group_layout = QHBoxLayout()
        self.btn_group_layout.addWidget(self.btn1)
        self.btn_group_layout.addWidget(self.btn2)
        self.btn_group_layout.addWidget(self.btn3)
        self.btn_group.setLayout(self.btn_group_layout)

        #

        ## -------------- UI_layout ----------------- ##
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.cb_text_group)
        self.layout.addWidget(self.cb_group)
        self.layout.addWidget(self.lbl_img)
        #self.layout.addWidget(self.lbl_titlea)
        self.layout.addWidget(self.btn_group)

        self.setLayout(self.layout)

    ##---------- function -------------- ##
    def btn1Function(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


    def btn2Function(self): # 글꼴, 크기, 색상
         # 변경한 폰트, 색상 매개변수로 넘겨줄 필요.
        font_style = str(self.cb1.currentText())
        font_size = str(self.cb2.currentText())
        font_color = str(self.cb3.currentText())
        print(font_size,font_style,font_color)


        slide_main(got_lyric_str, font_size, font_style)    # pptimage 삭제 시점, App2를 다시 실행...?
        #self.repaint()