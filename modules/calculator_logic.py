from PyQt6.QtWidgets import QInputDialog
from PyQt6.QtCore import Qt
import math
import re


class CalculatorLogic:
    def __init__(self, ui):
        self.ui = ui
        self.history = []

    def on_button_clicked(self):
        text = self.ui.sender().text()
        if text == 'C':
            self.ui.display.clear()
            self.ui.display.setPlaceholderText("Please, type your text")
        elif text == '⌧':
            self.ui.display.setText(self.ui.display.text()[:-1])
            if not self.ui.display.text():
                self.ui.display.setPlaceholderText("Please, type your text")
        elif text == '=':
            self.calculate_result()
        elif text in ('sin', 'cos', 'tan', 'cot', '√'):
            self.ui.display.setText(self.ui.display.text() + text + '(')
        elif text == '^':
            self.ui.display.setText(self.ui.display.text() + '**')
        elif text == '½':
            self.insert_fraction()
        else:
            self.ui.display.setText(self.ui.display.text() + text)

    def insert_fraction(self):
        numerator, ok1 = QInputDialog.getDouble(self.ui, "Fraction", "Enter numerator:")
        if not ok1:
            return
        denominator, ok2 = QInputDialog.getDouble(self.ui, "Fraction", "Enter denominator:")
        if not ok2 or denominator == 0:
            self.ui.display.clear()
            self.ui.display.setPlaceholderText("Error: Invalid denominator!")
            return
        fraction = f"({numerator}/{denominator})"
        self.ui.display.setText(self.ui.display.text() + fraction)

    def calculate_result(self):
        from datetime import datetime
        try:
            expression = self.ui.display.text()
            expression = re.sub(r'sin\(([^)]+)\)', r'math.sin(math.radians(\g<1>))', expression)
            expression = re.sub(r'cos\(([^)]+)\)', r'math.cos(math.radians(\g<1>))', expression)
            expression = re.sub(r'tan\(([^)]+)\)', r'math.tan(math.radians(\g<1>))', expression)
            expression = re.sub(r'cot\(([^)]+)\)', r'(1 / math.tan(math.radians(\g<1>)))', expression)
            expression = re.sub(r'√\(([^)]+)\)', r'math.sqrt(\g<1>)', expression)

            result = eval(expression, {"math": math, "__builtins__": {}})
            result_str = str(round(result, 4))
            self.ui.display.setText(result_str)
            self.history.append({
                "calculation": f"{expression} = {result_str}",
                "creator": "Amin Moniry",
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        except ZeroDivisionError:
            self.ui.display.clear()
            self.ui.display.setPlaceholderText("Error: Division by zero!")
        except SyntaxError:
            self.ui.display.clear()
            self.ui.display.setPlaceholderText("Error: Invalid syntax!")
        except Exception as e:
            self.ui.display.clear()
            self.ui.display.setPlaceholderText(f"Error: {str(e)}")

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Enter, Qt.Key.Key_Return):
            self.calculate_result()
        elif event.key() == Qt.Key.Key_Backspace:
            self.ui.display.setText(self.ui.display.text()[:-1])
            if not self.ui.display.text():
                self.ui.display.setPlaceholderText("Please, type your text")