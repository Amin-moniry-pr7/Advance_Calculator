from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QGridLayout, QPushButton, QWidget, QVBoxLayout, QComboBox
from PyQt6.QtCore import Qt


class CalculatorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Amin_Calculator")
        self.setFixedSize(600, 380)
        self.setWindowIcon(QIcon('LOGO.ico'))

        self.display = QLineEdit(self)
        self.display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display.setReadOnly(False)
        self.display.setFixedHeight(50)
        self.display.setPlaceholderText("Please, type your text")
        self.display.mousePressEvent = self.clear_placeholder

        self.current_theme = "Default"
        self.create_buttons()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)
        main_layout.addLayout(self.grid_layout)

        container = QWidget(self)
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.history_button = QPushButton("History", self)
        self.history_button.setFixedSize(200, 20)

        self.theme_folder = QComboBox(self)
        self.theme_folder.addItems(["Default", "Forest Green", "Midnight Blue", "Rose Pink", "Amber Glow", "Slate Gray"])
        self.theme_folder.setFixedSize(120, 20)
        self.theme_folder.setCurrentText("Default")

        self.about_button = QPushButton("About", self)
        self.about_button.setFixedSize(120, 20)

    def create_buttons(self):
        buttons = {
            '+': (0, 0), '=': (0, 1), '7': (0, 2), '8': (0, 3), '9': (0, 4), 'C': (0, 5), '⌧': (0, 6),
            '-': (1, 0), '*': (1, 1), '4': (1, 2), '5': (1, 3), '6': (1, 4), 'sin': (1, 5), 'cos': (1, 6),
            '^': (2, 0), '/': (2, 1), '1': (2, 2), '2': (2, 3), '3': (2, 4), '√': (2, 5), 'frac': (2, 6),
            '(': (3, 0), ')': (3, 1), '0': (3, 2), '.': (3, 3), '00': (3, 4), 'tan': (3, 5), 'cot': (3, 6),
        }

        self.grid_layout = QGridLayout()
        self.buttons_list = []

        for text, pos in buttons.items():
            button = QPushButton(text if text != 'frac' else '½')
            button.setFixedSize(60, 60)
            self.buttons_list.append(button)
            self.grid_layout.addWidget(button, pos[0], pos[1])

    def clear_placeholder(self, event):
        if not self.display.text():
            self.display.setText("")
            self.display.setPlaceholderText("Please, type your text")

    def resizeEvent(self, event):

        self.history_button.setGeometry(
            (self.width() - self.history_button.width()) // 2,
            self.height() - self.history_button.height(),
            200, 20
        )
        self.theme_folder.setGeometry(
            self.width() - self.theme_folder.width(),
            self.height() - self.theme_folder.height(),
            120, 20
        )
        self.about_button.setGeometry(
            0,
            self.height() - self.about_button.height(),
            120, 20
        )