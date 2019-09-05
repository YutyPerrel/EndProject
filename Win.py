# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Win.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WinDialog(object):
    def setupUi(self, WinDialog):
        WinDialog.setObjectName("Dialog")
        WinDialog.resize(310, 203)
        self.pushButton = QtWidgets.QPushButton(WinDialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(WinDialog)
        self.label.setGeometry(QtCore.QRect(50, 60, 201, 41))
        self.label.setObjectName("label")

        self.retranslateUi(WinDialog)
        QtCore.QMetaObject.connectSlotsByName(WinDialog)

    def retranslateUi(self, WinDialog):
        _translate = QtCore.QCoreApplication.translate
        WinDialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.label.setText(_translate("Dialog", "Win"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WinDialog = QtWidgets.QDialog()
    ui = Ui_WinDialog()
    ui.setupUi(WinDialog)
    WinDialog.show()
    sys.exit(app.exec_())
