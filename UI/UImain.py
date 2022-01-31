import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Slide.slidemain import slide_main # ppt 생성 이미지 만듬
from alarmUI import MiniApp
from UImain2 import MyApp2
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

        self.move(0, 0)
        self.setWindowIcon(QIcon(r"D:\바탕화면\web.png"))
        self.resize(1600, 800)

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
"* 이 프로그램은 입력된 노래가사를 ppt로 변환해 주는 프로그램입니다.\n\
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
        got_lyric_str.strip()
        if got_lyric_str == '':
            print("here is in if")
            MiniApp()
            widget.setCurrentIndex(widget.currentIndex())

        slide_main(got_lyric_str)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def button2Function(self) :
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


