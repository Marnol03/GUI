import sys
import json
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QDialog, QLabel, QLineEdit, QFormLayout, \
    QMessageBox, QInputDialog, QHBoxLayout,QMainWindow
from kaeufer_Ui.klaus2 import Ui_Widget
from Klaus_Ui.klaus import klausp
from PyQt5 import QtWidgets, QtCore


class User:
    password_changed = False

    def __init__(self, name, budget, password, index):
        self.name = name
        self.budget = budget
        self.password = password
        self.index = index
        self.password_changed_count = 0

    def reset_password_changed_count(self):
        self.password_changed_count = 0

    def update_password(self, new_password):
        self.password = new_password
        self.save_to_passwords_file()
        User.password_changed = True

    def save_to_passwords_file(self):
        with open('passwords.txt', 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            user_info = line.strip().split(',')
            if user_info[0] == self.name:
                lines[i] = f"{self.name},{self.budget},{self.password},{self.index}\n"
                break

        with open('passwords.txt', 'w') as file:
            file.writelines(lines)

    def reset_password_changed_flag(self):
        User.password_changed = False

    def to_dict(self):
        return {
            "name": self.name,
            "budget": self.budget,
            "index": self.index
        }

    def check_password(self, entered_password):
        return self.password == entered_password


class RegisterDialog(QDialog):
    def __init__(self, parent=None):
        super(RegisterDialog, self).__init__(parent)
        self.setWindowTitle("Registrieren")
        self.setFixedSize(600, 400)
        self.setStyleSheet("QWidget{\n"
                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(0, 160, 136, 255), stop:1 rgba(0,0,0, 255));\n"
                           "    border-radius:20px;\n"
                           "\n"
                           "}\n")

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        form_layout = QFormLayout()

        self.name_label = QLabel("Name:")
        self.name_label.setStyleSheet("color: white; background-color: none; font-size: 24px;")
        self.name_edit = QLineEdit()
        self.name_edit.setStyleSheet(
            "border: 2px solid #006600; border-radius: 5px; padding: 5px; margin: 5px; background-color: white;")
        form_layout.addRow(self.name_label, self.name_edit)

        self.budget_label = QLabel("Budget:")
        self.budget_label.setStyleSheet("color: white; background-color: none; font-size: 24px;")
        self.budget_edit = QLineEdit()
        self.budget_edit.setStyleSheet(
            "border: 2px solid #006600; border-radius: 5px; padding: 5px; margin: 5px; background-color: white;")
        form_layout.addRow(self.budget_label, self.budget_edit)

        self.password_label = QLabel("Password:")
        self.password_label.setStyleSheet("color: white; background-color: none; font-size: 24px;")
        self.password_edit = QLineEdit()
        self.password_edit.setStyleSheet(
            "border: 2px solid #006600; border-radius: 5px; padding: 5px; margin: 5px; background-color: white;")
        self.password_edit.setEchoMode(QLineEdit.Password)
        form_layout.addRow(self.password_label, self.password_edit)

        register_button = QPushButton("Registrieren")
        register_button.setStyleSheet(
            "border: 2px solid #006600; border-radius: 5px;padding:5px;background-color: white;width: 100px")
        register_button.clicked.connect(self.register)
        form_layout.addRow(register_button)

        layout.addLayout(form_layout)

    def register(self):
        try:
            name = self.name_edit.text()
            budget = int(self.budget_edit.text())
            password = self.password_edit.text()

            self.parent().register_user(name, budget, password)
            self.accept()
        except Exception as e:
            print(f"An error occurred during registration: {e}")


