import sys  # sys нужен для передачи argv в QApplication
from ui import Ui_Widget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Widget()
ui.setupUi(Form)
Form.show()
eng_ras_nr = "`!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./"
#eng_ras_nr = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
eng_ras_nr = [char for char in eng_ras_nr]
rus_ras_nr = 'ё!"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.'
#rus_ras_nr = "йцукенгшщзхъфывапролджэячсмитьбю."
rus_ras_nr = [char for char in rus_ras_nr]
#Верхний регистр
#eng_ras_vr = [char.upper() for char in eng_ras_nr]
eng_ras_vr = '~!@#$%^&QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?'
#rus_ras_vr = [char.upper() for char in rus_ras_nr]
rus_ras_vr = 'Ё!"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,'
def from_eng_in_rus():
    text = ui.textEdit.toPlainText()
    result = ""
    for i in text:
        if i in eng_ras_nr or i in eng_ras_vr:
            if i in eng_ras_vr:
                result += rus_ras_vr[eng_ras_vr.index(i)]
            else:
                result += rus_ras_nr[eng_ras_nr.index(i)]
        else:
            result += i
    ui.plainTextEdit.setPlainText(result)
def from_rus_in_en():
    text = ui.textEdit.toPlainText()
    result = ""
    for i in text:
        if i in rus_ras_nr or i in rus_ras_vr:
            if i in rus_ras_vr:
                result += eng_ras_vr[rus_ras_vr.index(i)]
            else:
                result += eng_ras_nr[rus_ras_nr.index(i)]
        else:
            result += i
    ui.plainTextEdit.setPlainText(result)
def edit_reg():
    text = ui.textEdit.toPlainText()
    result = ""
    for i in text:
        if i.isupper():
            result += i.lower()
        else:
            result += i.upper()
    ui.plainTextEdit.setPlainText(result)
def queston():
    msg = QMessageBox()
    msg.setWindowTitle("Объяснение")
    msg.setText("Программа 'Переставщик' написана для того, чтобы в случае, если пользователь написал текст, на другой раскладке, то он мог бы без проблем, перевести текст, на нужную для него раскладку.\n Текст, который вы хотите обработать, нужно вводить в поле ввода 'Входные данные'.\n  Обработанный текст появится в поле 'Результат обработки'\n Программа 'Переставщик', может перевести текст с русской раскладки, на английскую, для этого необходимо ввести текст в верхнее поле ввода и нажать на кнопку 'Перевести на английскую раскладку', результат обработки будет в нижем поле ввода.\n Аналогичным способом, можно перевести с английской на русскою раскладку и изменить регистер для всего текста.\n Приятного пользования;)")
    #msg.setIcon(QMessageBox.Question)
    msg.exec_()
ui.pushButton.clicked.connect(from_eng_in_rus)
ui.pushButton_2.clicked.connect(from_rus_in_en)
ui.pushButton_3.clicked.connect(edit_reg)
#ui.pushButton_5.clicked.setText("Over-write")
ui.pushButton_4.clicked.connect(queston)
sys.exit(app.exec_())