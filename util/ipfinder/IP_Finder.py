import os
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("IPfind.ui")[0]

# ip 찾기
class MyWindow(QDialog, form_class):
    start_ip = None
    end_ip = None
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('at.ico'))
        self.pushButton.clicked.connect(self.start)
        self.buttonBox.rejected.connect(self.close_button)
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
            os.system('arp -a > .\\db\\ip.txt')
            found_ip = open('.\\db\\ip.txt', 'rt')
            lines = found_ip.readlines()
            del lines[0:3]
            for line in lines:
                devices = line.split()
                self.textBrowser.append(devices[0] + '    ' + devices[1].replace('-','.') + '    ' + devices[2])
                print(devices)
            self.textBrowser.append('검색을 완료 하였습니다.\n')
        else:
            self.textBrowser.append('IP가 입력되지 않았습니다.\n')
    def close_button(self):
        self.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
