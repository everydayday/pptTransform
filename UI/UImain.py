import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Slide.slidemain import slide_main # ppt 생성 이미지 만듬
global got_lyric_str

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

        self.btn1.clicked.connect(self.button1Function)
        self.btn2.clicked.connect(self.button2Function)

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

        # QLabel 설명문
        self.lbl_paragraph = QLabel(\
"* 이 프로그램은 입력된 내용을 ppt로 변환해 주는 프로그램입니다.\n\
* 가사의 문단과 문단 사이는 빈 페이지가 생성 됩니다.\n\
* 필요 이상의 빈 페이지가 생성되는걸 방지하기 위해\n\
  문단과 문단 사이 빈 줄은 한 줄 이상 되지 않도록 해주세요." )
        #self.lbl_paragraph.setAlignment(Qt.AlignCenter)
        para_font = self.lbl_paragraph.font()
        para_font.setPointSize(15)
        para_font.setFamily("맑은 고딕")

        # QTextBrowser를 생성한다.
        self.le = QTextEdit()
        # QTextBrowser의 자리표지자를 지정한다
        self.le.setPlaceholderText('가사를 입력하세요.')

        # btn 그룹
        self.btn_group = QGroupBox()

        # btn 추가
        self.btn1 = QPushButton('미리보기')
        self.btn1.resize(100, 100)

        self.btn2 = QPushButton('초기화')
        self.btn2.resize(100, 100)

        # btn layout
        self.btn_group_layout = QHBoxLayout()
        self.btn_group_layout.addWidget(self.btn1)
        self.btn_group_layout.addWidget(self.btn2)
        self.btn_group.setLayout(self.btn_group_layout)


        ##  layout
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.lbl_title)
        self.layout.addWidget(self.lbl_paragraph)
        self.layout.addWidget(self.le)
        self.layout.addWidget(self.btn_group)

        self.setLayout(self.layout)



    def button1Function(self) :
        print(self.le.toPlainText())
        global got_lyric_str
        got_lyric_str = self.le.toPlainText()
        widget.setCurrentIndex(widget.currentIndex() + 1)
        slide_main(got_lyric_str)

    def button2Function(self) :
        self.le.clear()


class MyApp2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.btn1.clicked.connect(self.btn1Function)
        self.btn2.clicked.connect(self.btn2Function)

    def initUI(self):
        self.setWindowTitle('PPT 변환기')
        self.setWindowIcon(QIcon("D:\바탕화면\web.png"))
        self.resize(800, 400)



        # combobox
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


        # Label group
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




        self.lbl_titlea = QLabel('다음 페이지 입니다.')
        self.lbl_titlea.setStyleSheet("color: black;"
                                     "border-style: solid;"
                                     "border-width: 2px;"
                                     "font: 30pt'맑은 고딕';"  # 글자 폰트 설정
                                     "border-color: #26C5A5;"
                                     "border-radius: 3px")

        # btn 그룹
        self.btn_group = QGroupBox()

        # btn 추가
        self.btn1 = QPushButton('뒤로가기')
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
        self.layout.addWidget(self.cb_text_group)
        self.layout.addWidget(self.cb_group)
        self.layout.addWidget(self.lbl_titlea)
        self.layout.addWidget(self.btn_group)


        self.setLayout(self.layout)

    def btn1Function(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


    def btn2Function(self):
        self.le.clear()





def main():
    app = QApplication(sys.argv)

    # 화면 전환용 Widget 설정
    widget = QtWidgets.QStackedWidget()

    # 레이아웃 인스턴스 생성
    myApp = MyApp()
    myApp2 = MyApp2()

    # Widget 추가
    widget.addWidget(myApp)
    widget.addWidget(myApp2)
    widget.show()

    ex = MyApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 화면 전환용 Widget 설정
    widget = QtWidgets.QStackedWidget()

    # 레이아웃 인스턴스 생성
    myApp = MyApp()
    myApp2 = MyApp2()

    # Widget 추가
    widget.addWidget(myApp)
    widget.addWidget(myApp2)
    widget.show()

    ex = MyApp()
    sys.exit(app.exec_())


