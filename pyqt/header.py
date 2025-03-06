from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QToolButton
from PyQt6.QtGui import QPalette, QColor, QIcon, QAction, QPixmap
from theme import HEADER_COLOR
from PyQt6.QtCore import QSize


class Header(QWidget):
    """
    Header widget for the main window.
    Contains the title of the application and a menu button.
    """
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(HEADER_COLOR))
        self.setPalette(palette)

        self.setFixedHeight(50)

        layout = QHBoxLayout()

        label = QLabel('DDS GUI POC APP')
        label.setStyleSheet("font-size: 32px; font-weight: medium;")
        layout.addWidget(label)

        
        button = QToolButton()
        button.setIconSize(QSize(24, 24))
        icon = QIcon('../assets/icons8-menu-50.png')
        button.setIcon(icon)
        button.setStyleSheet("QToolButton { border: none; }")

        button.clicked.connect(self.on_button_clicked)

        layout.addWidget(button)

        
        self.setLayout(layout)

    def on_button_clicked(self):
        print('clicked')


