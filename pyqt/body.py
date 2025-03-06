from re import L, M
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt
from theme import BODY_COLOR, TEXT_COLOR
from welcome_text import WELCOME_TEXT
class Body(QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(BODY_COLOR))
        self.setPalette(palette)
        self.setFixedWidth(600)
        self.setContentsMargins(10, 10, 10, 10)

        master_layout = QVBoxLayout()
        welcome_text = QLabel("Welcome to the DDS GUI POC!")
        welcome_text.setStyleSheet(f"color: {TEXT_COLOR}; font-size: 32px;")
        master_layout.addWidget(welcome_text)

        layout = QHBoxLayout()

        label = QLabel(WELCOME_TEXT)
        label.setWordWrap(True)
        label.setFixedWidth(200)
        label.setStyleSheet(f"color: black; font-size: 16px;")
        layout.addWidget(label)

        image = QLabel()
        image.setPixmap(QPixmap('../assets/image.jpg'))
        image.setScaledContents(True)
        layout.addWidget(image)

        master_layout.addLayout(layout)
        master_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(master_layout)
