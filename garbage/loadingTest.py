import sys
from PyQt5.QtCore import Qt, QByteArray, QSettings, QTimer, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QSizePolicy, QVBoxLayout, QAction, QPushButton
from PyQt5.QtGui import QMovie


gifFile = "ColossalMeekCygnet-mobile.mp4"
class GifPlayer(QWidget):
    def __init__(self, title, gifFile, parent=None):
        QWidget.__init__(self, parent)

        self.movie = QMovie(gifFile, QByteArray(), self)
        size = self.movie.scaledSize()
        self.setGeometry(200, 200, size.width(), size.height())
        self.setWindowTitle(title)
        self.movie_screen = QLabel()
        self.movie_screen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.movie_screen.setAlignment(Qt.AlignCenter)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.movie_screen)
        self.setLayout(main_layout)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie_screen.setMovie(self.movie)
        self.movie.start()
        self.movie.loopCount()

        button = QPushButton('refresh gif', self)
        button.setToolTip('This is an example button')
        button.move(10,10)
        button.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        self.movie = QMovie(gifFile,QByteArray(), self)
        self.movie_screen.setMovie(self.movie)
        self.movie.start()
        print("done")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = GifPlayer("update this gif", gifFile)
    player.show()
sys.exit(app.exec_())