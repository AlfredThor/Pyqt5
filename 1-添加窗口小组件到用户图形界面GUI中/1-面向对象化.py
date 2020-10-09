import sys
from PyQt5.QtWidgets import QApplication,QWidget

'''
创建一个名为Gui的类，通过initUI()方法来创建窗口，并在初始化方法init()中调用它
'''
class Gui:
    def __init__(self):
        self.initUI()

    def initUI(self):
        self.win = QWidget()
        self.win.setWindowTitle('Pyqt5教程')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    gui.win.show()
    sys.exit(app.exec_())