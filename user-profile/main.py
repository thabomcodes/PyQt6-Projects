import sys
from UserProfile import get_profile
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.profile = get_profile()


