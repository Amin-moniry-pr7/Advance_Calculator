from PyQt6.QtGui import QColor


class Themes:
    def __init__(self, ui):
        self.ui = ui

    def get_themes(self):
        return {
            "Default": ("#000036", "#100c08", "#FFFFFF", 60, 60, 30),
            "Forest Green": ("#1B5E20", "#2E7D32", "#FFFFFF", 70, 50, 15),
            "Midnight Blue": ("#0D47A1", "#1976D2", "#E0E0E0", 65, 65, 5),
            "Rose Pink": ("#ff33cc", "#fba0e3 ", "#FFFFFF", 80, 40, 20),
            "Amber Glow": ("#E65100", "#FF8F00", "#212121", 80, 60, 10),
            "Slate Gray": ("#37474F", "#546E7A", "#ECEFF1", 75, 55, 25)
        }

    def on_button_pressed(self, button):
        themes = self.get_themes()
        default_bg, operator_bg, text_color, width, height, radius = themes[self.ui.current_theme]
        pressed_style = f"background-color: {QColor(operator_bg).lighter(150).name()}; color: {text_color}; font-size: 18px; border-radius: {radius}px;"
        button.setStyleSheet(pressed_style)

    def on_button_released(self, button):
        themes = self.get_themes()
        default_bg, operator_bg, text_color, width, height, radius = themes[self.ui.current_theme]
        if button.text() in ('+', '-', '*', '/', '^', '√', 'sin', 'cos', 'tan', 'cot', ')', '(', 'C', '=', '⌧', '½'):
            button.setStyleSheet(
                f"background-color: {operator_bg}; color: {text_color}; font-size: 18px; border-radius: {radius}px;")
        else:
            button.setStyleSheet(
                f"background-color: {default_bg}; color: {text_color}; font-size: 18px; border-radius: {radius}px;")

    def change_theme(self, theme):
        self.ui.current_theme = theme
        themes = self.get_themes()
        default_bg, operator_bg, text_color, width, height, radius = themes[theme]
        for button in self.ui.buttons_list:
            button.setFixedSize(width, height)
            if button.text() in (
            '+', '-', '*', '/', '^', '√', 'sin', 'cos', 'tan', 'cot', ')', '(', 'C', '=', '⌧', '½'):
                button.setStyleSheet(
                    f"background-color: {operator_bg}; color: {text_color}; font-size: 18px; border-radius: {radius}px;")
            else:
                button.setStyleSheet(
                    f"background-color: {default_bg}; color: {text_color}; font-size: 18px; border-radius: {radius}px;")

        self.ui.history_button.setStyleSheet(
            f"background-color: #086623; color: white; font-size: 18px; border-radius: 10px;")
        self.ui.theme_folder.setStyleSheet(
            f"background-color: #086623; color: white; font-size: 18px; border-radius: 5px;")
        self.ui.about_button.setStyleSheet(
            f"background-color: #086623; color: white; font-size: 18px; border-radius: 5px;")