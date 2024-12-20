# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer, pyqtSignal
from Configuracion import Ui_Dialog
from Especificaciones import Ui_Especificaciones
from Historial import Ui_Historial
from PyQt6.QtWidgets import QMainWindow

class Ui_Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1024, 600))
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(240, 20, 581, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(300, 480, 451, 71))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.widget1 = QtWidgets.QWidget(parent=Form)
        self.widget1.setGeometry(QtCore.QRect(120, 160, 801, 291))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(parent=self.widget1)
        self.splitter.setStyleSheet("#background-color: rgb(255, 255, 255)")
        self.splitter.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_8 = QtWidgets.QLabel(parent=self.splitter)
        self.label_8.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.widget2 = QtWidgets.QWidget(parent=self.splitter)
        self.widget2.setObjectName("widget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(parent=self.widget2)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(parent=self.widget2)
        self.label_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.widget2)
        self.label_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.widget2)
        self.label_9.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 4, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.widget2)
        self.label_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.widget2)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.splitter)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.widget1)
        self.pushButton_7.setMinimumSize(QtCore.QSize(151, 61))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.irConfiguracion)
        self.verticalLayout_2.addWidget(self.pushButton_7)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QtCore.QSize(151, 61))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.irEspecificaciones)
        self.verticalLayout_2.addWidget(self.pushButton_8)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget1)
        self.pushButton_5.setMinimumSize(QtCore.QSize(151, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.irHistorial)
        self.verticalLayout.addWidget(self.pushButton_5)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(151, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Main"))
        self.label.setText(_translate("Form", "Sistema de Empaquetado de Semillas"))
        self.pushButton.setText(_translate("Form", "Encendido"))
        self.pushButton_2.setText(_translate("Form", "Apagado"))
        self.label_8.setText(_translate("Form", "Información General"))
        self.label_11.setText(_translate("Form", "Tipo de semilla:"))
        self.label_14.setText(_translate("Form", "Apagado"))
        self.label_13.setText(_translate("Form", "Especifique el tipo de semilla"))
        self.label_9.setText(_translate("Form", "Estado actual:"))
        self.label_12.setText(_translate("Form", "Especifique el peso"))
        self.label_10.setText(_translate("Form", "Peso por paquete:"))
        self.pushButton_7.setText(_translate("Form", "Editar configuración"))
        self.pushButton_8.setText(_translate("Form", "Editar especificaciones"))
        self.pushButton_5.setText(_translate("Form", "Historial"))
        self.pushButton_6.setText(_translate("Form", "Al momento"))


    def irConfiguracion(self):
        # Crear y mostrar la segunda ventana
        print("Botón presionado, abriendo la ventana secundaria...")
        self.configuracion_ventana = QtWidgets.QDialog()  # Crear un QWidget para la segunda ventana
        ui = Ui_Dialog()  # Crear una instancia de la clase Ui_Form
        ui.setupUi(self.configuracion_ventana)  # Configurar la UI de la segunda ventana
        self.configuracion_ventana.show()  # Mostrar la segunda ventana
        self.configuracion_ventana.raise_()  # Asegura que la ventana esté al frente
        #QTimer.singleShot(100, Ui_Main.close)  # Esperar un poco antes de cerrar la ventana
        #QTimer.singleShot(100, self.close)

    def irEspecificaciones(self):
        # Crear y mostrar la segunda ventana
        print("Botón presionado, abriendo la ventana secundaria...")
        self.ventana_especificaciones = QtWidgets.QDialog()  # Crear un QWidget para la segunda ventana
        ui = Ui_Especificaciones()  # Crear una instancia de la clase Ui_Form
        ui.setupUi(self.ventana_especificaciones)  # Configurar la UI de la segunda ventana
        self.ventana_especificaciones.show()  # Mostrar la segunda ventana
        self.ventana_especificaciones.raise_()  # Asegura que la ventana esté al frente

    def irHistorial(self):
        # Crear y mostrar la segunda ventana
        print("Botón presionado, abriendo la ventana secundaria...")
        self.ventana_historial = QtWidgets.QDialog()  # Crear un QWidget para la segunda ventana
        ui = Ui_Historial()  # Crear una instancia de la clase Ui_Form
        ui.setupUi(self.ventana_historial)  # Configurar la UI de la segunda ventana
        self.ventana_historial.show()  # Mostrar la segunda ventana
        self.ventana_historial.raise_()  # Asegura que la ventana esté al frente

"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)  # Crear la aplicación Qt
    Main = QtWidgets.QDialog()  # Crear una instancia del QDialog
    ui = Ui_Main()  # Crear la interfaz de usuario
    ui.setupUi(Main)  # Configurar la interfaz en el dialog
    Main.exec()  # Ejecutar el diálogo"""

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)  # Crear la aplicación Qt
    Main = QtWidgets.QDialog()  # Crear una instancia del QDialog
    ui = Ui_Main()  # Crear la interfaz de usuario
    ui.setupUi(Main)  # Configurar la interfaz en el dialog
    Main.show()  # Asegurarse de mostrar la ventana principal
    sys.exit(app.exec())  # Ejecutar la aplicación

if __name__ == "__main__":
    main()
