import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QDesktopWidget
from PyQt5.QtCore import Qt

class BudgetApp(QWidget):
    def __init__(self, data):
        super().__init__()

        sorted_data = sorted(data.items(), key=lambda x: x[1]['index'])
        last_eight = dict(sorted_data[-8:])
        self.initUI(last_eight)

    def initUI(self, data):
        title_label = QLabel("Klaus Netz und Budget")
        title_label.setStyleSheet("font-size: 30px; font-weight: bold; font-style: italic; color: #4CAF50;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout = QHBoxLayout()
        main_layout.addWidget(title_label)

        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        for i, (person, info) in enumerate(data.items()):
            label_text = f"{info['name']}: {info['budget']}€"
            label = QLabel(label_text)
            label.setStyleSheet("""
                background-color: #4CAF50; 
                color: white; 
                border-radius: 20px; 
                padding: 20px; 
                max-width: 500px;
                margin-bottom: 10px;  
            """)
            label.setAlignment(Qt.AlignCenter)

            if i < 4:
                left_layout.addWidget(label)
            else:
                right_layout.addWidget(label)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)
        self.setWindowTitle('Budget Representation')
        self.center_on_screen()

    def center_on_screen(self):
        screen_geometry = QDesktopWidget().screenGeometry()

        self.setGeometry(
            (screen_geometry.width() - self.width()) // 2,
            (screen_geometry.height() - self.height()) // 2,
            self.width(),
            self.height()
        )

def load_data(file_path):
    with open(file_path) as f:
        data = eval(f.read())
    return data

if __name__ == '__main__':
    app = QApplication(sys.argv)
    file_path = 'user_data.json'
    data = load_data(file_path)
    ex = BudgetApp(data)
    ex.resize(1500, 900)
    ex.show()
    sys.exit(app.exec_())
