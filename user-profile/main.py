import sys
from UserProfile import get_profile
from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtGui import QFont, QPixmap
from PIL.ImageQt import ImageQt


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.profile = get_profile()
        self.initialize_ui()

    def initialize_ui(self):
        self.setWindowTitle("User Profile")
        self.setFixedSize(500, 550)
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

        skills_header = QLabel(self)
        skills_header.setText("Skills")
        skills_header.setFont(QFont("Arial", 16))
        skills_header.move(0, 340)

        skills_label = QLabel(self)
        skills_label.setText(self.profile.skills)
        skills_label.move(50, 365)

        experience_header = QLabel(self)
        experience_header.setText("Experience")
        experience_header.setFont(QFont("Arial", 16))
        experience_header.move(0, 390)

        title1 = QLabel(self)
        title1.setText(self.profile.experience[0][0])
        title1.move(50, 420)

        description1 = QLabel(self)
        description1.setText("- " + self.profile.experience[0][1])
        description1.move(75, 440)

        title2 = QLabel(self)
        title2.setText(self.profile.experience[1][0])
        title2.move(50, 460)

        description2 = QLabel(self)
        description2.setText("- " + self.profile.experience[1][1])
        description2.move(75, 480)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
