# Form implementation generated from reading ui file '.\view\Dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import sys


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):

        super().__init__()

        self.setObjectName("Dialog")
        self.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(parent=self)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.accept)  # type: ignore
        self.buttonBox.rejected.connect(self.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Hecho por:"))
        self.label_2.setText(_translate("Dialog", "Made by:"))
        self.label_3.setText(_translate(
            "Dialog", "ALAN DIDIER CHAVEZ PANIAGUA"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = Ui_Dialog()
    dialog.show()
    sys.exit(app.exec())
