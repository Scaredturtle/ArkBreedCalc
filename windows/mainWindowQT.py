from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

class dino_app_main_window(QMainWindow):
    def create_ui(self):
        super().__init__()

        self.background_color = "background-color: rgb(15, 79, 87);"
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

if __name__ == '__main__':
    import sys
    from PyQt5 import QtApplication
    
    app = QtApplication([])
    app_main_window = QMainWindow()
    ui = dino_app_main_window()
    ui.createUI(app_main_window)
    app_main_window.show()
	
    sys.exit(app.exec_())
	
