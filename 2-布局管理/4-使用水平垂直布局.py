'''
在前面的程序中，我们使用部件的move()方法来指定部件的位置，虽然很灵活，
但是如果部件很多的话，就会很繁琐。
Pyqt5提供了布局管理模块来支持部件的水平布局和垂直布局
QHBoxLayout:水平布局
QVBoxLayout:垂直布局
'''
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QWidget

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('使用水平垂直布局')
        self.move(600,600)
        self.show()
        self.add_menu_and_status()
        self.horizontal_vertical_box_layout()


    # 添加菜单栏和状态栏
    def add_menu_and_status(self):
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

    # 水平垂直布局
    def horizontal_vertical_box_layout(self):
        # 两个标签
        label_1 = QLabel('第一个标签')
        label_2 = QLabel('第二个标签')

        # 两个按钮
        button_1 = QPushButton('第一个按钮')
        button_2 = QPushButton('第二个按钮')

        # 创建两个水平盒子
        hbox_1 = QHBoxLayout()
        hbox_2 = QHBoxLayout()

        # 在水平盒子1中添加一个标签和一个按钮
        hbox_1.addWidget(label_1)
        hbox_1.addWidget(button_1)

        # 在水平盒子2中添加标签2和按钮2
        hbox_2.addWidget(label_2)
        hbox_2.addWidget(button_2)

        # 创建一个垂直盒子，包含两个水平盒子
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)

        # 创建一个窗口部件，设置布局为垂直盒子
        layout_widget = QWidget()
        layout_widget.setLayout(vbox)

        self.setCentralWidget(layout_widget)

if __name__ == '__main__':
    '''
    我们在horizontal_vertical_box_layout()方法中创建了一个窗口部件、一个垂直盒子、两个
    水平盒子、两个按钮和两个文本标签，分别进行了嵌套
    '''
    app = QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())