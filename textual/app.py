from textual.app import App, ComposeResult
from textual.widgets import Static, Label, Checkbox, Button

class Header(Static):
    def __init__(self):
        super().__init__()
        self.classes = "box"
        self.id = "header"

    def compose(self) -> ComposeResult:
        yield Label("DDS GUI POC APP", classes="header-title")

class Sidebar(Static):
    def __init__(self):
        super().__init__()
        self.classes = "box"
        self.id = "sidebar"

    def compose(self) -> ComposeResult:
        yield Label("Sidebar")
        yield Static("Page 1", classes="sidebar-page")
        yield Static("Page 2", classes="sidebar-page")
        yield Static("Page 3", classes="sidebar-page")
        yield Checkbox("Check me!", id="sidebar-checkbox")
        yield Button("CLICK ME", id="sidebar-button")

class Body(Static):
    def __init__(self):
        super().__init__()
        self.classes = "box"
        self.id = "body"

    def compose(self) -> ComposeResult:
        yield Label("Body")

class App(App):
    CSS_PATH = "app.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Sidebar()
        yield Body()

App().run()