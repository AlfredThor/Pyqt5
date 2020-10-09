import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QLabel

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('添加Label标签部件')
        self.resize(400,300)
        self.add_menu_and_statu()
        # self.add_position_layout()
        self.add_position_layouts()
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

        # 创建爱你一个行为
        new_action = QAction('新的文件',self)
        # 更新状态栏文本
        new_action.setStatusTip('打开新的文件')
        # 添加一个行为到菜单
        file_menu.addAction(new_action)

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

    # 添加布局控件
    def add_position_layout(self):
        label = QLabel('第一个标签',self)
        label.move(10,20)

    '''
    手动设置的移动高度很不灵活，我们可以先获取菜单栏的高度，再确定label标签移动的位置
    我们可以使用部件的size()方法获取部件的宽和高，使用height()方法获取部件的高度，使用
    width()方法获取到部件的宽度
    '''
    def add_position_layouts(self):
        # 获取菜单栏的高度
        mbar_height = self.menuBar().height()
        # 第一个标签
        label1 = QLabel('第一个标签',self)
        label1.move(10,mbar_height)
        # 第二个标签
        label2 = QLabel('第二个标签',self)
        label2.move(10,mbar_height*2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec())