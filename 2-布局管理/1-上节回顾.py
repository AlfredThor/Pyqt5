import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QLabel

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('上节回顾，菜单栏和任务栏')
        self.resize(400,300)
        self.add_menu_and_statu()
        # self.add_position_layout()
        self.show()

    # 添加菜单栏和状态栏
    def add_menu_and_statu(self):
        self.statusBar().showMessage('文本状态栏')
        # 创建一个菜单栏
        menu = self.menuBar()
        # 创建两个菜单
        file_menu = menu.addMenu('文件')
        file_menu.addSeparator()
        edit_menu = menu.addMenu('修改')

        # 创建一个行为
        new_action = QAction('新的文件',self)
        # 更新状态栏文本
        new_action.setStatusTip('打开新的文件')
        # 天剑一个行为到菜单
        file_menu.addAction(new_action)

        # 创建退出行为
        exit_action = QAction('退出',self)
        # 退出操作
        exit_action.setStatusTip('点击退出应用程序')
        # 点击关闭程序
        exit_action.triggered.connect(self.close)
        # 设置快捷退出键
        exit_action.setShortcut('Ctrl+Q')
        # 添加退出行为到菜单上
        file_menu.addAction(exit_action)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec())