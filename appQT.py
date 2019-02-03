import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import windows.mainWindowQT as main_window

dino_app = QApplication([])
dino_app.setStyle("Fusion")

dino_app_ui = main_window.dino_app_main_window()
dino_app_ui.create_ui()
dino_app_ui.show()

sys.exit(dino_app.exec_())
