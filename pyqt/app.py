from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QPalette, QColor, QFont
from header import Header
from sidebar import Sidebar
from body import Body

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DDS GUI POC")
        self.setFixedWidth(800)
        self.setFixedHeight(500)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(Header()) # Header

        body_layout = QHBoxLayout() # Body
        body_layout.addWidget(Sidebar()) # Left
        body_layout.addWidget(Body()) # Right

        main_layout.addLayout(body_layout)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        widget = QWidget()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)



app = QApplication([])
app.setFont(QFont("Courier New", 16))

window = MainWindow()
window.show()
app.exec()