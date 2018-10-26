# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-4, -1, 401, 261))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.dial = QtWidgets.QDial(self.tab)
        self.dial.setGeometry(QtCore.QRect(150, 70, 91, 71))
        self.dial.setObjectName("dial")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menu)
        self.menu_3.setObjectName("menu_3")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionxinwenjian = QtWidgets.QAction(MainWindow)
        self.actionxinwenjian.setObjectName("actionxinwenjian")
        self.actiontuichu = QtWidgets.QAction(MainWindow)
        self.actiontuichu.setObjectName("actiontuichu")
        self.actionzcd1 = QtWidgets.QAction(MainWindow)
        self.actionzcd1.setObjectName("actionzcd1")
        self.menu_3.addAction(self.actionzcd1)
        self.menu.addAction(self.actionxinwenjian)
        self.menu.addAction(self.actiontuichu)
        self.menu.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.actiontuichu.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "测试"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_3.setTitle(_translate("MainWindow", "子菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "修改"))
        self.actionxinwenjian.setText(_translate("MainWindow", "新文件"))
        self.actiontuichu.setText(_translate("MainWindow", "退出"))
        self.actiontuichu.setStatusTip(_translate("MainWindow", "点击退出应用程序"))
        self.actiontuichu.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionzcd1.setText(_translate("MainWindow", "子菜单1"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())