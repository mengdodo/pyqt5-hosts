# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, \
    QGridLayout, QTextEdit, QHBoxLayout, QVBoxLayout, QPushButton, \
    QLabel,QMessageBox
import os


class App(QWidget):

    hostsCode = ''

    def __init__(self):
        super().__init__()

        hostsCode = os.popen('sudo cat /private/etc/hosts')
        self.hostsCode = hostsCode.read()

        self.initUI()

    def initUI(self):
        # self.resize(800, 600) # 可拉伸的窗口大小
        self.setFixedSize(800, 400)  # 固定窗口大小

        self.center()

        self.setWindowTitle('host修改工具【MAC版】')

        # self.setStyleSheet("QLabel{background:#a9a9a9;padding-top:3px;padding-left:5px}")

        Message1 = '本工具是基于python3+pyqt5制作,简化传统的vim /private/etc/hosts编辑文件,快速修改MAC系统下的host文件,听起来是不是美滋滋。'
        label1 = QLabel(self)
        label1.setText(Message1)
        label1.setGeometry(10, 10, 780, 20)

        Message2 = '作者：Nemo'
        label2 = QLabel(self)
        label2.setText(Message2)
        label2.setGeometry(10, 30, 780, 20)

        Message3 = '格式：127.0.0.1       localhost'
        label3 = QLabel(self)
        label3.setText(Message3)
        label3.setGeometry(10, 50, 780, 20)

        Message4 = '邮箱：dodo@mengdodo.com'
        label4 = QLabel(self)
        label4.setText(Message4)
        label4.setGeometry(10, 70, 780, 20)

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        okButton.clicked.connect(self.savefile)
        cancelButton.clicked.connect(self.cancelButton)

        hbox = QHBoxLayout()  # 水平布局
        hbox.addStretch(0)    # 增加了一些弹性空间
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()  # 垂直布局
        vbox.addStretch(1)    # 增加了一些弹性空间

        self.reviewEdit = QTextEdit()
        self.reviewEdit.setText(self.hostsCode)

        grid = QGridLayout()
        grid.addWidget(self.reviewEdit, 9, 5, 1, 1)

        vbox.addLayout(grid)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.show()

    def savefile(self):
        hostsCode = self.reviewEdit.toPlainText()   #获取文本框内容
        f = open('/private/etc/hosts', 'w') # 若是'wb'就表示写二进制文件
        f.write(hostsCode)
        f.close()

        QMessageBox.about(self, "成功", "hosts文件修改成功")

    def cancelButton(self):
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
