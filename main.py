import sys  # sys нужен для передачи argv в QApplication
from ui import Ui_Widget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import webbrowser
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
def inversion():
    text = ui.textEdit.toPlainText()
    result = ""
    for i in text:
        if i in rus_ras_vr:
            result += eng_ras_vr[rus_ras_vr.index(i)]
        elif i in eng_ras_vr:
            result += rus_ras_vr[eng_ras_vr.index(i)]
        elif i in rus_ras_nr:
            result += eng_ras_nr[rus_ras_nr.index(i)]
        elif i in eng_ras_nr:
            result += rus_ras_nr[eng_ras_nr.index(i)]
        else:
            result += i
    ui.plainTextEdit.setPlainText(result)
def inversion_CL():
    text = ui.textEdit.toPlainText()
    result = ""
    for i in text:
        if i in rus_ras_vr:
            result += eng_ras_nr[rus_ras_vr.index(i)]
        elif i in eng_ras_vr:
            result += rus_ras_nr[eng_ras_vr.index(i)]
        elif i in rus_ras_nr:
            result += eng_ras_vr[rus_ras_nr.index(i)]
        elif i in eng_ras_nr:
            result += rus_ras_vr[eng_ras_nr.index(i)]
        else:
            result += i
    ui.plainTextEdit.setPlainText(result)
def cv():
    webbrowser.open_new_tab("https://vk.com/ivan___kozlov")
def queston():
    msg = QMessageBox()
    msg.setWindowTitle("Объяснение")
    msg.setText("Программа 'Переставщик' написана для того, чтобы в случае, если пользователь написал текст, на другой раскладке, то он мог без проблем, перевести текст, на нужную для него раскладку.\n Текст, который вы хотите обработать, нужно вводить в поле ввода 'Входные данные'.\n  Обработанный текст появится в поле 'Результат обработки'\n Программа 'Переставщик', может перевести текст с русской раскладки, на английскую, для этого необходимо ввести текст в верхнее поле ввода и нажать на кнопку 'Перевести на английскую раскладку', результат обработки будет в нижем поле ввода.\n Аналогичным способом, можно перевести с английской на русскою раскладку и изменить регистер для всего текста.\n Если вы, то что должны были написать на русской раскладке, написали на аглийской и, то что должы были написать на английской раскладке написали на русской раскладке, и из-за этого образовалась полная мешанина, то её можно преобразовать в нормальный текст, скопировав текст в поле ввода 'Входные данные' и нажав на кнопку 'Инверсия'. Если вы ещё помимо раскладки перепутали регистер, то нажмите кнопку 'Инверсия с Caps Lock'\nПриятного пользования;)")
    #msg.setIcon(QMessageBox.Question)
    msg.exec_()
ui.pushButton.clicked.connect(from_eng_in_rus)
ui.pushButton_2.clicked.connect(from_rus_in_en)
ui.pushButton_3.clicked.connect(edit_reg)
#ui.pushButton_5.clicked.setText("Over-write")
ui.pushButton_4.clicked.connect(queston)
ui.pushButton_5.clicked.connect(inversion)
ui.pushButton_6.clicked.connect(inversion_CL)
ui.pushButton_7.clicked.connect(cv)
sys.exit(app.exec_())
