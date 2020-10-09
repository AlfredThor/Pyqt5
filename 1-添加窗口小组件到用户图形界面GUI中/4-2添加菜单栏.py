import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('添加菜单栏2')
        self.statusBar().showMessage('文本状态栏')
        self.resize(400,300)

        # 创建一个菜单栏
        menu = self.menuBar()
        # 创建两个菜单
        file_menu = menu.addMenu('文件')
        file_menu.addSeparator()
        edit_menu = menu.addMenu('修改')

        # 创建一个行为
        new_action = QAction('新的文件',self)
        # 跟新状态栏文本
        new_action.setStatusTip('打开新的文件')
        # 添加一个行为到菜单
        file_menu.addAction(new_action)

        '''
        首先使用QAction()对象创建一个行为，然后使用setStatusTip()方法设置它的状态文本提示
        接着使用trigered.connect()方法调用关闭窗口的借口，再使用setShortcut()方法设置了
        行为快捷键，最后添加行为到菜单上
        '''
        # 创建退出行为
        exit_action = QAction('退出',self)
        # 退出操作
        exit_action.setStatusTip('点击退出应用程序')
        # 点击关闭程序
        exit_action.triggered.connect(self.close)
        # 设置退出快捷键
        exit_action.setShortcut('Ctrl+Q')
        # 添加退出行为到菜单上
        file_menu.addAction(exit_action)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())