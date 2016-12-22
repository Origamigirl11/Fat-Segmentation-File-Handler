# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(837, 566)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.convertBtn = QtGui.QPushButton(self.centralwidget)
        self.convertBtn.setObjectName(_fromUtf8("convertBtn"))
        self.verticalLayout.addWidget(self.convertBtn)
        self.aboutBtn = QtGui.QPushButton(self.centralwidget)
        self.aboutBtn.setObjectName(_fromUtf8("aboutBtn"))
        self.verticalLayout.addWidget(self.aboutBtn)
        self.gridLayout.addLayout(self.verticalLayout, 6, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.appendSrcCheckbox = QtGui.QCheckBox(self.centralwidget)
        self.appendSrcCheckbox.setObjectName(_fromUtf8("appendSrcCheckbox"))
        self.horizontalLayout_3.addWidget(self.appendSrcCheckbox)
        self.browseSrcBtn = QtGui.QPushButton(self.centralwidget)
        self.browseSrcBtn.setObjectName(_fromUtf8("browseSrcBtn"))
        self.horizontalLayout_3.addWidget(self.browseSrcBtn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.destEdit = QtGui.QLineEdit(self.centralwidget)
        self.destEdit.setObjectName(_fromUtf8("destEdit"))
        self.horizontalLayout.addWidget(self.destEdit)
        self.browseDestBtn = QtGui.QPushButton(self.centralwidget)
        self.browseDestBtn.setObjectName(_fromUtf8("browseDestBtn"))
        self.horizontalLayout.addWidget(self.browseDestBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.sourceTable = QtGui.QTableWidget(self.centralwidget)
        self.sourceTable.setObjectName(_fromUtf8("sourceTable"))
        self.sourceTable.setColumnCount(0)
        self.sourceTable.setRowCount(0)
        self.gridLayout.addWidget(self.sourceTable, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Fat Segmentation File Chooser", None))
        self.convertBtn.setText(_translate("MainWindow", "Convert", None))
        self.aboutBtn.setText(_translate("MainWindow", "About", None))
        self.label.setText(_translate("MainWindow", "Source Folders:", None))
        self.appendSrcCheckbox.setText(_translate("MainWindow", "Append to List", None))
        self.browseSrcBtn.setText(_translate("MainWindow", "Browse", None))
        self.label_2.setText(_translate("MainWindow", "Destination Folder:", None))
        self.browseDestBtn.setText(_translate("MainWindow", "Browse", None))

