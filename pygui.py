import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class GUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('窗口')
        self.statusBar().showMessage("文本栏状态")
        self.resize(400,300)
        self.add_menu_and_statu()
        self.grid_layout()

    def add_menu_and_statu(self):
        self.statusBar().showMessage("文本状态栏")
        #创建一个菜单栏
        menu = self.menuBar()
        #创建一个菜单
        file_menu = menu.addMenu("文件")
        #file_menu.addSepprator()
        edit_menu = menu.addMenu("修改")

        #创建一个行为
        new_action = QAction('新的文件',self)
        #更新状态栏文本
        new_action.setStatusTip('打开新的文件')
        # 添加一个行为到菜单
        file_menu.addAction(new_action)

        #创建退出行为
        exit_action = QAction('退出',self)
        #退出操作
        exit_action.setStatusTip("点击退出应用程序")
        #点击关闭程序
        exit_action.triggered.connect(self.close)
        #设置退出快捷键
        exit_action.setShortcut('Ctrl+Q')
        #添加退出行为到菜单上
        file_menu.addAction(exit_action)

    def grid_layout(self):

        #创建两个标签
        label_1 = QLabel("第一个标签",self)
        label_2 = QLabel("第二个标签",self)

        #创建两个按钮
        button_1 = QPushButton("按钮1",self)
        button_2 = QPushButton("按钮2",self)

        #创建一个网格布局对象
        grid_layout = QGridLayout()

        #在网格中添加窗口部件
        grid_layout.addWidget(label_1,0,0)#放置在0行0列
        grid_layout.addWidget(button_1,0,1)#放置在0行1列
        grid_layout.addWidget(label_2,1,0)#放置在1行0咧
        grid_layout.addWidget(button_2,1,1)#放置在1行1列

        grid_layout.setAlignment(Qt.AlignTop)#顶部对齐

        #创建窗一个窗口对象
        layout_widget = QWidget()
        layout_widget.setLayout(grid_layout)
        self.setCentralWidget(layout_widget)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUi()
    gui.show()
    sys.exit(app.exec_())

