import sys
from UserProfile import get_profile
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
from PIL.ImageQt import ImageQt


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.profile = get_profile()
        self.initialize_ui()

    def initialize_ui(self):
        self.setWindowTitle("User Profile")
        self.setGeometry(0, 0, 500, 500)
        self.add_widgets()
        self.show()

    def add_widgets(self):
        def load_image(image):
            return ImageQt(image)

        background_image = load_image("./images/background.jpg")
        background_image_label = QLabel(self)
        background_image_pixmap = QPixmap()
        background_image_pixmap.convertFromImage(background_image)
        background_image_label.setPixmap(background_image_pixmap.scaled(500, 250))

        profile_image = load_image(self.profile.profile_image)
        profile_image_label = QLabel(self)
        profile_image_pixmap = QPixmap()
        profile_image_pixmap.convertFromImage(profile_image)
        profile_image_label.setPixmap(profile_image_pixmap.scaled(250, 250))
        profile_image_label.move(125, 0)

        bio_header = QLabel(self)
        bio_header.setText("Biography")
        bio_header.setFont(QFont("Arial", 16))
        bio_header.move(0, 255)

        bio_label = QLabel(self)
        bio_label.setText(self.profile.biography)
        bio_label.setWordWrap(True)
        bio_label.move(50, 280)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
