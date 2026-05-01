import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

class MyApp(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(300, 200)
        self.label = QLabel("Default Text", self)
        self.label.move(50, 50)
        self.button_y = 100  # to position buttons

    def addTextBlock(self, text):
        self.label.setText(text)

    def addButton(self, name, function):
        button = QPushButton(name, self)
        button.clicked.connect(function)
        button.move(50, self.button_y)
        self.button_y += 50  # stack buttons

def wrap_window(title):
    return MyApp(title)

def addTextBlock(window, text):
    window.addTextBlock(text)

def Wrap_button(window, name, function):
    window.addButton(name, function)

def wrap_start():
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = wrap_window("Test")
        addTextBlock(window, "Check")
        Wrap_button(window, "Clicks", lambda: print("ale"))
        Wrap_button(window, "dj", lambda: print("kale"))
        window.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    wrap_start()
