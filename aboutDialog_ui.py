# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.resize(737, 372)
        self.verticalLayout = QtGui.QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(AboutDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About Fat Segmentation File Chooser", None))
        self.label.setText(_translate("AboutDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Author:</span> Addison Elliott</p><p><span style=\" font-weight:600;\">Overview: </span>The purpose of this program is to convert MRI scans into a standardized format. The program searches in destination folder for the four NIFTI images: fat upper, fat lower, water upper, and water lower. These are renamed and placed in the destination folder. In addition, an XML file is created for configuration options. Also, if a .mat file that ends with registered or results, then it will be copied over to the destination folder. </p><p><span style=\" font-weight:600;\">Instructions:</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:4px;\">Select the destination folder where you would like the new MRI scan information to be stored. A subfolder will be made within this destination folder to store the scan data which is named based on the <span style=\" font-style:italic;\">New Directory Field</span> in the source list view. So the actual folder where data is stored is destination folder plus the new directory name.</li><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the source folder for each MRI scan you would like to transfer over into the destination folder. Select the outermost folder that represents the scan data. As an example, there is a folder <span style=\" font-style:italic;\">MF0203_1026153</span> with the subfolder <span style=\" font-style:italic;\">ABDOMEN_ABD_20151026_150801_304000</span> which contains more subfolders with the data. The user would select <span style=\" font-style:italic;\">MF0203_1026153</span> as the source folder. The program will traverse into the directories and read the data from there.</li><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the new directory name for each of the source folders. This is the subfolder that will be created in the destination folder to store the data. A suggested format is present of <span style=\" font-style:italic;\">SubjectXXX_Initial/Final</span> where XXXX is the subject number and Initial/Final is pre/post intervention.</li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hit Convert to have the program convert the source folders to the destination folder.</li></ul></body></html>", None))

