# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\\main\\python\\ui\\main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 703)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 180, 1012, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(1000, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(12, -1, 11, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 476))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.treeView = QtWidgets.QTreeView(self.groupBox)
        self.treeView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QtCore.QSize(700, 0))
        self.treeView.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.treeView.setFont(font)
        self.treeView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.treeView.setObjectName("treeView")
        self.horizontalLayout.addWidget(self.treeView)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 1051, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("border: 0;background-color: rgb(16, 23, 30)")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.closebutton = QtWidgets.QPushButton(self.frame)
        self.closebutton.setGeometry(QtCore.QRect(970, 0, 71, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closebutton.sizePolicy().hasHeightForWidth())
        self.closebutton.setSizePolicy(sizePolicy)
        self.closebutton.setFlat(True)
        self.closebutton.setObjectName("closebutton")
        self.minimizebutton = QtWidgets.QPushButton(self.frame)
        self.minimizebutton.setGeometry(QtCore.QRect(900, 0, 71, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimizebutton.sizePolicy().hasHeightForWidth())
        self.minimizebutton.setSizePolicy(sizePolicy)
        self.minimizebutton.setFlat(True)
        self.minimizebutton.setObjectName("minimizebutton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(24, 0, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Cute Zealand")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(-10, 30, 1051, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet("border: 0;\n"
"background-color: rgb(28, 41, 54);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.File = QtWidgets.QPushButton(self.frame_3)
        self.File.setGeometry(QtCore.QRect(20, 0, 81, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.File.sizePolicy().hasHeightForWidth())
        self.File.setSizePolicy(sizePolicy)
        self.File.setStyleSheet("border: none;")
        self.File.setFlat(True)
        self.File.setObjectName("File")
        self.settingsbutton = QtWidgets.QPushButton(self.frame_3)
        self.settingsbutton.setGeometry(QtCore.QRect(100, 0, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsbutton.sizePolicy().hasHeightForWidth())
        self.settingsbutton.setSizePolicy(sizePolicy)
        self.settingsbutton.setStyleSheet("border: none;")
        self.settingsbutton.setFlat(True)
        self.settingsbutton.setObjectName("settingsbutton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(20, 90, 851, 51))
        font = QtGui.QFont()
        font.setFamily("Cute Zealand")
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setToolTip("")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.clientlabel = QtWidgets.QLabel(self.centralwidget)
        self.clientlabel.setGeometry(QtCore.QRect(20, 90, 841, 51))
        font = QtGui.QFont()
        font.setFamily("Cute Zealand")
        font.setPointSize(20)
        self.clientlabel.setFont(font)
        self.clientlabel.setObjectName("clientlabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 1032, 1))
        self.line.setMinimumSize(QtCore.QSize(1032, 0))
        self.line.setMaximumSize(QtCore.QSize(900, 1))
        self.line.setBaseSize(QtCore.QSize(0, 0))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(920, 70, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Cute Zealand")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.leftarrow = QtWidgets.QPushButton(self.centralwidget)
        self.leftarrow.setGeometry(QtCore.QRect(880, 60, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.leftarrow.setFont(font)
        self.leftarrow.setStyleSheet("background-color: rgb(25, 35, 45);\n"
"border-color: rgb(25, 35, 45);")
        self.leftarrow.setObjectName("leftarrow")
        self.rightarrow = QtWidgets.QPushButton(self.centralwidget)
        self.rightarrow.setGeometry(QtCore.QRect(990, 60, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rightarrow.setFont(font)
        self.rightarrow.setStyleSheet("background-color: rgb(25, 35, 45);\n"
"border-color: rgb(25, 35, 45);")
        self.rightarrow.setObjectName("rightarrow")
        self.yearline = QtWidgets.QLineEdit(self.centralwidget)
        self.yearline.setGeometry(QtCore.QRect(880, 90, 141, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(24)
        self.yearline.setFont(font)
        self.yearline.setStyleSheet("")
        self.yearline.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.yearline.setAlignment(QtCore.Qt.AlignCenter)
        self.yearline.setObjectName("yearline")
        self.addressbar = QtWidgets.QLineEdit(self.centralwidget)
        self.addressbar.setGeometry(QtCore.QRect(140, 150, 881, 31))
        self.addressbar.setObjectName("addressbar")
        self.upper = QtWidgets.QPushButton(self.centralwidget)
        self.upper.setGeometry(QtCore.QRect(100, 150, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.upper.setFont(font)
        self.upper.setStyleSheet("background-color: rgb(28, 41, 54);")
        self.upper.setObjectName("upper")
        self.forwardbutton = QtWidgets.QPushButton(self.centralwidget)
        self.forwardbutton.setGeometry(QtCore.QRect(60, 150, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.forwardbutton.setFont(font)
        self.forwardbutton.setStyleSheet("background-color: rgb(28, 41, 54);")
        self.forwardbutton.setObjectName("forwardbutton")
        self.backbutton = QtWidgets.QPushButton(self.centralwidget)
        self.backbutton.setGeometry(QtCore.QRect(20, 150, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.backbutton.setFont(font)
        self.backbutton.setStyleSheet("background-color: rgb(28, 41, 54);")
        self.backbutton.setObjectName("backbutton")
        self.lineEdit.raise_()
        self.groupBox.raise_()
        self.frame.raise_()
        self.frame_3.raise_()
        self.clientlabel.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.leftarrow.raise_()
        self.rightarrow.raise_()
        self.yearline.raise_()
        self.line.raise_()
        self.addressbar.raise_()
        self.upper.raise_()
        self.forwardbutton.raise_()
        self.backbutton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.minimizebutton, self.closebutton)
        MainWindow.setTabOrder(self.closebutton, self.File)
        MainWindow.setTabOrder(self.File, self.settingsbutton)
        MainWindow.setTabOrder(self.settingsbutton, self.leftarrow)
        MainWindow.setTabOrder(self.leftarrow, self.rightarrow)
        MainWindow.setTabOrder(self.rightarrow, self.yearline)
        MainWindow.setTabOrder(self.yearline, self.backbutton)
        MainWindow.setTabOrder(self.backbutton, self.forwardbutton)
        MainWindow.setTabOrder(self.forwardbutton, self.upper)
        MainWindow.setTabOrder(self.upper, self.addressbar)
        MainWindow.setTabOrder(self.addressbar, self.scrollArea)
        MainWindow.setTabOrder(self.scrollArea, self.treeView)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Information"))
        self.closebutton.setText(_translate("MainWindow", "X"))
        self.minimizebutton.setText(_translate("MainWindow", "-"))
        self.label.setText(_translate("MainWindow", "Client File Browser v2.0"))
        self.File.setText(_translate("MainWindow", "File"))
        self.settingsbutton.setText(_translate("MainWindow", "Settings"))
        self.clientlabel.setText(_translate("MainWindow", "Select a client..."))
        self.label_2.setText(_translate("MainWindow", "CLIENT NAME"))
        self.label_3.setText(_translate("MainWindow", "TAX YEAR"))
        self.leftarrow.setText(_translate("MainWindow", "⯇"))
        self.rightarrow.setText(_translate("MainWindow", "⯈"))
        self.upper.setText(_translate("MainWindow", "🡅"))
        self.forwardbutton.setText(_translate("MainWindow", "🡆"))
        self.backbutton.setText(_translate("MainWindow", "🡄"))
