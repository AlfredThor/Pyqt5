import sys
from PyQt5.QtWidgets import QMainWindow,QApplication

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('添加状态栏')
        self.resize(400,300)

        # 设置状态消息栏文本
        self.statusBar().showMessage('文本状态栏')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())