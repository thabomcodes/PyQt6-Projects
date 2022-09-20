from GuessingGame import GuessingGame
import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QFont


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.result = None
        self.restart_button = None
        self.guess_button = None
        self.edit = None
        self.label = None
        self.initialize_ui()

        self.guess_game = GuessingGame(1, 5)
        self.guess = self.guess_game.get_number()

    def initialize_ui(self):
        self.setWindowTitle("Guessing Game")
        self.setFixedSize(500, 170)
        self.add_widgets()
        self.show()

    def add_widgets(self):
        self.label = QLabel(self)
        self.label.setText("Please guess a number between 1 and 5")
        self.label.setFont(QFont("Arial", 16))
        self.label.move(50, 20)

        self.edit = QLineEdit(self)
        self.edit.move(175, 60)
        self.edit.returnPressed.connect(self.guess_clicked)

        self.result = QLabel(self)
        self.result.setText("")
        self.result.move(130, 90)

        self.guess_button = QPushButton("Guess", self)
        self.guess_button.move(150, 120)
        self.guess_button.clicked.connect(self.guess_clicked)

        self.restart_button = QPushButton("Restart", self)
        self.restart_button.move(260, 120)
        self.restart_button.clicked.connect(self.restart_clicked)

    def guess_clicked(self):

        self.guess_button.setEnabled(False)
        guess = self.edit.text()
        try:
            guess = int(guess)
            if self.guess == guess:
                msg = f"You win! {self.guess} is the correct number."
                self.result.setText(msg)
            else:
                msg = f"You lose! {self.guess} is the correct number."
                self.result.setText(msg)

            self.result.adjustSize()

        except ValueError:
            pass

    def restart_clicked(self):
        self.guess = self.guess_game.get_number()
        self.guess_button.setEnabled(True)
        self.result.setText("")
        self.edit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
