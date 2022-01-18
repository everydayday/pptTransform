import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 창 Title, Icon 설정
        self.setWindowTitle('PPT 변환기')
        self.move(300, 300)
        self.setWindowIcon(QIcon("D:\바탕화면\web.png"))
        self.resize(800, 400)

        #self.statusBar().showMessage('Ready')
        # mainWindow = QMainWindow()
        # mainWindow.statusBar().showMessage('Ready')

        # 제목 박스
        # lbl_title = QLabel('PPT 변환기 hello world')
        # lbl_title.setStyleSheet("color: black;"
        #                       "border-style: solid;"
        #                       "border-width: 2px;"
        #                       "font: 10pt'Times New Roman';" # 글자 폰트 설정
        #                       "border-color: #26C5A5;"
        #                       "border-radius: 3px")
        #
        # lbl_title.setAlignment(Qt.AlignCenter) # 가운데 맞춤
        # vbox = QVBoxLayout()
        # vbox.addWidget(lbl_title)
        #
        # self.layout.addwidget(lbl_title)


        # text_input 박스 추가
        # self.echo_le = QLineEdit()
        # self.echo_le.setPlaceholderText('가사를 입력하세요.\n\n\n\n\n\n\n')
        # self.echo_le.setFocus()
        #
        # self.echo_layout = QGridLayout
        # self.echo_layout.addWidget(self.echo_le, 0, 0)
        #
        # self.echo_group.setLayout(self.echo_layout)
        # self.layout.addWidget(self.echo_group, 0, 0)

        '''
        layout = QVBoxLayout()

        text_box = QLineEdit()
        text_box.setPlaceholderText('가사를 입력하세요. \n\n\n\n\n\n')
        text_box.adjustSize()
        #text_box.textChanged[str].connect(self.onChanged)



        layout.addWidget(text_box)

        self.setLayout(layout)
        '''
        '''
        self.lineedit = QLineEdit()
        self.lineedit.move(10,40)
        self.lineedit.resize(300,20)
        self.lineedit.setPlaceholderText('가사를 입력하세요.')
        self.lineedit.setFocus()
        '''

        # 전체 layout 관련 코드 추가
        self.layout = QGridLayout()
        self.echo_group = QGroupBox()


        self.btn_group = QGroupBox()

        self.setLayout(self.layout)

        # QLabel 생성
        self.lbl_title = QLabel('PPT 변환기')
        self.lbl_title.setStyleSheet("color: black;"
                                     "border-style: solid;"
                                     "border-width: 2px;"
                                     "font: 10pt'Times New Roman';"  # 글자 폰트 설정
                                     "border-color: #26C5A5;"
                                     "border-radius: 3px")
        self.lbl_title.setAlignment(Qt.AlignCenter)  # 가운데 맞춤

        # QLineEdit를 생성한다.
        self.echo_le = QLineEdit()
        # QLineEdit의 자리표지자를 지정한다
        self.echo_le.setPlaceholderText('가사를 입력하세요.')
        # QLineEdit에 포커스를 준다.
        self.echo_le.setFocus()

        # btn 추가
        self.btn1 = QPushButton('미리보기')
        self.btn1.resize(200, 100)

        self.btn2 = QPushButton('생성하기')
        self.btn2.resize(200, 100)

        self.btn_layout = QGridLayout()
        self.btn_layout.addWidget(self.btn1, 0, 0)
        self.btn_layout.addWidget(self.btn1, 0, 1)
        self.btn_group.setLayout(self.btn_layout)




        #  echo_layout
        # echo 그리드레이아웃을 생성한다.
        self.echo_layout = QGridLayout()
        # echo 그리드레이아웃에 각 위젯의 위치를 지정한다.
        # 기준
        self.echo_layout.addWidget(self.lbl_title, 0, 0)
        self.echo_layout.addWidget(self.echo_le, 1, 0 )
        self.echo_layout.addWidget(self.btn_group, 2, 0)

        # 위에서 지정한 레이아웃 설정이 echo 묶음에 반영되도록 설정
        self.echo_group.setLayout(self.echo_layout)

        # 전체 창에서의 이 묶음 위쩻의 위치를 지정한다.
        self.layout.addWidget(self.echo_group, 0, 0)

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