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