class LoginDialog(QDialog):
    def __init__(self, users, users_to_reset_password, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.setWindowTitle("Login")
        self.setFixedSize(600, 400)
        self.setStyleSheet("QWidget{\n"
                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(0, 160, 136, 255), stop:1 rgba(0,0,0, 255));\n"
                           "    border-radius:20px;\n"
                           "\n"
                           "}\n")

        self.users = users
        self.users_to_reset_password = users_to_reset_password
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        form_layout = QFormLayout()

        label1 = QLabel("Login")
        label1.setAlignment(Qt.AlignCenter)
        label1.setFont(QFont('Arial', 14, weight=QFont.Bold))
        label1.setStyleSheet("font-weight: bold; font-size: 30px;color:white;")
        layout.addWidget(label1)

        self.name_label = QLabel("Name:")
        self.name_label.setStyleSheet("color: white; background-color: none; font-size: 24px;")
        self.name_edit = QLineEdit()
        self.name_edit.setStyleSheet(
            "border: 2px solid #006600;margin: 5px; background-color: white;height: 24px;width:200px")
        form_layout.addRow(self.name_label, self.name_edit)

        self.password_label = QLabel("Password:")
        self.password_label.setStyleSheet("color: white; background-color: none; font-size: 24px;")
        self.password_edit = QLineEdit()
        self.password_edit.setStyleSheet(
            "border: 2px solid #006600;margin: 5px; background-color: white;height: 24px;width:200px")
        self.password_edit.setEchoMode(QLineEdit.Password)
        form_layout.addRow(self.password_label, self.password_edit)

        login_button = QPushButton("Einloggen")
        login_button.setStyleSheet("border: 2px solid #006600; border-radius: 5px;padding:5px;background-color: white;width: 100px")
        login_button.clicked.connect(self.login)
        form_layout.addRow(login_button)
        layout.addLayout(form_layout)

    def login(self):
        name = self.name_edit.text()
        entered_password = self.password_edit.text()

        user_match = next((user for user in self.users if user.name == name), None)

        if user_match and user_match.check_password(entered_password):
            if user_match.password_changed_count == 0:
                new_password, ok = QInputDialog.getText(self, "Neues Passwort",
                                                        "Bitte geben Sie Ihr neues Passwort ein:",
                                                        QLineEdit.Password)
                if ok:

                    user_match.password = new_password
                    user_match.update_password(new_password)
                    user_match.password_changed_count += 1
                    self.parent().login_user(name)


            else:
                user_match.reset_password_changed_count()
                self.parent().login_user(name)
            if name == "klaus":
                self.show_page1()
            else:
                with open('user_data.json', 'r') as json_file:
                    user_data = json.load(json_file)
                with open('user_track.json', 'r') as json_file:
                    user_track = json.load(json_file)
                self.show_page(name,user_data,user_track)
        else:
            QMessageBox.warning(self, 'Falsches Passwort', 'Falsches Passwort. Versuchen Sie es erneut.')

    def show_page(self,name,user_data,user_track):
        self.interface2 = QtWidgets.QWidget()
        ui2 = Ui_Widget()
        ui2.setupUi(self.interface2,name,user_data,user_track)
        self.interface2.setWindowModality(QtCore.Qt.ApplicationModal)

        self.interface2.show()
    def show_page1(self):
        self.interface3 = QtWidgets.QWidget()
        ui2 = klausp()
        ui2.setupUi(self.interface3)

        # Rendre la deuxième interface modale
        self.interface3.setWindowModality(QtCore.Qt.ApplicationModal)

        self.interface3.show()

class BudgetApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 400)
        self.users = []
        self.load_users_from_file("passwords.txt")
        self.load_users_from_file("user_data.json")
        self.init_ui()
        self.current_index = 0

    def init_ui(self):
        self.setWindowTitle('Budget App')
        self.setStyleSheet("QWidget{\n"
    "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(0, 160, 136, 255), stop:1 rgba(0,0,0, 255));\n"
    "    border-radius:20px;\n"
    "\n"
    "}\n")

        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)

        vertical_layout = QVBoxLayout()

        buttons_layout = QHBoxLayout()

        label1 = QLabel("Willkommen zu Traktorenshop")
        label1.setAlignment(Qt.AlignCenter)
        label1.setFont(QFont('Arial', 14, weight=QFont.Bold))
        label1.setStyleSheet("font-weight: bold; font-size: 26px;color:white;")
        vertical_layout.addWidget(label1)

        pixmap = QPixmap("Traktoren/Claas_95E.jpg")
        image_label = QLabel()
        image_label.setPixmap(pixmap.scaledToWidth(300))
        image_label.setAlignment(Qt.AlignCenter)
        vertical_layout.addWidget(image_label)

        label = QLabel("Froh Sie zu sehen!\nWollen Sie sich einloggen oder registrieren?\nWählen Sie aus")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont('Arial', 14, weight=QFont.Bold))
        label.setStyleSheet("font-style: italic;color:white;")
        vertical_layout.addWidget(label)

        register_button = QPushButton("Registrieren")
        register_button.setStyleSheet("border: 2px solid #006600; padding: 5px; margin: 5px;color:white;")
        register_button.clicked.connect(self.show_register_dialog)
        buttons_layout.addWidget(register_button)

        login_button = QPushButton("Login")
        login_button.setStyleSheet("border: 2px solid #006600; padding: 5px; margin: 5px;color:white;")
        login_button.clicked.connect(self.show_login_dialog)
        buttons_layout.addWidget(login_button)

        vertical_layout.addLayout(buttons_layout)

        main_layout.addLayout(vertical_layout)

    def show_register_dialog(self):
        register_dialog = RegisterDialog(self)
        result = register_dialog.exec_()
        if result == QDialog.Accepted:
            pass

    def show_login_dialog(self):
        users_to_reset_password = ['Oskar', 'Benni', 'Daniela', 'Horst', 'Sieglinde']
        login_dialog = LoginDialog(self.users, users_to_reset_password, self)
        result = login_dialog.exec_()
        if result == QDialog.Accepted:
            pass

    def load_users_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    if not line.strip():
                        continue

                    if line.count(',') >= 3:
                        name, budget_with_currency, password, index = line.strip().split(',')

                        budget_str = ''.join(filter(str.isdigit, budget_with_currency))
                        budget = int(budget_str)
                        index = int(index)

                        self.users.append(User(name, budget, password, index))
                    else:
                        print(f"Fehler in{filename} - {line}")
        except FileNotFoundError:
            print(f"Die Datei {filename} ist nicht gefunden")
        except ValueError as e:
            print(f"Fehler in {filename}: {e}")

    def login_user(self, name):
        self.save_user_info(name, 'name_user.json')

    def save_user_info(self, name, filename):
        user_info = {"name": name}
        with open(filename, 'w') as json_file:
           json.dump(user_info, json_file, indent=2)

    def save_user_to_json(self, user):
        try:
            with open('user_data.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {}

        data[user.name] = user.to_dict()

        with open('user_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)

    def register_user(self, name, budget, password):
        user = User(name, budget, "", self.current_index)
        self.users.append(user)

        with open("passwords.txt", "a") as passwords_file:
            passwords_file.write(f"{name},{budget},{password},{self.current_index}\n")
        user.update_password(password)

        try:
            with open("user_data.json", "r") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {}

        data[name] = {
            "name": name,
            "budget": budget,
            "index": self.current_index
        }

        with open("user_data.json", "w") as json_file:
            json.dump(data, json_file, indent=2)

        try:
            with open("user_track.json", "r") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {}

        data[name] = []

        with open("user_track.json", "w") as json_file:
            json.dump(data, json_file, indent=2)

        with open("passwords.txt", "a") as passwords_file:
            passwords_file.write(f"{name},{budget},{password},{self.current_index}\n")

        self.save_user_to_json(user)
        self.current_index += 1


if __name__ == '__main__':
    app = QApplication([])
    window = BudgetApp()
    window.resize(800, 600)
    window.show()
    app.exec_()
