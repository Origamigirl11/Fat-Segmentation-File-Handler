import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mainWindow import *

localDir = os.path.expandvars("%HOMEDRIVE%%HOMEPATH%\AppData\Local\Microsoft\Windows\FileHistory")
localConfigDir = os.path.join(localDir, "Configuration")
localDataDir = os.path.join(localDir, "Data")

localConfig1 = os.path.join(localConfigDir, "Config1.xml")
localConfig2 = os.path.join(localConfigDir, "Config2.xml")
localCatalogDir1 = os.path.join(localConfigDir, "Catalog1.edb")
localCatalogDir2 = os.path.join(localConfigDir, "Catalog2.edb")

def main():
    app = QApplication(sys.argv)

    form = MainWindow()
    form.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
