# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import multiprocessing
import subprocess
import sys
from datetime import datetime
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    ip = None
    ip2 = None
    ip3 = None
    ip4 = None
    setip = None
    filename = None
    filename2 = None
    name = None
    file = None
    installresult = None
    appfolder = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 595)
        MainWindow.setMinimumSize(QtCore.QSize(800, 595))
        MainWindow.setMaximumSize(QtCore.QSize(800, 595))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("db/at.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 331, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 230, 781, 311))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_5)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 751, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.Label = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.LineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.LineEdit.setEnabled(False)
        self.LineEdit.setText("")
        self.LineEdit.setReadOnly(True)
        self.LineEdit.setObjectName("LineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.LineEdit)
        self.Label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.LineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.LineEdit_2.setEnabled(False)
        self.LineEdit_2.setText("")
        self.LineEdit_2.setReadOnly(True)
        self.LineEdit_2.setObjectName("LineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.LineEdit_2)
        self.mACLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.mACLabel.setObjectName("mACLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.mACLabel)
        self.mACLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.mACLineEdit.setEnabled(False)
        self.mACLineEdit.setText("")
        self.mACLineEdit.setReadOnly(True)
        self.mACLineEdit.setObjectName("mACLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.mACLineEdit)
        self.Label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.LineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.LineEdit_3.setEnabled(False)
        self.LineEdit_3.setText("")
        self.LineEdit_3.setReadOnly(True)
        self.LineEdit_3.setObjectName("LineEdit_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.LineEdit_3)
        self.Label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.LineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.LineEdit_5.setEnabled(False)
        self.LineEdit_5.setReadOnly(True)
        self.LineEdit_5.setObjectName("LineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.LineEdit_5)
        self.configLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.configLabel.setObjectName("configLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.configLabel)
        self.configLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.configLineEdit.setEnabled(False)
        self.configLineEdit.setReadOnly(True)
        self.configLineEdit.setObjectName("configLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.configLineEdit)
        self.Label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.LineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.LineEdit_4.setEnabled(False)
        self.LineEdit_4.setText("")
        self.LineEdit_4.setReadOnly(True)
        self.LineEdit_4.setObjectName("LineEdit_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.LineEdit_4)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.toolBox_2 = QtWidgets.QToolBox(self.tab)
        self.toolBox_2.setGeometry(QtCore.QRect(10, 10, 751, 261))
        self.toolBox_2.setObjectName("toolBox_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 751, 201))
        self.page_3.setObjectName("page_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 170, 92, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.progressBar_4 = QtWidgets.QProgressBar(self.page_3)
        self.progressBar_4.setGeometry(QtCore.QRect(10, 170, 271, 23))
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_4.setObjectName("progressBar_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.page_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 10, 731, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setGeometry(QtCore.QRect(380, 170, 261, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_22 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_22.setEnabled(False)
        self.pushButton_22.setGeometry(QtCore.QRect(650, 170, 93, 21))
        self.pushButton_22.setObjectName("pushButton_22")
        self.toolBox_2.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_4.setObjectName("page_4")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.page_4)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 731, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_18 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_2.addWidget(self.pushButton_18)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.label_5 = QtWidgets.QLabel(self.page_4)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 721, 20))
        self.label_5.setObjectName("label_5")
        self.progressBar = QtWidgets.QProgressBar(self.page_4)
        self.progressBar.setGeometry(QtCore.QRect(10, 80, 731, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.toolBox_2.addItem(self.page_4, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 751, 148))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 3, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_2.addWidget(self.radioButton_5, 0, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 4, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_3, 2, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_2.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout_2.addWidget(self.radioButton_6, 0, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 3, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 3, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_8.setDragEnabled(False)
        self.lineEdit_8.setReadOnly(False)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 4, 1, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_15.setGeometry(QtCore.QRect(310, 180, 149, 23))
        self.pushButton_15.setObjectName("pushButton_15")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textEdit = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 751, 221))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 10, 295, 30))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_19 = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.pushButton_19.setEnabled(False)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_7.addWidget(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.pushButton_20.setEnabled(False)
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout_7.addWidget(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.pushButton_21.setEnabled(False)
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_7.addWidget(self.pushButton_21)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.toolBox = QtWidgets.QToolBox(self.tab_2)
        self.toolBox.setGeometry(QtCore.QRect(10, 20, 751, 261))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 751, 201))
        self.page.setObjectName("page")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 731, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 150, 731, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.progressBar_2 = QtWidgets.QProgressBar(self.horizontalLayoutWidget_5)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_5.addWidget(self.progressBar_2)
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 731, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.page)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_2.setObjectName("page_2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.page_2)
        self.progressBar_3.setGeometry(QtCore.QRect(10, 170, 731, 23))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 731, 43))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_7.setMaximumSize(QtCore.QSize(20, 16777215))
        self.radioButton_7.setText("")
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayout.addWidget(self.radioButton_7, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setEnabled(True)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 3, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_4.setMaximumSize(QtCore.QSize(70, 16777215))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 0, 2, 1, 1)
        self.radioButton_8 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_8.setMaximumSize(QtCore.QSize(75, 16777215))
        self.radioButton_8.setObjectName("radioButton_8")
        self.gridLayout.addWidget(self.radioButton_8, 0, 4, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 0, 5, 1, 1)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 731, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_6.addWidget(self.lineEdit_3)
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_6.addWidget(self.pushButton_12)
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 721, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.pushButton_13.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton_13.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_13.setObjectName("pushButton_13")
        self.toolBox.addItem(self.page_2, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 331, 141))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 311, 111))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_3.addWidget(self.radioButton, 1, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_3.addWidget(self.radioButton_3, 3, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_3.addWidget(self.radioButton_4, 4, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_3.addWidget(self.radioButton_2, 2, 0, 1, 1)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(30, 190, 295, 30))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_4.addWidget(self.pushButton_9)
        self.pushButton_14 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_4.addWidget(self.pushButton_14)
        self.pushButton_17 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_4.addWidget(self.pushButton_17)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(350, 40, 441, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 20, 421, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setPlaceholderText("")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(500, 190, 75, 23))
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(210, 540, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 590, 781, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(700, 810, 93, 28))
        self.pushButton_23.setObjectName("pushButton_23")
        self.tabWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.groupBox.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.groupBox_2.raise_()
        self.pushButton_16.raise_()
        self.label_9.raise_()
        self.textBrowser.raise_()
        self.pushButton_23.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_5 = QtWidgets.QMenu(self.menu)
        self.menu_5.setObjectName("menu_5")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menuSTP = QtWidgets.QMenu(self.menu_2)
        self.menuSTP.setObjectName("menuSTP")
        self.menu_4 = QtWidgets.QMenu(self.menu_2)
        self.menu_4.setObjectName("menu_4")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionTFTP = QtWidgets.QAction(MainWindow)
        self.actionTFTP.setObjectName("actionTFTP")
        self.actionIP_Finder = QtWidgets.QAction(MainWindow)
        self.actionIP_Finder.setObjectName("actionIP_Finder")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.actionMantis = QtWidgets.QAction(MainWindow)
        self.actionMantis.setObjectName("actionMantis")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.actionADB = QtWidgets.QAction(MainWindow)
        self.actionADB.setObjectName("actionADB")
        self.actionAIQP = QtWidgets.QAction(MainWindow)
        self.actionAIQP.setObjectName("actionAIQP")
        self.actionApp_Open = QtWidgets.QAction(MainWindow)
        self.actionApp_Open.setObjectName("actionApp_Open")
        self.actionLog_Open = QtWidgets.QAction(MainWindow)
        self.actionLog_Open.setObjectName("actionLog_Open")
        self.actionDB_Open = QtWidgets.QAction(MainWindow)
        self.actionDB_Open.setObjectName("actionDB_Open")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.actionVODCG = QtWidgets.QAction(MainWindow)
        self.actionVODCG.setObjectName("actionVODCG")
        self.actionEPG = QtWidgets.QAction(MainWindow)
        self.actionEPG.setObjectName("actionEPG")
        self.menu_5.addAction(self.actionVODCG)
        self.menu_5.addAction(self.actionEPG)
        self.menu.addAction(self.action)
        self.menu.addAction(self.actionTFTP)
        self.menu.addAction(self.menu_5.menuAction())
        self.menu.addAction(self.actionIP_Finder)
        self.menuSTP.addAction(self.action_5)
        self.menuSTP.addAction(self.action_6)
        self.menu_4.addAction(self.action_7)
        self.menu_4.addAction(self.action_8)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.actionMantis)
        self.menu_2.addAction(self.menuSTP.menuAction())
        self.menu_2.addAction(self.menu_4.menuAction())
        self.menu_3.addAction(self.actionADB)
        self.menu_3.addAction(self.actionAIQP)
        self.menuFile.addAction(self.actionApp_Open)
        self.menuFile.addAction(self.actionLog_Open)
        self.menuFile.addAction(self.action_4)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox_2.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Atnet IPTV QC Program"))
        self.label.setText(_translate("MainWindow", "IP "))
        self.lineEdit.setText(_translate("MainWindow", "192.168.219."))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.Label.setText(_translate("MainWindow", "모델"))
        self.Label_2.setText(_translate("MainWindow", "가입자번호"))
        self.mACLabel.setText(_translate("MainWindow", "MAC"))
        self.Label_3.setText(_translate("MainWindow", "펌웨어"))
        self.Label_5.setText(_translate("MainWindow", "SBC TYPE"))
        self.configLabel.setText(_translate("MainWindow", "Config버젼"))
        self.Label_4.setText(_translate("MainWindow", "부팅시간"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "단말 정보"))
        self.pushButton_2.setText(_translate("MainWindow", "저장"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "검색어를 입력해주세요."))
        self.pushButton_22.setText(_translate("MainWindow", "검색"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_3), _translate("MainWindow", "Logcat"))
        self.pushButton_3.setText(_translate("MainWindow", "Current"))
        self.pushButton_4.setText(_translate("MainWindow", "Anr"))
        self.pushButton_5.setText(_translate("MainWindow", "Tombstones"))
        self.pushButton_6.setText(_translate("MainWindow", "EPG"))
        self.pushButton_18.setText(_translate("MainWindow", "SDS"))
        self.pushButton_7.setText(_translate("MainWindow", "Menu Agent"))
        self.pushButton_8.setText(_translate("MainWindow", "PVS"))
        self.label_5.setText(_translate("MainWindow", "저장할 로그를 선택해 주세요."))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_4), _translate("MainWindow", "기타"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "로그저장"))
        self.label_8.setText(_translate("MainWindow", "Protocol"))
        self.lineEdit_5.setText(_translate("MainWindow", "192.168.219."))
        self.radioButton_5.setText(_translate("MainWindow", "Host"))
        self.label_16.setText(_translate("MainWindow", "Password"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "SSH2"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Telnet"))
        self.radioButton_6.setText(_translate("MainWindow", "직접입력"))
        self.label_15.setText(_translate("MainWindow", "Username"))
        self.lineEdit_7.setText(_translate("MainWindow", "root"))
        self.lineEdit_6.setText(_translate("MainWindow", "23"))
        self.label_7.setText(_translate("MainWindow", "Post"))
        self.lineEdit_8.setText(_translate("MainWindow", "qkdthdtpsxj!"))
        self.pushButton_15.setText(_translate("MainWindow", "Connect"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "원격접속"))
        self.pushButton_19.setText(_translate("MainWindow", "불러오기"))
        self.pushButton_20.setText(_translate("MainWindow", " 저장"))
        self.pushButton_21.setText(_translate("MainWindow", "내보내기"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Config변경"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "파일을 선택해 주세요."))
        self.pushButton_10.setText(_translate("MainWindow", "File"))
        self.label_2.setText(_translate("MainWindow", "설치할 파일을 선택하세요."))
        self.pushButton_11.setText(_translate("MainWindow", "Install"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "앱 인스톨"))
        self.label_4.setText(_translate("MainWindow", "목표 앱"))
        self.comboBox_4.setToolTip(
            _translate("MainWindow", "<html><head/><body><p>tvG는 직접 입력을 선택해 주세요.</p></body></html>"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "폴더선택"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "app"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "priv-app"))
        self.radioButton_8.setText(_translate("MainWindow", "직접 입력"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "폴더명 까지 입력해 주세요."))
        self.label_3.setText(_translate("MainWindow", "소스 앱"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "파일을 선택해 주세요."))
        self.pushButton_12.setText(_translate("MainWindow", "File"))
        self.label_6.setText(_translate("MainWindow", "소스 앱과 목표 앱을 선택해 주세요."))
        self.pushButton_13.setText(_translate("MainWindow", "Copy"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "앱 복사"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "앱 설치"))
        self.groupBox.setTitle(_translate("MainWindow", "ADB 연결 단말"))
        self.radioButton.setText(_translate("MainWindow", "None"))
        self.radioButton_3.setText(_translate("MainWindow", "None"))
        self.radioButton_4.setText(_translate("MainWindow", "None"))
        self.radioButton_2.setText(_translate("MainWindow", "None"))
        self.pushButton_9.setText(_translate("MainWindow", "Devices"))
        self.pushButton_14.setText(_translate("MainWindow", "Disconnect"))
        self.pushButton_17.setText(_translate("MainWindow", "Reboot"))
        self.groupBox_2.setTitle(_translate("MainWindow", "실행 내역"))
        self.pushButton_16.setText(_translate("MainWindow", "Clear"))
        self.label_9.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" color:#8b8b8b;\">Copyright 2018. LeeKyungYul(ATNET). all rights reserved.</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">   </span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">   AIQP정보</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   이 프로그램은 파이썬 3.6을 사용합니다.</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   AIQP는 Atnet IPTV QC Test를 위해서 제작 되었습니다.</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   작성자의 동의 없이<span style=\" color:#000000;\"> 무단 배포를 금지</span>합니다.</p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   제작일 : 2018년 1월 22일</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   작업내역 : ADB Script 및 원격접속</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   작성자 : 이경열(okyul25@gmail.com)</p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   버전 : 4.00.00</p></body></html>"))
        self.pushButton_23.setText(_translate("MainWindow", "닫기"))
        self.menu.setTitle(_translate("MainWindow", "도구"))
        self.menu_5.setTitle(_translate("MainWindow", "원격접속"))
        self.menu_2.setTitle(_translate("MainWindow", "사이트"))
        self.menuSTP.setTitle(_translate("MainWindow", "STP"))
        self.menu_4.setTitle(_translate("MainWindow", "테스트베드"))
        self.menu_3.setTitle(_translate("MainWindow", "도움말"))
        self.menuFile.setTitle(_translate("MainWindow", "파일"))
        self.action.setText(_translate("MainWindow", "파일 탐색기"))
        self.actionTFTP.setText(_translate("MainWindow", "TFTP"))
        self.actionIP_Finder.setText(_translate("MainWindow", "IP Finder"))
        self.action_3.setText(_translate("MainWindow", "에트넷"))
        self.actionMantis.setText(_translate("MainWindow", "Mantis"))
        self.action_5.setText(_translate("MainWindow", "가입자정보"))
        self.action_6.setText(_translate("MainWindow", "펌웨어배포"))
        self.action_7.setText(_translate("MainWindow", "가입자정보"))
        self.action_8.setText(_translate("MainWindow", "펌웨어배포"))
        self.actionADB.setText(_translate("MainWindow", "ADB 재시작"))
        self.actionAIQP.setText(_translate("MainWindow", "About AIQP..."))
        self.actionApp_Open.setText(_translate("MainWindow", "App 열기"))
        self.actionLog_Open.setText(_translate("MainWindow", "Log 열기"))
        self.actionDB_Open.setText(_translate("MainWindow", "DB Open"))
        self.action_4.setText(_translate("MainWindow", "끝내기"))
        self.actionVODCG.setText(_translate("MainWindow", "VODCG"))
        self.actionEPG.setText(_translate("MainWindow", "EPG"))
        subprocess.call('adb\\adb kill-server', shell=True)
        subprocess.call('adb\\adb start-server', shell=True)
        subprocess.call('adb\\adb disconnect', shell=True)
        subprocess.call('adb\\adb devices > db\\devices.txt', shell=True)
        self.threadClass = ThreadClass()
        self.utile = Util()
        self.logsave = LogSave()
# 파일
        self.actionApp_Open.triggered.connect(self.appFolderOpen)
        self.actionLog_Open.triggered.connect(self.logFolderOpen)
        self.action_4.triggered.connect(self.end)
# 사이트
        self.action_3.triggered.connect(self.atnetcom)
        self.actionMantis.triggered.connect(self.mantisbt)
        self.action_5.triggered.connect(self.stpwstb)
        self.action_6.triggered.connect(self.stpnms)
        self.action_7.triggered.connect(self.tbbwstb)
        self.action_8.triggered.connect(self.tbnms)
# 도구
        self.action.triggered.connect(self.explorer)
        self.actionTFTP.triggered.connect(self.tftpd)
        self.actionVODCG.triggered.connect(self.mstsc_vodcg)
        self.actionEPG.triggered.connect(self.mstsc_epg)
        self.actionIP_Finder.triggered.connect(self.ipfind)
# 도움말
        self.actionADB.triggered.connect(self.adbKill)
        self.actionAIQP.triggered.connect(self.programInfo)
        self.pushButton_23.clicked.connect(self.programInfoclose)
# 메인
        self.radioButton.clicked.connect(self.choice)
        self.radioButton_2.clicked.connect(self.choice)
        self.radioButton_3.clicked.connect(self.choice)
        self.radioButton_4.clicked.connect(self.choice)
        self.pushButton.clicked.connect(self.connect)
        self.pushButton_9.clicked.connect(self.devices)
        self.pushButton_14.clicked.connect(self.disconnect)
        self.pushButton_17.clicked.connect(self.reboot)
        self.pushButton_16.clicked.connect(self.textBrowser_2.clear)
#로그
        self.pushButton_2.clicked.connect(self.logcat)
        self.pushButton_3.clicked.connect(self.current)
        self.pushButton_4.clicked.connect(self.anr)
        self.pushButton_5.clicked.connect(self.tombstons)
        self.pushButton_6.clicked.connect(self.epg)
        self.pushButton_18.clicked.connect(self.sds)
        self.pushButton_7.clicked.connect(self.menuagent)
        self.pushButton_8.clicked.connect(self.pvs)
# app
        self.pushButton_10.clicked.connect(self.openFile)
        self.pushButton_11.clicked.connect(self.install)
        self.pushButton_12.clicked.connect(self.openFile2)
        self.pushButton_13.clicked.connect(self.copy)
        self.pushButton_15.clicked.connect(self.protocolConnect)
        self.pushButton_19.clicked.connect(self.pullConfig)
        self.pushButton_20.clicked.connect(self.saveConfig)
        self.pushButton_21.clicked.connect(self.pushConfig)
        self.pushButton_22.clicked.connect(self.search)
        self.buttonEnabled()
# init
    def init(self):
        self.label_5.setText('저장할 로그를 선택해 주세요.')
        self.progressBar.setValue(0)
        self.lineEdit_2.clear()
        self.label_2.setText('설치할 파일을 선택하세요.')
        self.progressBar_2.setValue(0)
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.label_6.setText('소스 앱과 목표 앱을 선택해 주세요.')
        self.progressBar_3.setValue(0)
        self.textEdit.clear()
        self.comboBox.clear()
        self.textBrowser_3.clear()
        ui.progressBar_4.setValue(0)
        self.lineEdit_9.clear()
# 버튼
    def buttonEnabled(self):
        if self.setip == None or self.setip == 'None':
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(False)
            self.pushButton_4.setEnabled(False)
            self.pushButton_5.setEnabled(False)
            self.pushButton_6.setEnabled(False)
            self.pushButton_7.setEnabled(False)
            self.pushButton_8.setEnabled(False)
            self.pushButton_10.setEnabled(False)
            self.pushButton_11.setEnabled(False)
            self.pushButton_12.setEnabled(False)
            self.pushButton_13.setEnabled(False)
            self.pushButton_14.setEnabled(False)
            self.pushButton_17.setEnabled(False)
            self.pushButton_18.setEnabled(False)
            self.pushButton_19.setEnabled(False)
            self.pushButton_20.setEnabled(False)
            self.pushButton_21.setEnabled(False)
            self.pushButton_22.setEnabled(False)
            self.LineEdit.setEnabled(False)
            self.LineEdit_2.setEnabled(False)
            self.mACLineEdit.setEnabled(False)
            self.LineEdit_3.setEnabled(False)
            self.configLineEdit.setEnabled(False)
            self.LineEdit_4.setEnabled(False)
            self.LineEdit_5.setEnabled(False)
            self.lineEdit_9.setEnabled(False)
            self.textEdit.setEnabled(False)
        else:
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.pushButton_5.setEnabled(True)
            self.pushButton_6.setEnabled(True)
            self.pushButton_7.setEnabled(True)
            self.pushButton_8.setEnabled(True)
            self.pushButton_10.setEnabled(True)
            self.pushButton_12.setEnabled(True)
            self.pushButton_14.setEnabled(True)
            self.pushButton_17.setEnabled(True)
            self.pushButton_18.setEnabled(True)
            self.pushButton_19.setEnabled(True)
            self.LineEdit.setEnabled(True)
            self.LineEdit_2.setEnabled(True)
            self.mACLineEdit.setEnabled(True)
            self.LineEdit_3.setEnabled(True)
            self.configLineEdit.setEnabled(True)
            self.LineEdit_4.setEnabled(True)
            self.LineEdit_5.setEnabled(True)
 # 도구
    def ipfind(self):
        subprocess.Popen('util\\ipfinder\\IPfind')
    def tftpd(self):
        subprocess.Popen('util\\tftpd\\tftpd32')
    def explorer(self):
        subprocess.Popen('explorer .\\')
    def mstsc_vodcg(self):
        subprocess.Popen('mstsc /admin /v:172.21.143.61')
    def mstsc_epg(self):
        subprocess.Popen('mstsc /admin /v:172.21.143.21')
# 사이트
    def atnetcom(self):
        subprocess.Popen('"C:\Program Files\Internet Explorer\iexplore.exe" http://182.215.78.238')
    def mantisbt(self):
        subprocess.Popen('"C:\Program Files\Internet Explorer\iexplore.exe" bugs.lguplustv.com/my_view_page.php')
    def tbbwstb(self):
        subprocess.Popen('"C:\Program Files\Internet Explorer\iexplore.exe" http://bwstb.mylgtv.com/stb/modsbc2.php')
    def tbnms(self):
        subprocess.Popen('"C:\Program Files\Internet Explorer\iexplore.exe" http://123.140.17.2')
    def stpwstb(self):
        subprocess.Popen('"C:\Program Files\Internet Explorer\iexplore.exe" http://182.223.73.142/stb/modsbc2.php')
    def stpnms(self):
        subprocess.Popen('"C:\Program Files\Internet Explorer\iexplore.exe" http://182.223.73.145/LGT_PVS')
# 파일
    def appFolderOpen(self):
        subprocess.call('explorer .\\app')
    def logFolderOpen(self):
        subprocess.call('explorer .\\log')
    def end(self):
        subprocess.call('adb\\adb kill-server', shell=True)
        MainWindow.close()
# 도움말
    def adbKill(self):
        result = QMessageBox.question(MainWindow, 'Logcat', 'ADB 서버를 재시작 하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            subprocess.call('adb\\adb kill-server', shell=True)
            subprocess.call('adb\\adb start-server', shell=True)
            subprocess.call('adb\\adb disconnect', shell=True)
            self.utile.times()
            self.textBrowser_2.append(self.utile.nowDatetime + '     ADB를 재시작 하였습니다.')
            self.devices()
        else:
            self.utile.imes()
            self.textBrowser_2.append(self.nutile.owDatetime + '     ADB를 재시작을 취소하였습니다.')
    def programInfo(self):
        MainWindow.resize(800, 900)
        MainWindow.setMinimumSize(QtCore.QSize(800, 900))
        MainWindow.setMaximumSize(QtCore.QSize(800, 900))
    def programInfoclose(self):
        MainWindow.resize(800, 595)
        MainWindow.setMinimumSize(QtCore.QSize(800, 595))
        MainWindow.setMaximumSize(QtCore.QSize(800, 595))
# device connect
    def connect(self):
        print('connect start...')
        ui.setip = self.setip
        self.setip = self.lineEdit.text()
        print(self.setip)
        if self.setip != '192.168.219.':
            QMessageBox.information(MainWindow, "AIQP", '%s 연결을 진행합니다.\n잠시만 기달려 주세요.' % self.setip)
            subprocess.call('adb\\adb connect %s > db\\connect.txt' % (self.setip), shell=True)
            f = open('db\\connect.txt', 'rt', encoding='utf-8')
            lines = f.readlines()
            for line in lines:
                QtWidgets.QMessageBox.information(MainWindow, "AIQP", line)
            connectresult = line[:12]
            print(connectresult)
            if connectresult == 'connected to':
                self.utile.times()
                self.textBrowser_2.append(self.utile.nowDatetime + '     %s     연결을 성공 하였습니다.' % self.setip)
                self.remount()
                self.devices()
                self.choice()
                self.utile.times()
            elif connectresult == 'already conn':
                pass
            else:
                self.utile.times()
                self.textBrowser_2.append(self.utile.nowDatetime + '     %s     연결을 실패 하였습니다.' % self.setip)
        else:
            QtWidgets.QMessageBox.critical(MainWindow, "AIQP", "IP를 입력해 주세요.")
        print('connect end')
        print('-----------------------------------------------------------------------------------------------------')
# disconnect
    def disconnect(self):
        print('disconnect start...')
        self.choice()
        if self.setip == None or self.setip == 'None':
            QtWidgets.QMessageBox.critical(MainWindow, "AIQP", "단말을 선택해 주세요.")
        else:
            subprocess.call('adb\\adb disconnect %s:5555 > db\\disconnect.txt' % self.setip, shell=True)
            self.utile.times()
            self.textBrowser_2.append(self.utile.nowDatetime + '     %s     연결을 해제 하였습니다.' % self.setip)
            self.devices()
        print('disconnect end')
        print('-----------------------------------------------------------------------------------------------------')
 # reboot
    def reboot(self):
        print('reboot start...')
        self.choice()
        if self.setip == None or self.setip == 'None':
            QtWidgets.QMessageBox.critical(MainWindow, "AIQP", "단말을 선택해 주세요.")
        else:
            QMessageBox.information(MainWindow, "AIQP", '%s 리부팅을 진행합니다.\n잠시만 기달려 주세요.' % self.setip)
            subprocess.call('adb\\adb -s %s:5555 reboot' % self.setip, shell=True)
            self.utile.times()
            self.textBrowser_2.append(self.utile.nowDatetime + '     %s     리부팅 하였습니다.' % self.setip)
            self.devices()
        print('reboot end')
        print('-----------------------------------------------------------------------------------------------------')
#단말선택
    def choice(self):
        subprocess.call('adb\\adb devices > db\\devices.txt', shell=True)
        if self.radioButton.isChecked():
            self.setip = self.ip
        elif self.radioButton_2.isChecked():
            self.setip = self.ip2
        elif self.radioButton_3.isChecked():
            self.setip = self.ip3
        elif self.radioButton_4.isChecked():
            self.setip = self.ip4
        else:
            self.setip = None
        print(self.setip)
        self.buttonEnabled()
        self.modelInfo()
        self.init()
        self.comboBox_4.currentIndexChanged.connect(self.applist)
#리마운트 실행
    def remount(self):
        print('remount start...')
        subprocess.Popen('adb\\adb -s %s:5555 root' % self.setip, shell=True)
        subprocess.call('adb\\adb -s %s:5555 remount > db\\remount.txt' % self.setip, shell=True)
        f = open('db\\remount.txt', 'rt')
        remount = f.readline()
        if remount == 'remount succeeded\n':
            self.utile.times()
            self.textBrowser_2.append(self.utile.nowDatetime + '     %s     remount를 성공 하였습니다.' % self.setip)
            pass
        else:
            QMessageBox.warning(MainWindow, self.setip, "단말이 remount되지 않았습니다.\n기능 사용에 문제가 발생시 단말을 리부팅 후 다시 연결해 주세요.")
            self.utile.times()
            self.textBrowser_2.append(self.utile.nowDatetime + '     %s     remount를 실패 하였습니다.' % self.setip)
            subprocess.call('adb\\adb connect %s > db\\connect.txt' % (self.setip), shell=True)
        print('remount end')
#devices 실행
    def devices(self):
        print('devices start...')
        subprocess.call('adb\\adb devices > db\\devices.txt', shell=True)
        QMessageBox.information(MainWindow, "AIQP", "단말 연결 리스트를 갱신하였습니다.")
        self.ip_show()
        print('devices end')
#IP 출력
    def ip_show(self):
        print('ip_show start...')
        self.ip = 'None'
        self.ip2 = 'None'
        self.ip3 = 'None'
        self.ip4 = 'None'
        f = open('db\\devices.txt', 'rt')
        ips = f.readlines()
        if len(ips) >= 3:
            self.ip = ips[1].split(':')[0]
            print(self.ip)
        if len(ips) >= 4:
            self.ip2 = ips[2].split(':')[0]
            print(self.ip2)
        if len(ips) >= 5:
            self.ip3 = ips[3].split(':')[0]
            print(self.ip3)
        if len(ips) >= 6:
            self.ip4 = ips[4].split(':')[0]
            print(self.ip4)
        if self.ip == '':
            self.label.setText('연결된 단말이 없습니다.')
        else:
            self.radioButton.setText(self.ip)
        self.radioButton_2.setText(self.ip2)
        self.radioButton_3.setText(self.ip3)
        self.radioButton_4.setText(self.ip4)
        self.comboBox_2.clear()
        self.comboBox_2.addItem(self.ip)
        self.comboBox_2.addItem(self.ip2)
        self.comboBox_2.addItem(self.ip3)
        self.comboBox_2.addItem(self.ip4)
# 단말정보
    def modelInfo(self):
        if self.setip == None or self.setip == 'None':
            self.LineEdit.setText(None)
            self.LineEdit_2.setText(None)
            self.mACLineEdit.setText(None)
            self.LineEdit_3.setText(None)
            self.configLineEdit.setText(None)
            self.LineEdit_4.setText(None)
            self.LineEdit_5.setText(None)
        else:
            print('modelInfo start....')
            try:
                subprocess.call('adb\\adb -s %s:5555 pull /LGU_conf/config.xml db\\config.txt' % (self.setip), shell=True)
                f = open('db\\config.txt', 'rt', encoding='utf-8')
                lines = f.readlines()
                model = lines[2].split()
                model = model[2]
                model = model[7:-2]
                f.close()
                subprocess.call('del db\\config.txt', shell=True)
            except:
                model = None
            try:
                subprocess.call('adb\\adb -s %s:5555 shell cat /LGU_data/UP/SUBSCRIBER_NUMBER.0 > db\\member.txt' % (self.setip), shell=True)
                f = open('db\\member.txt', 'rt', encoding='utf-8')
                member = f.readlines()
                member = member[0]
                count = len(member)
                if count == 12:
                    pass
                else:
                    member = None
            except:
                member = None
            try:
                subprocess.call('adb\\adb -s %s:5555 shell cat /LGU_data/UP/MACADDRESS.0 > db\\MAC.txt' % (self.setip), shell=True)
                f = open('db\\MAC.txt', 'rt', encoding='utf-8')
                mac = f.readlines()
                mac = mac[0]
                count = len(mac)
                if count == 14:
                    pass
                else:
                    mac = None
            except:
                mac = None
            try:
                subprocess.call('adb\\adb -s %s:5555 shell cat /LGU_data/UP/FW_VERSION.0 > db\\FW.txt' % (self.setip), shell=True)
                f = open('db\\FW.txt', 'rt', encoding='utf-8')
                fw = f.readlines()
                fw = fw[0]
                count = len(fw)
                print(count)
                if count == 22:
                    pass
                else:
                    fw = None
            except:
                fw = None
            try:
                subprocess.call('adb\\adb -s %s:5555 shell cat /LGU_data/UP/SBC_TYPE.0 > db\\SBC.txt' % (self.setip), shell=True)
                f = open('db\\SBC.txt', 'rt', encoding='utf-8')
                sbc = f.readlines()
                sbc = sbc[0]
                count = len(sbc)
                print(sbc)
                if count <= 5:
                    pass
                else:
                    sbc = None
            except:
                sbc = None
            try:
                subprocess.call('adb\\adb -s %s:5555 shell cat /LGU_data/UP/CONF_CONFIG_VERSION.0 > db\\configv.txt' % (self.setip), shell=True)
                f = open('db\\configv.txt', 'rt', encoding='utf-8')
                config = f.readlines()
                config = config[0]
                count = len(config)
                print(config)
                if count == 4:
                    pass
                else:
                    config = None
            except:
                config = None
            try:
                subprocess.call('adb\\adb -s %s:5555 shell uptime > db\\uptime.txt' % (self.setip), shell=True)
                f = open('db\\uptime.txt', 'rt', encoding='utf-8')
                uptime = f.readlines()
                uptime = uptime[0]
                uptime = uptime[1:]
                f.close()
                subprocess.call('del db\\uptime.txt', shell=True)
            except:
                uptime = None
            self.LineEdit.setText(model)
            self.LineEdit_2.setText(member)
            self.mACLineEdit.setText(mac)
            self.LineEdit_3.setText(fw)
            self.configLineEdit.setText(config)
            self.LineEdit_4.setText(uptime)
            self.LineEdit_5.setText(sbc)
    def logcat(self):
        print('Logcat start...')
        self.textBrowser_3.clear()
        ui.progressBar_4.setValue(0)
        try:
            QMessageBox.information(MainWindow, 'AIQP', "Logcat 저장을 시작합니다.\n잠시만 기달려 주세요.")
            subprocess.call('adb\\adb -s %s:5555 logcat -d -v threadtime > ./log/logcat/logcat_%s.txt' % (self.setip, self.setip), shell=True, timeout=10)
            ui.progressBar_4.setValue(80)
            try:
                print(self.setip)
                f = open('log\\logcat\\logcat_%s.txt' % (self.setip), 'rt', encoding='utf-8')
                lines = f.readlines()
                for line in lines:
                    line = line.rstrip('\n')
                    self.textBrowser_3.append(line)
                f.close()
                self.textEdit.append('')
                ui.progressBar_4.setValue(100)
                QMessageBox.information(MainWindow, 'AIQP', "Logcat 저장을 성공하였습니다.")
                self.utile.times()
                self.textBrowser_2.append(self.utile.nowDatetime + '     %s     Logcat 파일을 저장하였습니다.' % self.setip)
                self.lineEdit_9.setEnabled(True)
                self.pushButton_22.setEnabled(True)
            except:
                f.close()
                self.textBrowser_2.append(self.utile.nowDatetime + '     %s     Logcat 저장을 성공하였습니다.' % self.setip)
                QMessageBox.warning(MainWindow, "AIQP", "Logcat 저장을 성공하였으나 불러오기를 실패하였습니다.\n문제가 계속 발생시에는 adb 다시 연결해 주세요.")
                ui.progressBar_4.setValue(0)
        except:
            self.textBrowser_2.append(self.utile.nowDatetime + '     %s     Logcat 파일을 실패 하였습니다.' % self.setip)
            QMessageBox.warning(MainWindow, "AIQP", "Logcat 저장을 실패하였습니다.")
            self.devices()
            ui.progressBar_4.setValue(0)
        print('logcat end')
        print('-----------------------------------------------------------------------------------------------------')
    def search(self):
        self.textBrowser_3.clear()
        search = self.lineEdit_9.text()
        f = open('log\\logcat\\logcat_%s.txt' % self.setip, 'rt', encoding='utf-8')
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            result = line.find(search)
            if result == -1:
                pass
            else:
                self.textBrowser_3.append(line)
# 로그저장 > current
    def current(self):
        print('current start...')
        self.name = 'Current'
        self.label_5.setText('%s 저장 준비 중...' % self.name)
        f = open('db\\log.txt', 'wt')
        f.close()
        self.runing = '0'
        QMessageBox.information(MainWindow, 'AIQP', "%s Current 저장을 시작합니다.\n잠시만 기달려 주세요." % self.setip)
        self.threadClass.start()
        self.label_5.setText('%s 압축 중...' % self.name)
        subprocess.call('adb\\adb -s %s:5555 shell busybox  tar -cvf /tmp/Current.tar /LGU_data/logs/current' % (self.setip), shell=True)
        self.label_5.setText('%s 저장 중...' % self.name)
        subprocess.Popen('adb\\adb -s %s:5555 pull /tmp/Current.tar ./log/current/current_%s.tar > db\\log.txt' % (self.setip, self.setip), shell=True)
 # 로그저장 > anr
    def anr(self):
        print('anr start...')
        self.name = 'Anr'
        self.label_5.setText('%s 저장 준비 중...' % self.name)
        f = open('db\\log.txt', 'wt')
        f.close()
        self.runing = '0'
        QMessageBox.information(MainWindow, 'AIQP', "%s Anr 저장을 시작합니다.\n잠시만 기달려 주세요." % self.setip)
        self.threadClass.start()
        self.label_5.setText('%s 압축 중...' % self.name)
        subprocess.call('adb\\adb -s %s:5555 shell busybox  tar -cvf /tmp/Anr.tar /data/anr' % (self.setip), shell=True)
        self.label_5.setText('%s 저장 중...' % self.name)
        subprocess.Popen('adb\\adb -s %s:5555 pull /tmp/Anr.tar ./log/anr/anr_%s.tar > db\\log.txt' % (self.setip, self.setip), shell=True)
# 로그저장 > tombstons
    def tombstons(self):
        print('tombstons start...')
        self.name = 'Tombstones'
        self.label_5.setText('%s 저장 준비 중...' % self.name)
        f = open('db\\log.txt', 'wt')
        f.close()
        self.runing = '0'
        QMessageBox.information(MainWindow, self.setip, "Tombstons 저장을 시작합니다.\n잠시만 기달려 주세요.")
        self.threadClass.start()
        self.label_5.setText('%s 압축 중...' % self.name)
        subprocess.call('adb\\adb -s %s:5555 shell busybox  tar -cvf /tmp/Tombstones.tar /data/tombstones' % (self.setip), shell=True)
        self.label_5.setText('%s 저장 중...' % self.name)
        subprocess.Popen('adb\\adb -s %s:5555 pull /tmp/Tombstones.tar ./log/tombstones/tombstones__%s.tar > db\\log.txt' % (self.setip, self.setip), shell=True)
# 로그저장 > epg
    def epg(self):
        print('epg start...')
        self.name = 'epg'
        self.label_5.setText('%s 저장 준비 중...' % self.name)
        f = open('db\\log.txt', 'wt')
        f.close()
        self.runing = '0'
        QMessageBox.information(MainWindow, self.setip, "EPG 저장을 시작합니다.\n잠시만 기달려 주세요.")
        self.threadClass.start()
        self.label_5.setText('%s 압축 중...' % self.name)
        subprocess.call('adb\\adb -s %s:5555 shell busybox  tar -cvf /tmp/epg.tar /data/data/com.lguplus.iptv3.base.si.provider/databases' % (self.setip), shell=True)
        self.label_5.setText('%s 저장 중...' % self.name)
        subprocess.Popen('adb\\adb -s %s:5555 pull /tmp/epg.tar ./log/epg_sds/epgdb_%s.tar > db\\log.txt' % (self.setip, self.setip), shell=True)
# 로그저장 > sds
    def sds(self):
        print('sds start...')
        self.name = 'sds'
        self.label_5.setText('%s 저장 준비 중...' % self.name)
        f = open('db\\log.txt', 'wt')
        f.close()
        self.runing = '0'
        QMessageBox.information(MainWindow, self.setip, "SDS 저장을 시작합니다.\n잠시만 기달려 주세요.")
        self.threadClass.start()
        self.label_5.setText('%s 압축 중...' % self.name)
        subprocess.call('adb\\adb -s %s:5555 shell busybox  tar -cvf /tmp/sds.tar /LGU_data/sds' % (self.setip), shell=True)
        self.label_5.setText('%s 저장 중...' % self.name)
        subprocess.Popen('adb\\adb -s %s:5555 pull /tmp/sds.tar ./log/epg_sds/sds_%s.tar > db\\log.txt' % (self.setip, self.setip), shell=True)
# 로그저장 > menuagent
    def menuagent(self):
        print('Menuagent start...')
        self.name = 'Menuagent'
        self.label_5.setText('%s 저장 준비 중...' % self.name)
        f = open('db\\log.txt', 'wt')
        f.close()
        self.runing = '0'
        self.choice()
        QMessageBox.information(MainWindow, self.setip, "Menuagent 저장을 시작합니다.\n잠시만 기달려 주세요.")
        self.threadClass.start()
        self.label_5.setText('%s 압축 중...' % self.name)
        subprocess.call('adb\\adb -s %s:5555 shell busybox  tar -cvf /tmp/Menuagent.tar /LGU_data/ma' % (self.setip), shell=True)
        self.label_5.setText('%s 저장 중...' % self.name)
        subprocess.Popen('adb\\adb -s %s:5555 pull /tmp/Menuagent.tar ./log/menuagent/menuagent_%s.tar > db\\log.txt' % (self.setip, self.setip), shell=True)
# 로그저장 > pvs
    def pvs(self):
        print('PVS start...')
        self.name = 'PVS'
        self.label_5.setText('%s 저장 준비 중...' % self.name)
        f = open('db\\log.txt', 'wt')
        f.close()
        self.runing = '0'
        self.choice()
        QMessageBox.information(MainWindow, self.setip, "PVS 저장을 시작합니다.\n잠시만 기달려 주세요.")
        self.threadClass.start()
        self.label_5.setText('%s 압축 중...' % self.name)
        subprocess.call('adb\\adb -s %s:5555 shell busybox  tar -cvf /tmp/PVS.tar /LGU_data/pvs' % (self.setip), shell=True)
        self.label_5.setText('%s 저장 중...' % self.name)
        subprocess.Popen('adb\\adb -s %s:5555 pull /tmp/PVS.tar ./log/pvs/pvs%s.tar > db\\log.txt' % (self.setip, self.setip), shell=True)
# log 결과
    def logResult(self):
        endline = []
        self.utile.times()
        # self.textBrowser.clear()
        f = open('db\\log.txt', 'rt', encoding='utf-8')
        lines = f.readlines()
        for line in lines:
            endline.append(line)
        copyresult = endline[len(endline) - 1]
        if copyresult[1:5] == '100%':
            self.label_5.setText('%s 저장을 성공 하였습니다.' % (self.name))
            self.utile.times()
            self.textBrowser_2.append(self.utile.nowDatetime + '     %s     %s 파일을 저장하였습니다.' % (self.setip, self.name))
        else:
            self.label_5.setText('%s 저장을 실패 하였습니다.' % (self.name))
            self.utile.times()
            self.textBrowser_2.append(self.utile.nowDatetime + '     %s     %s 파일을 저장을 실패 하였습니다.' % (self.setip, self.name))
# config 불러오기
    def pullConfig(self):
        try:
            self.textEdit.setEnabled(True)
            self.textEdit.clear()
            subprocess.call('adb\\adb -s %s:5555 pull /LGU_conf/config.xml db\\config_%s.txt' % (self.setip, self.setip), shell=True)
            f = open('db\\config_%s.txt' % self.setip, 'rt', encoding='utf-8')
            lines = f.readlines()
            model = lines[2].split()
            model = model[2]
            model = model[7:-2]
            print(model)
            for line in lines:
                line = line.rstrip('\n')
                self.textEdit.append(line)
            self.textEdit.append('')
            QMessageBox.information(MainWindow, 'AIQP', "%s Config 파일을 불러왔습니다." % self.setip)
            self.pushButton_20.setEnabled(True)
        except:
            self.textEdit.setEnabled(False)
            QMessageBox.information(MainWindow, 'AIQP', "%s Config 파일을 불러오기를 실패하였습니다." % self.setip)
# config 저장하기
    def saveConfig(self):
        mytext = self.textEdit.toPlainText()
        with open('db\\config_%s.txt' % self.setip, 'wt') as f:
            f.write(mytext)
        f.close()
        QMessageBox.information(MainWindow, 'AIQP', "Config 파일을 저장하였습니다.")
        self.pushButton_21.setEnabled(True)
# config 내보내기
    def pushConfig(self):
        result = QMessageBox.question(MainWindow, 'AIQP', '%s Cinfig 변경을 진행하시겠습니까?' % self.setip, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            subprocess.call('adb\\adb -s %s:5555 push db\\config_%s.txt /LGU_conf/config.xml' % (self.setip, self.setip), shell=True)
            QMessageBox.information(MainWindow, 'AIQP', '%s Config 파일을 변경하였습니다.' % self.setip)
            subprocess.call('del db\\config_%s.txt' % (self.setip), shell=True)
            self.textEdit.clear()
            self.pushButton_20.setEnabled(False)
            self.pushButton_21.setEnabled(False)
            self.textEdit.setEnabled(False)
        else:
            QMessageBox.critical(MainWindow, 'AIQP', '%s Cinfig 변경을 취소하였습니다.' % self.setip)
# 파일 선택
    def openFile(self):
        lineedit = self.lineEdit_2
        button = self.pushButton_11
        self.utile.open(lineedit, button)
    def openFile2(self):
        lineedit = self.lineEdit_3
        button = self.pushButton_13
        self.utile.open(lineedit, button)
#app install
    def install(self):
        print(self.filename[0])
        f = open('db\\log.txt', 'wt')
        f.close()
        self.runing = '0'
        self.choice()
        print('b')
        print('adb\\adb -s %s:5555 install -r -d %s > db\\log.txt' % (self.setip, self.filename[0]))
        QMessageBox.information(MainWindow, self.setip, "%s인스톨을 시작합니다.\n잠시만 기달려 주세요." % (self.filename[0]))
        self.threadClass.start()
        self.label_2.setText('설치 중...')
        subprocess.Popen('adb\\adb -s %s:5555 install -r -d ./app/%s > db\\log.txt' % (self.setip, self.file), shell=True)
# app install result
    def install_Result(self, file, selectlist):
        print('인스톨 확인 시작...')
        if self.installresult == 'Success':
            self.label_2.setText('%s 설치를 성공 하였습니다.' % (selectlist))
            self.filename = None
            self.lineEdit_2.clear()
        else:
            self.label_2.setText('%s 설치를 실패 하였습니다.' % (selectlist))
            self.filename = None
            self.lineEdit_2.clear()
# app copy
    def applist(self):
        self.comboBox.clear()
        self.appfolder = self.comboBox_4.currentText()
        if self.appfolder != '폴더선택':
            print(self.appfolder)
            subprocess.call('adb\\adb -s %s:5555 shell ls /system/%s > db\\%s_app_list.txt' % (self.setip, self.appfolder, self.appfolder), shell=True)
            f = open('db\\%s_app_list.txt' % self.appfolder, 'rt', encoding = 'utf-8')
            lines = f.readlines()
            self.list = lines[::2]
            for line in self.list:
                line = line.replace('\n','')
                self.comboBox.addItem(line)
        else:
            self.comboBox.clear()
    def copy(self):
        f = open('db\\log.txt', 'wt')
        f.close()
        self.runing = '0'
        self.choice()
        if self.radioButton_7.isChecked():
            self.app2 = '/system/%s/%s/%s.apk' % (self.filename, self.comboBox.currentText())
            self.copying()
        elif self.radioButton_8.isChecked():
            self.app2 = self.lineEdit_4.text()
            self.copying()
        else:
            result = QMessageBox.question(MainWindow, 'AIQP', 'name 변경 없이 %s 복사를 진행하시겠습니까?'% self.filename2[0], QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result == QMessageBox.Yes:
                self.threadClass.start()
                self.label_6.setText('복사 중...')
                subprocess.Popen('adb\\adb -s %s:5555 push %s /system/app/%s > db\\log.txt' % (self.setip, self.filename2[0], self.filename2[0]), shell=True)
            else:
                QMessageBox.critical(MainWindow, 'AIQP', '%s 복사을 취소하였습니다.' % self.filename2[0])
    def copying(self):
        QMessageBox.information(MainWindow, 'AIQT', "%s 복사를 시작합니다.\n잠시만 기달려 주세요." % self.filename2[0])
        self.threadClass.start()
        subprocess.Popen('adb\\adb -s %s:5555 push %s %s > db\\log.txt' % (self.setip, self.filename2[0], self.app2), shell=True)
        self.label_2.setText('복사 중...')
    def copy_Result(self, file, selectlist):
        print('복사 확인 시작...')
        endline = []
        f = open('db\\log.txt', 'rt', encoding = 'utf-8')
        lines = f.readlines()
        for line in lines:
            endline.append(line)
        epg_menu_result = endline[len(endline) - 1]
        print(epg_menu_result[1:5])
        if epg_menu_result[1:5] == '100%':
            self.label_6.setText('%s 복사를 성공 하였습니다.' % (selectlist))
            self.filename2 = None
            self.lineEdit_3.clear()
        else:
            self.label_6.setText('%s 복사를 실패 하였습니다.' % (selectlist))
            self.filename2 = None
            self.lineEdit_3.clear()
    def protocolConnect(self):
        port = self.lineEdit_6.text()
        protocol = self.comboBox_3.currentText()
        user = self.lineEdit_7.text()
        password = self.lineEdit_8.text()
        if self.radioButton_5.isChecked():
            setip = self.comboBox_2.currentText()
        elif self.radioButton_6.isChecked():
            setip = self.lineEdit_5.text()
        else:
            QMessageBox.information(MainWindow, 'AIQP', 'IP를 입력해 주세요.')
        pc = ProtocolConnect(setip, port, protocol, user, password)
        QMessageBox.information(MainWindow, 'AIQP', '%s 단말에 %s로 원격접속을 시작합니다.' % (setip, protocol))
        pc.connect()

class LogSave:
# 로그저장 > logcat
    def logcat(self):
        self.setip = ui.setip
        print('Logcat start...')
        ui.progressBar.setValue(0)
        try:
            ui.label_5.setText('Logcat 저장 중...')
            QMessageBox.information(MainWindow, 'AIQP', "%s Logcat 저장을 시작합니다.\n잠시만 기달려 주세요." % self.setip)
            subprocess.call('adb\\adb -s %s:5555 logcat -d -v threadtime > ./log/logcat/logcat_%s.txt' % (self.setip, self.setip), shell=True, timeout=20)
            ui.progressBar.setValue(100)
            ui.label_5.setText('Logcat 파일 저장을 완료하였습니다.')
            ui.utile.times()
            ui.textBrowser.append(ui.utile.nowDatetime + '     %s     Logcat 파일을 저장하였습니다.' % self.setip)
        except:
            ui.label_5.setText('Logcat 파일 저장을 실패하였습니다.')
            QMessageBox.warning(MainWindow, "AIQP", "%s Logcat 저장을 실패하였습니다.\n단말 연결을 확인해 주세요." % self.setip)
        print('reboot end')
        print('-----------------------------------------------------------------------------------------------------')
    # 로그저장 > current
    def current(self):
        self.setip = ui.setip
        print('current start...')
        self.name = 'Current'
        ui.name = self.name
        ui.label_5.setText('%s 저장 준비 중...' % self.name)
        f = open('db\\log.txt', 'wt')
        f.close()
        ui.runing = '0'
        QMessageBox.information(MainWindow, 'AIQP', "%s Current 저장을 시작합니다.\n잠시만 기달려 주세요." % self.setip)
        ui.threadClass.start()
        ui.label_5.setText('%s 압축 중...' % self.name)
        subprocess.call('adb\\adb -s %s:5555 shell busybox  tar -cvf /tmp/Current.tar /LGU_data/logs/current' % (self.setip), shell=True)
        ui.label_5.setText('%s 저장 중...' % self.name)
        subprocess.Popen('adb\\adb -s %s:5555 pull /tmp/Current.tar ./log/current/current_%s.tar > db\\log.txt' % (self.setip, self.setip), shell=True)

class ProtocolConnect:
    def __init__(self, setip, port, protocol, user, password):
        self.setip = setip
        self.port = port
        self.protocol = protocol
        self.user = user
        self.password = password
    def connect(self):
        if self.protocol == 'Telnet':
            subprocess.Popen('"C:\Program Files\VanDyke Software\SecureCRT\SecureCRT.exe" telnet://%s' % self.setip)
        else:
            subprocess.Popen('"C:\Program Files\VanDyke Software\SecureCRT\SecureCRT.exe" /ssh2 %s /P %s /L %s /Password %s' % (self.setip, self.port, self.user, self.password))

class Util():
    # 시간구하기
    def times(self):
        now = datetime.now()
        self.nowDatetime = now.strftime('%Y-%m-%d %H:%M')
    #Mac 찾기
    def mac_show(self, ip):
        print('mac_show start...')
        subprocess.call('arp -a %s > db\\ipdevice.txt' % ip, shell=True)
        found_ip = open('db\\ipdevice.txt', 'rt')
        lines = found_ip.readlines()
        print(lines)
        devices_info = lines[3].split()
        m = devices_info[1]
        m = m.replace('-', '')
        mac = m[0:4] + '.' + m[4:8] + '.' + m[8:]
        print('mac_show end')
        return mac
    # 파일 선택
    def open(self, lineedit, button):
        print('openFile start...')
        lineedit.clear()
        self.filename = QFileDialog.getOpenFileName(MainWindow, 'OpenFile', './app')
        self.file = self.filename[0].split('/')[-1]
        extension = self.file.split('.')[-1]
        if extension:
            if extension == 'apk':
                ui.filename = self.filename
                ui.file = self.file
                lineedit.setText(self.filename[0])
                button.setEnabled(True)
            else:
                QMessageBox.critical(MainWindow, "AIQP", "파일을 잘못 선택 하셨습니다.\napk파일을 선택해 주세요.")
        else:
            QMessageBox.critical(MainWindow, "AIQP", "파일 선택을 취소하였습니다.")
        print(self.file)
        print(extension)

class ThreadClass(QtCore.QThread):
    def __init__(self):
        super().__init__()
    def run(self):
        self.setip = ui.setip
        self.name = ui.name
        self.file = ui.file
        self.filename = ui.filename
        self.filename2 = ui.filename2
        if self.filename2:
            self.appCopy()
        elif self.filename:
            self.app()
        else:
            self.log()
    def log(self):
        try:
            self.runing = '0'
            while True:
                if self.runing != '100':
                    f = open('db\\log.txt', 'rt', encoding='utf-8')
                    lines = f.readlines()
                    for line in lines:
                        self.runing = line[1:4]
                        self.runing = self.runing.replace(" ", "")
                    print(self.runing)
                    ui.progressBar.setValue(int(self.runing))
                else:
                    break
            ui.label_5.setText('%s 삭제 중...' % self.name)
            subprocess.call('adb\\adb -s %s:5555 shell rm /tmp/%s.tar' % (self.setip, self.name), shell=True)
            print('%s end' % self.name)
            print('-----------------------------------------------------------------------------------------------------')
        except:
            pass
        ui.logResult()
    def app(self):
        try:
            self.runing = '0'
            while True:
                if self.runing != '100' :
                    f = open('db\\log.txt', 'rt', encoding='utf-8')
                    lines = f.readlines()
                    for line in lines:
                        self.runing = line[1:4]
                        self.runing = self.runing.replace(" ", "")
                    print(self.runing)
                    ui.progressBar_2.setValue(int(self.runing))
                else:
                    installresult = None
                    endline = []
                    ui.label_2.setText('설치 확인 중... 잠시만 기달려 주세요...')
                    while True:
                        if installresult == 'Success':
                            ui.installresult = installresult
                            break
                        elif installresult == 'Failure':
                            break
                        else:
                            f = open('db\\log.txt', 'rt', encoding='utf-8')
                            lines = f.readlines()
                            for line in lines:
                                endline.append(line)
                            installresult = endline[-2]
                            installresult = installresult[0:7]
                            print(installresult)
                    break
            print(self.filename[0])
        except:
            print('-----------------------------------------------------------------------------------------------------')
            pass
        ui.install_Result('app_install', self.file)
    def appCopy(self):
        try:
            self.runing = '0'


            print('-----------------------------------------------------------------------------------------------------')
        except:
            pass
        ui.copy_Result('app_install', self.file)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())