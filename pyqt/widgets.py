from PyQt6.QtGui import QAction, QColor, QIcon
from PyQt6.QtWidgets import QAbstractButton, QApplication, QCheckBox, QColorDialog, QComboBox, QCommandLinkButton, QDateTimeEdit, QDial, QDockWidget, QErrorMessage, QFileDialog, QFontDialog, QInputDialog, QLCDNumber, QLabel, QLineEdit, QListWidget, QMainWindow, QMenu, QMenuBar, QMessageBox, QProgressBar, QProgressDialog, QPushButton, QRadioButton, QScrollArea, QSlider, QSpinBox, QSplashScreen, QStackedLayout, QStackedWidget, QStatusBar, QStyleOptionButton, QStyleOptionToolButton, QTabWidget, QTableWidget, QTextEdit, QToolButton, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QHBoxLayout, QWhatsThis, QWidget    


class ButtonWidgets(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.setLayout(layout)

        layout.addWidget(QPushButton("Push button"))
        #layout.addWidget(QAbstractButton())
        layout.addWidget(QCommandLinkButton("Command link button"))
        layout.addWidget(QRadioButton("Radio button"))
        #layout.addWidget(QStyleOptionButton())
        layout.addWidget(QToolButton())
        #layout.addWidget(QStyleOptionToolButton())
        layout.addWidget(QCheckBox("Check box"))

class InputWidgets(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QLineEdit("Line edit"))
        layout.addWidget(QTextEdit("Text edit"))
        layout.addWidget(QInputDialog())

        layout.addWidget(QSpinBox())

        layout.addWidget(QDateTimeEdit())

        

class SelectWidgets(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        combo_box = QComboBox()
        combo_box.addItem("Item 1")
        combo_box.addItem("Item 2")
        combo_box.addItem("Item 3")
        layout.addWidget(combo_box) 

       

        file_select_button = QPushButton("Select file")
        file_select_button.clicked.connect(self.select_file)
        layout.addWidget(file_select_button)


    def select_file(self):
        file_dialog = QFileDialog()
        file_dialog.exec()

class ContainerWidgets(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        dock_widget = QDockWidget()
        dock_widget.setWidget(QLabel("Dock widget"))
        layout.addWidget(dock_widget)

        tab_widget = QTabWidget()
        tab_widget.addTab(QLabel("Tab 1"), "Tab 1")
        tab_widget.addTab(QLabel("Tab 2"), "Tab 2")
        layout.addWidget(tab_widget)

        self.stack_widget = QStackedWidget()
        self.stack_widget.addWidget(QLabel("Stack 1"))
        self.stack_widget.addWidget(QLabel("Stack 2"))
        self.stack_widget.setCurrentIndex(0)
        layout.addWidget(self.stack_widget)


        stack_button = QPushButton("Stack button")
        stack_button.clicked.connect(self.stack_widget_changed)
        layout.addWidget(stack_button)



    def stack_widget_changed(self):
        if self.stack_widget.currentIndex() == 0:
            self.stack_widget.setCurrentIndex(1)
        else:
            self.stack_widget.setCurrentIndex(0)

class DisplayWidgets(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QLCDNumber())

        list_widget = QListWidget()
        list_widget.addItem("Item 1")
        list_widget.addItem("Item 2")
        list_widget.addItem("Item 3")
        layout.addWidget(list_widget)

        table_widget = QTableWidget()
        table_widget.setColumnCount(3)
        table_widget.setRowCount(3)
        layout.addWidget(table_widget)
        

class RandomWidgets(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QDial())

        layout.addWidget(QSlider())

        progress_bar = QProgressBar()
        progress_bar.setValue(50)
        layout.addWidget(progress_bar)


class MessageWidgets(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)  

        layout.addWidget(QErrorMessage())
        layout.addWidget(QMessageBox())


class Widgets(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widgets")
        
        main_layout = QVBoxLayout()
       
        tabs = QTabWidget()
        tabs.addTab(ButtonWidgets(), "Button Widgets")
        tabs.addTab(InputWidgets(), "Input Widgets")
        tabs.addTab(SelectWidgets(), "Select Widgets")
        tabs.addTab(ContainerWidgets(), "Container Widgets")
        tabs.addTab(DisplayWidgets(), "Display Widgets")
        tabs.addTab(RandomWidgets(), "Random Widgets")
        tabs.addTab(MessageWidgets(), "Message Widgets")
        main_layout.addWidget(tabs)

        widget = QWidget()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)



app = QApplication([])

window = Widgets()
window.show()
app.exec()