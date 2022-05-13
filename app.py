import os
import sys
from ctypes import windll
from time import sleep

from PIL import Image, ImageGrab
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from aip import AipOcr

from Ui_ocrui import Ui_MainWindow

# from configDialog import Ui_Dialog #暂时未使用

APP_ID = '19105187'  # APP_ID
API_KEY = 'IywiicFEKa5ny2ckUp29tHVk'  # API_KEY
SECRET_KEY = 'uWnu44pu6lFjPZylFLMBymurGNTtrD2t'  # SECRET_KEY
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        dpi = self.screen().logicalDotsPerInch() / 96
        self.setupUi(self)
        font_size = 14 if dpi <= 1 else (12 if 1 < dpi <= 1.25 else (10 if 1.25 < dpi <= 1.5 else 8))
        self.setStyleSheet(f'font-family: "Microsoft YaHei", Calibri, Ubuntu; font-size: {font_size}pt;')
        self.resize(1050, 600)
        self.text = ""
        self.strTime = ""
        self.basicid = ""
        self.filePath = ""

    def loadImage(self):
        self.filePath, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '图像文件(*.png *.jpg *.jpeg)')
        self.jpg = QtGui.QPixmap(self.filePath).scaled(self.plabel.width(), self.plabel.height())
        self.plabel.setPixmap(self.jpg)

    def loadcopyImage(self):
        self.filePath = './1.jpg'
        index = 0
        im = ImageGrab.grabclipboard()
        while not im:
            if index < 500:
                im = ImageGrab.grabclipboard()
                sleep(0.01)
                index = index + 1
            else:
                break
        if isinstance(im, Image.Image):
            im.save(self.filePath)
        self.jpg = QtGui.QPixmap(self.filePath).scaled(self.plabel.width(), self.plabel.height())
        self.plabel.setPixmap(self.jpg)

    def recognize(self):
        if (self.filePath == ""):
            print(QMessageBox.warning(self, "错误", "没有找到图片", QMessageBox.Yes, QMessageBox.Yes))
            return

        result = aipOcr.basicAccurate(self.get_file_content(self.filePath), options)
        words_result = result['words_result']
        for i in range(len(words_result)):
            self.text = self.text + words_result[i]['words'] + '\n'

        self.tedit.setPlainText(self.text)
        self.tedit.repaint()  # 解决mac端文本无法显示的问题

        self.text = ''

    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def cleanText(self):
        self.tedit.repaint()  # 解决mac端文本无法显示的问题

    def configApi(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
