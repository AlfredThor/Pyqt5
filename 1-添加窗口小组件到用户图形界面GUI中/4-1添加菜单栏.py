import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction

'''
我们在上一个程序的基础上，使用了menuBar()方法创建了一个菜单栏，
同时在菜单栏中添加了一个 '文件' 菜单，在这个基础上，通过Qaction模块
创建了一个行为new_action，在 '文件' 菜单中添加了这个行为。这个行为
的动作就是设置状态栏的文本
'''
class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('添加菜单栏')
        self.statusBar().showMessage('文本状态栏')
        self.resize(400,300)

        # 创建一个菜单栏
        menu = self.menuBar()
        # 创建一个菜单
        file_menu = menu.addMenu('文件')
        # 创建一个行为
        new_action = QAction('新文件',self)
        # 添加一个行为到菜单
        file_menu.addAction(new_action)

        # 更新状态栏文本
        new_action.setStatusTip('新的文件')

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())