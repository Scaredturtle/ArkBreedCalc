import os
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
import windows.initial_dialog as initdiag
import dataGather.web_grab_new as web_grab

class dino_app_main_window(QMainWindow):
    def create_ui(self):
        super(dino_app_main_window, self).__init__()

        self.background_color = "background-color: rgb(15, 79, 87);"
        self.foreground_color = "background-color: cyan;"
        self.setWindowTitle("Ultimate Ark Companion")
        self.resolution = QDesktopWidget().screenGeometry()
        self.window_height = 600
        self.window_width = 800
        self.vertical_position = (self.resolution.height() - self.window_height)/2
        self.horizontal_position = (self.resolution.width() - self.window_width)/2

        self.create_display()
        self.file_check()

    def create_display(self):
        self.setStyleSheet(self.background_color)
        self.resize(self.window_width, self.window_height)
        self.move(self.horizontal_position, self.vertical_position)

    def file_check(self):
        existing_file = os.path.join('.', 'dinoData', 'dinoData.db')
        self.init_diag = initdiag.dino_app_initial_dialog()

        if os.path.isfile(existing_file):
            new_pull_ui = self.init_diag.create_ui()
            new_pull_ui.show()
        else:
            self.data_grab = web_grab.site_data_pull()
            self.data_grab.main_table_pull()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication([])
    app_main_window = QMainWindow()
    ui = dino_app_main_window()
    ui.create_ui(app_main_window)
    app_main_window.show()
	
    sys.exit(app.exec_())
	
