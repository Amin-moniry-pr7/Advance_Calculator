from modules.calculator_logic import CalculatorLogic
from modules.ui_elements import CalculatorUI
from modules.history import HistoryManager
from PyQt6.QtWidgets import QApplication
from modules.themes import Themes
from modules.about import About
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = CalculatorUI()
    logic = CalculatorLogic(ui)
    themes = Themes(ui)
    history = HistoryManager(ui, logic)
    about = About(ui)

    for button in ui.buttons_list:
        button.clicked.connect(logic.on_button_clicked)
        button.pressed.connect(lambda btn=button: themes.on_button_pressed(btn))
        button.released.connect(lambda btn=button: themes.on_button_released(btn))

    ui.history_button.clicked.connect(history.show_history)
    ui.theme_folder.currentTextChanged.connect(themes.change_theme)
    ui.about_button.clicked.connect(about.show_about)

    ui.keyPressEvent = logic.keyPressEvent

    themes.change_theme("Default")
    ui.show()
    sys.exit(app.exec())