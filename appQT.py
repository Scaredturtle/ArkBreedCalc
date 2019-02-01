import sys
from PyQt5.QtWidgets import QApplication
import windows.mainWindowQT as main_window

dino_app = QApplication([])
dino_app.setStyle("Fusion")

dino_app_window = main_window.dino_app_main_window()
dino_app_window.show()

sys.exit(dino_app.exec_())