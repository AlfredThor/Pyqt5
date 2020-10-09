import sys
from PyQt5.QtWidgets import QApplication,QWidget

'''
除了使用原生的类，我们还能从pyqt5中继承一些模块，以此来获得相关模块的属性。
比如我们创建一个继承与QWidget()的类，那么它就拥有了QWidget()的方法和属性，
这样我们就可以不实例化一个QWidget()对象而直接拥有QWidget()的属性
'''
# 继承来自QWidget
class Gui(QWidget):
    def __init__(self):
        # 实例化super类，用于创建窗口
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在类中继承')
        # QWidget类的方法，用于设置窗口大小
        self.resize(400,100)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())