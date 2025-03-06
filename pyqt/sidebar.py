from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox, QHBoxLayout
from theme import MENU_COLOR, BUTTON_COLOR, MENU_ITEM_COLOR, TEXT_COLOR
from PyQt6.QtCore import QSize, Qt  
from PyQt6.QtGui import QPalette, QColor

class Sidebar(QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        self.setFixedWidth(200)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(MENU_COLOR))
        self.setPalette(palette)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 20, 0, 20)
        self.setLayout(layout)

        menu_layout = QVBoxLayout()
        layout.addLayout(menu_layout)

        menu_item_style = f"font-size: 24px;  background-color: {MENU_ITEM_COLOR};color: {TEXT_COLOR};"

        label1 = QLabel('Page 1')
        label1.setStyleSheet(menu_item_style)
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label1.setFixedHeight(50)
        label1.setFixedWidth(200)
        menu_layout.addWidget(label1)

        label2 = QLabel('Page 2')
        label2.setStyleSheet(menu_item_style)
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label2.setFixedHeight(50)
        label2.setFixedWidth(200)
        menu_layout.addWidget(label2)

        label3 = QLabel('Page 3')
        label3.setStyleSheet(menu_item_style)
        label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label3.setFixedHeight(50)
        label3.setFixedWidth(200)
        menu_layout.addWidget(label3)

        buttons_layout = QVBoxLayout()
        buttons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(buttons_layout)

        checkbox = QCheckBox('Check me!')
        checkbox.setStyleSheet(f"font-size: 24px; color: {TEXT_COLOR};")
        buttons_layout.addWidget(checkbox)

        button = QPushButton('CLICK ME!')
        button.setStyleSheet(f"background-color: {BUTTON_COLOR}; border-radius: 4px; padding: 4px; font-size: 24px;")
        button.setFixedWidth(150)
        button.clicked.connect(self.on_button_clicked)
        buttons_layout.addWidget(button)


    def on_button_clicked(self):
        print('clicked')

        


