import aboutDialog_ui
from PyQt4.QtGui import *

class AboutDialog(QDialog, aboutDialog_ui.Ui_AboutDialog):
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)