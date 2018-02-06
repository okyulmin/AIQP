# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IPfind.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(392, 331)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("at.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(270, 290, 121, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 120, 351, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 331, 131))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 351, 71))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 40, 101, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 101, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 101, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(240, 40, 101, 21))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.close)
        self.pushButton.clicked.connect(self.start)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "IP Finder"))
        self.groupBox_2.setTitle(_translate("Dialog", "사용 중인 IP 정보"))
        self.groupBox.setTitle(_translate("Dialog", "정보 입력"))
        self.lineEdit_2.setText(_translate("Dialog", "192.168.219.255"))
        self.label.setText(_translate("Dialog", "시작 IP 입력"))
        self.label_2.setText(_translate("Dialog", "마지막 IP 입력"))
        self.lineEdit.setText(_translate("Dialog", "192.168.219.1"))
        self.pushButton.setText(_translate("Dialog", "시작"))

    def start(self):
        self.start_ip = self.lineEdit.text()
        self.end_ip = self.lineEdit_2.text()
        if self.start_ip != '192.168.219.' or self.end_ip != '192.168.219.':
            start_third = int(self.start_ip[8:11])
            start_last = int(self.start_ip[12:])
            print(start_third, start_last)
            start_end = int(self.end_ip[12:])
            print(start_end)
            while start_last < start_end:
                result = os.system('ping -n 1 -w 1 192.168.%s.%s' % (start_third, start_last))
                if result == 0:
                    print('192.168.%s.%s' % (start_third, start_last))
                start_last += 1
            os.system('arp -a > db\\ip.txt')
            found_ip = open('db\\ip.txt', 'rt')
            lines = found_ip.readlines()
            del lines[0:3]
            for line in lines:
                devices = line.split()
                self.textBrowser.append(devices[0] + '    ' + devices[1].replace('-','.') + '    ' + devices[2])
                print(line)
            self.textBrowser.append('검색을 완료 하였습니다.\n')
        else:
            self.textBrowser.append('IP가 입력되지 않았습니다.\n')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

