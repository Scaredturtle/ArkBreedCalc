from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

class dino_app_initial_dialog(QMainWindow):
    def create_ui(self):
        super(dino_app_initial_dialog, self).__init__()
        
        self.background_color = "background-color: rgb(15, 79, 87);"
        self.setWindowTitle("Existing Data Found")
        self.resolution = QDesktopWidget().screenGeometry()
        self.window_height = 60
        self.window_width = 80
        self.vertical_position = (self.resolution.height() - self.window_height) / 2
        self.horizontal_position = (self.resolution.width() - self.window_width) / 2

        self.create_display()

    def create_display(self):
        self.setStyleSheet(self.background_color)
        self.resize(self.window_width, self.window_height)
        self.move(self.horizontal_position, self.vertical_position)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])
    app_main_window = QMainWindow()
    ui = dino_app_initial_dialog
    ui.create_ui(app_main_window)
    app_main_window.show()

    sys.exit(app.exec_())