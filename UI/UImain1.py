import shutil
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import time

from pptx.util import Pt
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Slide.slidemain import slide_main # ppt 생성 이미지 만듬
from PIL import ImageColor

global got_lyric_str


font_col_rgb = (255,255,255)  # font col rgb 값 : 전역변수,,, font col 선택하기 전에도 값은 있어야 함 = > 전역변수
background_col_rgb = (0,0,0)
class MyApp(QWidget):    #  QWidget vs Qmainwindow

    def __init__(self):
        super().__init__()
        self.initUI()

        self.btn1.clicked.connect(self.button1Function)
        self.btn2.clicked.connect(self.button2Function)

        '''self.setWindowTitle("PPT 변환기")
        self.setFixedSize(800,500) # widget 들의 전체적인 크기 # not window 크기
        self.resize(1000,500)
        self.setGeometry(0,0,1500,1500) # 바뀌질 않네...
        
        '''


    def initUI(self):
        # 창 Title, Icon 설정
        #self.resize(100, 100)
        self.move(300, 300)

        widget.setFixedWidth(600)
        widget.setFixedHeight(500)




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
"* 이 프로그램은 입력된 가사를 ppt로 변환해 주는 프로그램입니다.\n\
* 한 페이지 당 두 줄의 가사가 입력되고, 빈 줄 하나당 빈 페이지 하나씩 생성됩니다.\n")
        #self.lbl_paragraph.setAlignment(Qt.AlignCenter)
        para_font = self.lbl_paragraph.font()
        para_font.setPointSize(15)
        para_font.setFamily("맑은 고딕")

        # combo label group
        self.lbl1_font_style = QLabel('글꼴')
        self.lbl2_font_size = QLabel('크기')
        self.lbl3_font_color = QLabel('폰트색')
        self.lbl4_background_color = QLabel('배경색')

        self.lbl1_font_style.setAlignment(Qt.AlignCenter)
        self.lbl2_font_size.setAlignment(Qt.AlignCenter)
        self.lbl3_font_color.setAlignment(Qt.AlignCenter)
        self.lbl4_background_color.setAlignment(Qt.AlignCenter)

        self.cb_lbl_group = QGroupBox()
        self.cb_lbl_group_layout = QHBoxLayout()

        #lbl_list = [self.lbl1_font_style,self.lbl2_font_size,self.lbl3_font_color,self.lbl4_background_color]
        self.cb_lbl_group_layout.addWidget(self.lbl1_font_style)
        self.cb_lbl_group_layout.addWidget(self.lbl2_font_size)
        self.cb_lbl_group_layout.addWidget(self.lbl3_font_color)
        self.cb_lbl_group_layout.addWidget(self.lbl4_background_color)
        self.cb_lbl_group.setLayout(self.cb_lbl_group_layout)


        # combobox
        self.cb1_font_style = QComboBox()
        cb1_font_style_list = ['굴림', '굴림체', '궁서', '궁서체',  '돋음', '돋음체', '바탕','바탕체']
        self.cb1_font_style.addItems(cb1_font_style_list)
        self.cb1_font_style.setCurrentIndex(4)


        self.cb2_font_size = QComboBox() # 매개변수 넘겨줄 때 int형으로 바꾸어 줌
        cb2_font_size_list = ['8','9','10','10.5','11','12','14','16','18','20','24','28','32','36','40','44','48']
        self.cb2_font_size.addItems(cb2_font_size_list)
        self.cb2_font_size.setCurrentIndex(12)

        # color palette
        pal = self.cb2_font_size.palette()
        pal.setColor(QtGui.QPalette.Button, QtGui.QColor(255, 255, 255))
        self.cb2_font_size.setPalette(pal)


        # progress Bar
        self.pbar = QProgressBar(self)

        # 색상 표 생성
        self.cb3_font_col = QPushButton('클릭하여 변경', self)
        #self.cb3_font_col = QPushButton()
        self.cb3_font_col.setStyleSheet("background-color: rgb(255,255,255)")
        self.cb3_font_col.clicked.connect(self.showDialog_font)  # 어느 함수에서 주었는지 구분해주는 인자

        self.cb4_font_col = QPushButton('클릭하여 변경',self)
        self.cb4_font_col.setStyleSheet("background-color: rgb(0,0,0)")
        self.cb4_font_col.clicked.connect(self.showDialog_background)

        # combobox group
        self.cb_group = QGroupBox()
        self.cb_group_layout = QHBoxLayout()

        self.cb_group_layout.addWidget(self.cb1_font_style)
        self.cb_group_layout.addWidget(self.cb2_font_size)
        self.cb_group_layout.addWidget(self.cb3_font_col)
        self.cb_group_layout.addWidget(self.cb4_font_col)
        self.cb_group.setLayout(self.cb_group_layout)



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


        # ------img
        global pptimage_num
        pptimage_num = 0
        pixmap = QPixmap('pptimage{}.png'.format(pptimage_num))

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)


        ##  -------------layout--------------
        self.layout = QVBoxLayout()

        #self.layout.addWidget(lbl_img)


        self.layout.addWidget(self.lbl_title)
        self.layout.addWidget(self.cb_lbl_group)
        self.layout.addWidget(self.cb_group)
        self.layout.addWidget(self.lbl_paragraph)
        self.layout.addWidget(self.le)
        self.layout.addWidget(self.btn_group)

        #self.layout.removeWidget()
        self.setLayout(self.layout)

        #self.show()

    def showDialog_font(self): #color dialog 표시
        col = QColorDialog.getColor()

        hex = col.name()

        global font_col_rgb
        font_col_rgb = ImageColor.getcolor(hex, "RGB")

    def showDialog_background(self): #color dialog 표시
        col = QColorDialog.getColor()

        hex = col.name()

        global background_col_rgb
        background_col_rgb = ImageColor.getcolor(hex, "RGB")

    def button1Function(self) :  # 미리보기
        print(self.le.toPlainText())
        # 기존에 남아있던 이미지 파일 삭제
        #os.remove("..\slideImagefolder\pptimage0.png")
        shutil.rmtree("..\slideImagefolder")
        os.mkdir("..\slideImagefolder")
        print("after os.remove")

        global got_lyric_str
        got_lyric_str = (self.le.toPlainText()).strip()

        print("font_col_rgb in button1Fucntion",font_col_rgb)
        print("What is type of font_col_rgb",type(font_col_rgb))  ### That is tuple
        font_style = str(self.cb1_font_style.currentText())
        font_size = int(self.cb2_font_size.currentText())
        print("ppt 생성 중 입니다.")

        # https://stackoverflow.com/questions/40519375/what-does-x-is-used-prior-to-global-declaration-mean-python-2
        font_col_rgb
        print("after font_col_rgb in button1")
        global background_col_rgb
        print("after background_col_rgb")
        slide_main(got_lyric_str,font_style,font_size,font_col_rgb,background_col_rgb)
        print("ppt 생성 완료되었습니다")

        myApp2 = MyApp2()     # 이것 때문에 2번째 위젯에서 만든 ppt img가 반영되엇나봐
        widget.addWidget(myApp2)

        widget.setCurrentIndex(widget.currentIndex() + 1)

    def button2Function(self): # 초기화
        self.le.clear()
        global pptimage_num
        pptimage_num += 1
        print(pptimage_num)
        self.cb3_font_col.setStyleSheet("background-color: rgb(0,0,0)")   # 이것만 있어도 update 반영됨.
        #self.repaint()


