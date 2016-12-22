import mainWindow_ui
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
import os.path
import shutil
from datetime import datetime
from lxml import etree
from aboutDialog import *

class MainWindow(QMainWindow, mainWindow_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.sourceTable.setColumnCount(2)
        self.sourceTable.setHorizontalHeaderLabels(["Directory", "New Directory Name"])
        self.sourceTable.horizontalHeader().setStretchLastSection(False)
        self.sourceTable.horizontalHeader().setResizeMode(0, QHeaderView.Stretch)
        self.sourceTable.horizontalHeader().setResizeMode(1, QHeaderView.ResizeToContents)

    @pyqtSlot()
    def on_browseDestBtn_clicked(self):

        # Open up dialog to get directory
        dir = QFileDialog.getExistingDirectory(self, "Select destination directory", os.path.expanduser("~"), QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog)

        # If user pressed cancel, return
        if not dir:
            return

        # Make sure directory is valid
        if not os.path.isdir(dir):
            QMessageBox.critical(self, "Invalid directory", "The directory you chose was invalid")
            return

        # Set the text in the box
        self.destEdit.setText(dir)

    @pyqtSlot()
    def on_browseSrcBtn_clicked(self):
        w = QFileDialog(self)
        w.setFileMode(QFileDialog.DirectoryOnly)
        # Must use custom dialog if I want multiple directories to be selected
        w.setOption(QFileDialog.DontUseNativeDialog, True)

        # Custom command to allow for multiple directories to be selected
        for view in self.findChildren((QListView, QTreeView)):
            if isinstance(view.model(), QFileSystemModel):
                view.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # Start the dialog box and wait for input, it returns false if cancel was pressed
        if not w.exec():
            return

        # Get selected directories
        dirs = w.selectedFiles()

        # If empty, then cancel was pressed, return
        if not dirs:
            return

        if not self.appendSrcCheckbox.isChecked():
            self.sourceTable.setRowCount(0)

        # Check to make sure the directories are valid
        error = False
        for dir in dirs:
            if os.path.isdir(dir):
                i = 1
                rowCount = self.sourceTable.rowCount()
                self.sourceTable.insertRow(rowCount)
                self.sourceTable.setItem(rowCount, 0, QTableWidgetItem(dir))
                self.sourceTable.setItem(rowCount, 1, QTableWidgetItem("SubjectXXXX_Initial/Final"))
            else:
                error = True

        # If an error occurred, tell the user that the directory was not added
        if error:
            QMessageBox.critical(self, "Invalid directory", "One of the directories you chose was invalid. It was not added to the list")

    @pyqtSlot()
    def on_convertBtn_clicked(self):
        # If there are no source files, then return
        if self.sourceTable.rowCount() is 0:
            QMessageBox.warning(self, "No source directories", "There are no source directories in the list currently. Please add some folders before converting.")
            return

        # If there are no destination folder, then return
        if not self.destEdit.text():
            QMessageBox.warning(self, "No destination directory", "There is no destination directory currently. Please select one before converting.")
            return

        # Search for abdomen folder to go into
        rowCount = self.sourceTable.rowCount()
        for row in range(0, rowCount):
            dir = self.sourceTable.item(row, 0).text()
            newDirName = self.sourceTable.item(row, 1).text()

            destPath = os.path.join(self.destEdit.text(), newDirName)
            os.makedirs(destPath, exist_ok=True)

            # Go into dir/ and search for abdomen folder.
            for name1 in os.listdir(dir):
                fullPath1 = os.path.join(dir, name1)

                if not os.path.isdir(fullPath1):
                    continue

                # Customize this part for each MRI place we use
                if 'abdomen_abd' in name1[:11].lower():
                    fatIndices = []
                    waterIndices = []
                    for name2 in os.listdir(fullPath1):
                        fullPath2 = os.path.join(fullPath1, name2)

                        if 't1_vibe_dixon' in name2[:13].lower():
                            ids = name2.split('_')

                            index = int(ids[-1])
                            type = ids[-2].lower()

                            if type == 'f':
                                fatIndices.append([index, name2, fullPath2])
                            else: # Water
                                waterIndices.append([index, name2, fullPath2])

                        if name2.lower().endswith("registered.mat"):
                            shutil.copyfile(fullPath2, os.path.join(destPath, newDirName.lower() + "_registered.mat"))

                        if name2.lower().endswith("results.mat"):
                            shutil.copyfile(fullPath2, os.path.join(destPath, newDirName.lower() + "_results.mat"))

                    if not (len(fatIndices) is 2 or len(waterIndices) is 2):
                        print(len(fatIndices))
                        print(len(waterIndices))
                        print("Could not find appropiate folder T1_VIBE_DIXON...")
                        break

                    fatLowerInfo = fatIndices[0] if (fatIndices[0][0] > fatIndices[1][0]) else fatIndices[1]
                    found = False
                    for file in os.listdir(fatLowerInfo[2]):
                        if file.endswith("resliced.nii"):
                            fatLowerInfo[2] = os.path.join(fatLowerInfo[2], file)
                            found = True
                            break

                    if found:
                        shutil.copyfile(fatLowerInfo[2], os.path.join(destPath, "fatLower.nii"))
                    else:
                        print('Unable to find a resliced.nii file in ' + fatLowerInfo[2])
                        break

                    fatUpperInfo = fatIndices[0] if (fatIndices[0][0] < fatIndices[1][0]) else fatIndices[1]
                    found = False
                    for file in os.listdir(fatUpperInfo[2]):
                        if file.endswith("resliced.nii"):
                            fatUpperInfo[2] = os.path.join(fatUpperInfo[2], file)
                            found = True
                            break

                    if found:
                        shutil.copyfile(fatUpperInfo[2], os.path.join(destPath, "fatUpper.nii"))
                    else:
                        print('Unable to find a resliced.nii file in ' + fatUpperInfo[2])
                        break

                    waterLowerInfo = waterIndices[0] if (waterIndices[0][0] > waterIndices[1][0]) else waterIndices[1]
                    found = False
                    for file in os.listdir(waterLowerInfo[2]):
                        if file.endswith("resliced.nii"):
                            waterLowerInfo[2] = os.path.join(waterLowerInfo[2], file)
                            found = True
                            break

                    if found:
                        shutil.copyfile(waterLowerInfo[2], os.path.join(destPath, "waterLower.nii"))
                    else:
                        print('Unable to find a resliced.nii file in ' + waterLowerInfo[2])
                        break

                    waterUpperInfo = waterIndices[0] if (waterIndices[0][0] < waterIndices[1][0]) else waterIndices[1]
                    found = False
                    for file in os.listdir(waterUpperInfo[2]):
                        if file.endswith("resliced.nii"):
                            waterUpperInfo[2] = os.path.join(waterUpperInfo[2], file)
                            found = True
                            break

                    if found:
                        shutil.copyfile(waterUpperInfo[2], os.path.join(destPath, "waterUpper.nii"))
                    else:
                        print('Unable to find a resliced.nii file in ' + waterUpperInfo[2])
                        break

                    nameSplit = name1.split("_")

                    # XML File
                    xmlRoot = etree.Element("config", SchemaVersion="1")

                    etree.SubElement(xmlRoot, "scanDate", value=datetime.strptime(nameSplit[2], "%Y%m%d")\
                                                                            .strftime('%b %d, %Y'))
                    etree.SubElement(xmlRoot, "imageUpper", startSlice="12", stopSlice="24")
                    etree.SubElement(xmlRoot, "imageLower", startSlice="12", stopSlice="24")

                    xmlEAT = etree.SubElement(xmlRoot, "EAT")
                    etree.SubElement(xmlEAT, "search", startSlice="50", stopSlice="100")

                    xmlPAT = etree.SubElement(xmlRoot, "PAT")
                    etree.SubElement(xmlPAT, "search", startSlice="50", stopSlice="100")

                    xmlPAAT = etree.SubElement(xmlRoot, "PAAT")
                    etree.SubElement(xmlPAAT, "search", startSlice="50", stopSlice="100")

                    xmlVAT = etree.SubElement(xmlRoot, "VAT")
                    etree.SubElement(xmlVAT, "search", startSlice="50", stopSlice="100")

                    xmlSCAT = etree.SubElement(xmlRoot, "SCAT")
                    etree.SubElement(xmlSCAT, "search", startSlice="50", stopSlice="100")

                    etree.ElementTree(xmlRoot).write(os.path.join(destPath, 'config.xml'), encoding="UTF-8",\
                                                  xml_declaration=True, pretty_print=True)

                    print("Finished " + destPath)

    @pyqtSlot()
    def on_aboutBtn_clicked(self):
        aboutDialog = AboutDialog()
        aboutDialog.exec()