from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

class dino_app_main_window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.background_color = "background-color: blue;"
        self.foreground_color = "background-color: cyan;"
        self.setWindowTitle("Ultimate Ark Companion")
        self.resolution = QDesktopWidget().screenGeometry()
        self.window_height = 600
        self.window_width = 800
        self.vertical_position = (self.resolution.height() - self.window_height)/2
        self.horizontal_position = (self.resolution.width() - self.window_width)/2

        self.create_display()

    def create_display(self):
        self.setStyleSheet(self.background_color)
        self.resize(self.window_width, self.window_height)
        self.move(self.horizontal_position, self.vertical_position)