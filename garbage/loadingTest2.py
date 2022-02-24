# refer to...
# https://stackoverflow.com/questions/52884600/python-error-can-not-show-gif-in-a-qlabel
import threading
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from FirebaseLogin import db
from contraInicio import ContraInicioC


class LoginC(QtWidgets.QMainWindow):
    firebaseFinished = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        super(LoginC, self).__init__(parent)
        uic.loadUi("Interfaz/Login.ui",self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.l_permiso.setAttribute(QtCore.Qt.WA_NoMousePropagation)
        self.l_sucursal.setAttribute(QtCore.Qt.WA_NoMousePropagation)
        self.l_close.clicked.connect(self.close)
        self.contraseña = ContraInicioC()
        self.l_entrar.clicked.connect(self.setDataPrincipal)
        self.l_permiso.currentIndexChanged.connect(self.cambioPermiso)
        self.l_permiso.setCurrentText("Caja")
        self.l_sucursal.setCurrentText("Exxe 1")
        self.firebaseFinished.connect(self.on_firebaseFinished)

    @QtCore.pyqtSlot()
    def cambioPermiso(self):
        self.l_sucursal.setEnabled(self.l_permiso.currentText() == "Administrador")

    def setDataPrincipal(self):
        movi = QtGui.QMovie("480px-Loader.gif")
        self.label.setMovie(movi)
        movi.start()
        fechaActual = QtCore.QDate.currentDate().toPyDate()
        path = "/{}".format(fechaActual)
        threading.Thread(target=self.get_data, args=(path,), daemon=True).start()

    def get_data(self, path):
        ref = db.reference(path)
        ret = ref.get()
        self.firebaseFinished.emit(ret)

    def on_firebaseFinished(self, ret):
        print("result", ret)
        self.contraseña.show()
        self.close()

    def mousePressEvent(self,event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self,event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    l = LoginC()
    l.show()
    sys.exit(app.exec_())