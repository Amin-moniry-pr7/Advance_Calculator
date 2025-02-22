from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QPushButton, QTableWidgetItem, QMessageBox
from PyQt6.QtCore import Qt


class HistoryManager:
    def __init__(self, ui, logic):
        self.ui = ui
        self.logic = logic

    def show_history(self):
        dialog = QDialog(self.ui)
        dialog.setWindowTitle("History")
        dialog.setFixedSize(400, 300)
        layout = QVBoxLayout()

        table = QTableWidget()
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["#", "Calculation", "Creator", "Time"])
        table.setStyleSheet("background-color: #2E2E4E; color: white;")
        table.horizontalHeader().setStyleSheet("background-color: #3A3A5C; color: #FFD700;")
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        if self.logic.history:
            table.setRowCount(len(self.logic.history))
            for i, entry in enumerate(self.logic.history):
                table.setItem(i, 0, QTableWidgetItem(str(i + 1)))
                table.setItem(i, 1, QTableWidgetItem(entry["calculation"]))
                table.setItem(i, 2, QTableWidgetItem(entry["creator"]))
                table.setItem(i, 3, QTableWidgetItem(entry["time"]))
        else:
            table.setRowCount(1)
            table.setItem(0, 0, QTableWidgetItem("1"))
            table.setItem(0, 1, QTableWidgetItem("History is empty"))
            table.setItem(0, 2, QTableWidgetItem("N/A"))
            table.setItem(0, 3, QTableWidgetItem("N/A"))

        table.resizeColumnsToContents()
        layout.addWidget(table)

        delete_button = QPushButton("Delete Selected", dialog)
        delete_button.setFixedSize(150, 30)
        delete_button.setStyleSheet("background-color: #FF4040; color: white; font-size: 18px; border-radius: 10px;")
        delete_button.clicked.connect(lambda: self.delete_history_entry(table, dialog))
        layout.addWidget(delete_button, alignment=Qt.AlignmentFlag.AlignCenter)

        dialog.setLayout(layout)
        dialog.exec()

    def delete_history_entry(self, table, dialog):
        selected_rows = list(set(index.row() for index in table.selectedIndexes()))
        if not selected_rows:
            QMessageBox.warning(self.ui, "Selection Error", "Please select at least one entry to delete!")
            return
        for row in sorted(selected_rows, reverse=True):
            del self.logic.history[row]
        dialog.close()
        self.show_history()