image_num = 0
# 두번째 widget
class MyApp2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.btn1.clicked.connect(self.btn1Function)
        self.btn2.clicked.connect(self.btn2Function)
        self.btn3.clicked.connect(self.btn3Function)

    def initUI(self):
        self.setWindowTitle('PPT 변환기')
        self.setWindowIcon(QIcon("../garbage/web.png"))
        self.resize(200,600)
        #self.setGeometry(0,0, 800, 400)
        #self.setFixedSize(800,600) # it works that changing widget size

        widget.setFixedWidth(600)   # 생성 될 때는 두번 째 widget이 이 크기로 설정이 되나
        widget.setFixedHeight(500)   # 실행 된 이후로는 처음 widget에서 변함이 없음

        # combo label group
        self.lbl1_font_style = QLabel('글꼴')
        self.lbl2_font_size = QLabel('크기')
        self.lbl3_font_color = QLabel('폰트색')
        self.lbl4_background_color = QLabel('배경색')

        self.lbl1_font_style.setAlignment(Qt.AlignCenter)
        self.lbl2_font_size.setAlignment(Qt.AlignCenter)
        self.lbl3_font_color.setAlignment(Qt.AlignCenter)
        self.lbl4_background_color.setAlignment(Qt.AlignCenter)

        self.cb_lbl_group = QGroupBox()
        self.cb_lbl_group_layout = QHBoxLayout()

        # lbl_list = [self.lbl1_font_style,self.lbl2_font_size,self.lbl3_font_color,self.lbl4_background_color]
        self.cb_lbl_group_layout.addWidget(self.lbl1_font_style)
        self.cb_lbl_group_layout.addWidget(self.lbl2_font_size)
        self.cb_lbl_group_layout.addWidget(self.lbl3_font_color)
        self.cb_lbl_group_layout.addWidget(self.lbl4_background_color)
        self.cb_lbl_group.setLayout(self.cb_lbl_group_layout)

        # combobox
        self.cb1_font_style_text = QLabel('글꼴')
        self.cb1_font_style = QComboBox()
        cb1_font_style_list = [ '굴림', '굴림체', '궁서', '궁서체',  '돋음', '돋음체', '바탕','바탕체']
        self.cb1_font_style.addItems(cb1_font_style_list)
        self.cb1_font_style.setCurrentIndex(4)



        self.cb2_font_size_text = QLabel('크기')
        self.cb2_font_size = QComboBox()  # 매개변수 넘겨줄 때 int형으로 바꾸어 줌
        cb2_font_size_list = ['8', '9', '10', '10.5', '11', '12', '14', '16', '18', '20', '24', '28', '32', '36','40', '44', '48']
        self.cb2_font_size.addItems(cb2_font_size_list)
        self.cb2_font_size.setCurrentIndex(12)

        # 색상 표 생성
        self.cb3_font_col = QPushButton('클릭하여 변경', self)
        self.cb3_font_col.setStyleSheet("background-color: rgb(255,255,255)")
        self.cb3_font_col.clicked.connect(self.showDialog_font)  # 어느 함수에서 주었는지 구분해주는 인자

        self.cb4_background_color = QPushButton('클릭하여 변경', self)
        self.cb4_background_color.setStyleSheet("background-color: rgb(0,0,0)")
        self.cb4_background_color.clicked.connect(self.showDialog_background)

        # Label group
        self.cb_text_group = QGroupBox()
        self.cb_text_group_layout = QHBoxLayout()

        self.cb_text_group_layout.addWidget(self.cb1_font_style_text)
        self.cb_text_group_layout.addWidget(self.cb2_font_size_text)
        self.cb_text_group.setLayout(self.cb_text_group_layout)

        # combo group
        self.cb_group = QGroupBox()
        self.cb_group_layout = QHBoxLayout()


        self.cb_group_layout.addWidget(self.cb1_font_style)
        self.cb_group_layout.addWidget(self.cb2_font_size)
        self.cb_group_layout.addWidget(self.cb3_font_col)
        self.cb_group_layout.addWidget(self.cb4_background_color)
        self.cb_group.setLayout(self.cb_group_layout)

        self.lbl_titlea = QLabel('다음 페이지 입니다.')
        self.lbl_titlea.setStyleSheet("color: black;"
                                     "border-style: solid;"
                                     "border-width: 2px;"
                                     "font: 30pt'맑은 고딕';"  # 글자 폰트 설정
                                     "border-color: #26C5A5;"
                                     "border-radius: 3px")

        # 2. --- img 그룹 ---
        global image_num

        pixmap = QPixmap('..\slideImagefolder\pptimage{}.png'.format(image_num))

        self.lbl_img = QLabel()
        self.lbl_img.setPixmap(pixmap)


        '''self.lbl_img = QLabel(self)
        self.lbl_img.resize(800, 400)
        self.lbl_img.setPixmap(self.pixmap)'''
        # btn 그룹
        self.btn_group = QGroupBox()

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

        ## -------------- UI_layout ----------------- ##
        self.layout = QVBoxLayout()

        #self.layout.addWidget(self.cb_text_group)
        self.layout.addWidget(self.cb_lbl_group)
        self.layout.addWidget(self.cb_group)
        #self.layout.addWidget(self.lk_lbl)
        self.layout.addWidget(self.lbl_img)
        #self.layout.addWidget(self.lbl_img)
        # self.layout.addWidget(self.lbl_titlea)
        self.layout.addWidget(self.btn_group)



        self.setLayout(self.layout)

        # widget.repaint()
        #widget.show() # 이거 왜 있지 .. 없어도 큰 문제 없긴 함.
        #self.show()

    def showDialog_font(self):  # color dialog 표시
        col = QColorDialog.getColor()

        hex = col.name()

        global font_col_rgb
        font_col_rgb = ImageColor.getcolor(hex, "RGB")

    def showDialog_background(self):  # color dialog 표시
        col = QColorDialog.getColor()
        hex = col.name()

        global background_col_rgb
        background_col_rgb = ImageColor.getcolor(hex, "RGB")

    def btn1Function(self): # 뒤로가기

        widget.setCurrentIndex(widget.currentIndex() - 1)


    def btn2Function(self): # 재생성 하기
        # 이미지 삭제(현 imageViewer 에 있는 값 삭제 후 다시 생성)
        '''i = 0
        while(True):
            try:
                os.remove("..\slideImagefolder\pptimage{}.jpg".format(i))
                print("this is i",i)
                i += 1
            except:
                break
        '''

        shutil.rmtree("..\slideImagefolder")
        os.mkdir("..\slideImagefolder")
        print(got_lyric_str)
        font_style = str(self.cb1_font_style.currentText()) # default 값 선택해도 오류나지 않음
        font_size = int(self.cb2_font_size.currentText())

        slide_main(got_lyric_str, font_style, font_size, font_col_rgb, background_col_rgb)

        # img 재지정
        # 2. --- img 그룹 ---
        global image_num
        print("global image_num", image_num)
        pixmap = QPixmap('..\slideImagefolder\pptimage{}.png'.format(image_num))
        self.lbl_img.setPixmap(pixmap)

        #self.setLayout(self.layout)

        '''self.layout.removeWidget(self.lbl_img)
        self.lbl_img.deleteLater()
        self.lbl_img = None
        widget.repaint()'''

        #widget.repaint()   # 안 됨
        #widget.quit()  안 먹히는 명령어(존재하지 않는 명령어)
        # widget.show() 안 됨
        #widget.update() 안 됨

        widget.activateWindow()
        '''widget.setCurrentIndex(widget.currentIndex()-1) # setCurrentIndex는 잠깐 왔다갔다 할 용도는 안 되는 듯.
        time.sleep(3)  # 창의 전환 확인하기 위해 멈춤          # 말 그대로 고정용
        widget.setCurrentIndex(widget.currentIndex()+1)''' # 이전으로 전환은 되지만 갔다 왔다는 안 먹힘

        print("after widget.repaint")

    def btn3Function(self): # 이대로 하기
        #widget.close()
        global image_num
        image_num = image_num+ 1
        print("image_num in btn3Function :",image_num)
        self.repaint()

'''def main(): # 필요 없는 부분인 듯
    app = QApplication(sys.argv)

    # 화면 전환용 Widget 설정
    widget = QtWidgets.QStackedWidget()

    # 레이아웃 인스턴스 생성
    myApp = MyApp()ㅇ    myApp2 = MyApp2()

    # Widget 추가
    widget.addWidget(myApp)
    widget.addWidget(myApp2)
    widget.show()

    ex = MyApp()
    sys.exit(app.exec_())'''


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 화면 전환용 Widget 설정
    global widget
    widget = QtWidgets.QStackedWidget()

    # 레이아웃 인스턴스 생성
    myApp = MyApp()
    #myApp2 = MyApp2()

    # Widget 추가
    widget.addWidget(myApp)
    #widget.addWidget(myApp2)
    widget.show()

    #widget.addWidget(myApp2)   # 언제 show 하든 상관없이 이미 2번째 widget이 생성되어 버려
    #widget.setFixedWidth(400)
    #widget.setFixedHeight(400)
    #widget.resize(600, 400)


    ex = MyApp()
    sys.exit(app.exec_())