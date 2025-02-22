from PyQt6.QtWidgets import QMessageBox


class About:
    def __init__(self, ui):
        self.ui = ui

    def show_about(self):
        QMessageBox.information(self.ui, "About Calculator",
                                "\n\nCreator: Amin Moniry\n"
                                "Location: Iran, Tabriz\n"
                                "Date: 22-2-2025\n\n"
                                "GitHub: https://github.com/Amin-moniry-pr7\n"
                                "Contact: aminmoniry199@gmail.com\n"
                                "Technology: PyQt6, Python 3.12.4\n"
                                "Version: 1.0.0\n")