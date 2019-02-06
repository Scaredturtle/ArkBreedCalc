import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import windows.mainWindowQT as main_window
import dataGather.web_grab_new as gather

dino_app = QApplication([])
dino_app.setStyle("Fusion")

dino_app_ui = main_window.dino_app_main_window()
dino_app_ui.create_ui()
dino_app_ui.show()

#scrape = gather.site_data_pull()
#scrape.main_table_pull()

sys.exit(dino_app.exec_())
