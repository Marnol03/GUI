import sys
import random
from datetime import date

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi
import pyperclip
import csv
class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
        if (email == "" or password==""):
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(f"geben sie echte dfaten ein")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.email.setText("")
            self.password.setText("")
        #TODO Prufe in Databank ob die Email und password exsistieren
        print("Successfully logged in with email: ", email, "and password:", password)
        isempty = True
        if (isempty):
            datum = date.today()
            with open("./beispiel.txt", 'w') as file:
                file.write(f"{password} | {email} | {datum}")



    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotLogin)
        self.passwordGanrator.clicked.connect(self.generate_password)

    def createaccfunction(self):
        email = self.email.text()
        prufen = False # TODO soll email geprüft ob das in Databank /excel exsisert
        if (prufen or email==""):
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(f"andern sie diese Email ")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.email.setText("")

        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            print("Successfully created acc with email: ", email, "and password: ", password)
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(f"Das Passworde sind nicht edintich")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()
            self.password.setText("")
            self.confirmpass.setText("")
    def gotLogin(self):
        Loginacc = Login()
        widget.addWidget(Loginacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def generate_password(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '@', '%', '&', '(', ')', '*', '+']
        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_list = []

        for _ in range(nr_letters):
            password_list.append(random.choice(letters))

        for _ in range(nr_symbols):
            password_list += random.choice(symbols)

        for _ in range(nr_numbers):
            password_list += random.choice(numbers)

        random.shuffle(password_list)

        password = "".join(password_list)
        print(password)
        # Set the generated password in the fields
        self.password.setText(password)
        self.confirmpass.setText(password)

        # Zeige das Passwort in einer MessageBox an
        msg = QMessageBox()
        msg.setWindowTitle("Generated Password")
        msg.setText(f"The generated password is: {password} \n The password is in the clipPort")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        pyperclip.copy(password)

app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()


# def check_password(self, e):
#     pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&\(\)])[A-Za-z\d@\(\)$!%*?&+**,&%#*!#@]{8,}$"
#     password = self.password_entry.get()
#     str_commit = tk.StringVar()
#     error_Label = tk.Label(self.div, textvariable=str_commit)
#     if re.match(pattern, password):
#         if password == self.password_entry_2.get():
#             self.fP = True
#         else:
#             # messagebox.showinfo(
#             # message="The entered passwords do not match. Please check your input or use our Password Generator.")
#             str_commit.set(
#                 f"The entered passwords do not match. Please check \n your input or use our Password Generator.")
#             error_Label.grid(row=6, column=1, sticky="we")
#             error_Label.config(foreground="red")
#             self.div.after(2000, error_Label.destroy)
#     else:
#         messagebox.showinfo(
#             message="Password requirements:\n- Minimum length of 8 characters\n- At least one lowercase letter\n- At least one uppercase letter\n- At least one digit\n- At least one special character")