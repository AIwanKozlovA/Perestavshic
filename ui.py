# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(781, 625)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("perestavshic.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Widget.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(20, 50, 161, 51))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 281, 41))
        self.pushButton.setObjectName("pushButton")
        self.checkBox_2 = QtWidgets.QCheckBox(Widget)
        self.checkBox_2.setGeometry(QtCore.QRect(610, 110, 92, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 10, 281, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Widget)
        self.textEdit.setGeometry(QtCore.QRect(10, 110, 761, 191))
        self.textEdit.setObjectName("textEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Widget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 360, 761, 221))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(20, 320, 261, 17))
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Widget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 10, 171, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Widget)
        self.pushButton_4.setGeometry(QtCore.QRect(720, 590, 51, 25))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Переставщик"))
        self.label.setText(_translate("Widget", "Входные данные"))
        self.pushButton.setText(_translate("Widget", "Преобразовать на русскую раскладку"))
        self.checkBox_2.setText(_translate("Widget", "CheckBox"))
        self.pushButton_2.setText(_translate("Widget", "Перевести на английскую раскладку"))
        self.label_2.setText(_translate("Widget", "Результат обработки"))
        self.pushButton_3.setText(_translate("Widget", "Изменить регистер"))
        self.pushButton_4.setText(_translate("Widget", "?"))
