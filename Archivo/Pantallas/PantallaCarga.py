from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer, pyqtSignal
from Main import Ui_Main
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 600))
        MainWindow.setStyleSheet("background-color: rgb(236, 236, 236)")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 110, 391, 361))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/Users/Chuch0/Desktop/Entornos/Empaquetadora/Imagenes/Máquina.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 20, 601, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(80)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(380, 490, 291, 61))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Temporizador para actualizar la barra de progreso
        self.timer = QtCore.QTimer(MainWindow)
        self.timer.timeout.connect(self.updateProgressBar)
        #self.timer.start(100)  # Actualizar cada 100 ms
        self.timer.start(10)
        self.current_value = 0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PantallaCarga"))
        self.label_2.setText(_translate("MainWindow", "Empaquetadora"))

    def updateProgressBar(self):
        self.current_value += 1
        self.progressBar.setValue(self.current_value)

        # Cuando la barra llegue a 100, detener el temporizador y abrir la siguiente ventana
        if self.current_value >= 100:
            self.timer.stop()
            self.goToSecondWindow()

    def goToSecondWindow(self):
        # Crear y mostrar la segunda ventana
        """self.second_window = QtWidgets.QDialog()  # Crear un QWidget para la segunda ventana
        ui = Ui_Main()  # Crear una instancia de la clase Ui_Form
        ui.setupUi(self.second_window)  # Configurar la UI de la segunda ventana
        self.second_window.show()  # Mostrar la segunda ventana
        self.second_window.raise_()  # Asegura que la ventana esté al frente
        QtCore.QTimer.singleShot(100, MainWindow.close)  # Esperar un poco antes de cerrar la ventana"""
        self.second_window = Ui_Main()
        self.second_window.show()  # Mostrar la segunda ventana
        self.second_window.raise_()  # Asegura que la ventana esté al frente
        QtCore.QTimer.singleShot(100, MainWindow.close)  # Esperar un poco antes de cerrar la ventana


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Crear la aplicación Qt
    MainWindow = QtWidgets.QMainWindow()  # Crear una instancia del QMainWindow
    ui = Ui_MainWindow()  # Crear la interfaz de usuario
    ui.setupUi(MainWindow)  # Configurar la interfaz en el MainWindow
    MainWindow.show()  # Mostrar el MainWindow
    sys.exit(app.exec())  # Ejecutar la aplicación y salir cuando se cierre