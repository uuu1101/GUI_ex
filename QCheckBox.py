import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb1 = QCheckBox('CheckBox 1', self)
        cb1.move(20, 20)
        cb1.stateChanged.connect(self.changeStatusBar)

        cb2 = QCheckBox('CheckBox 2', self)
        cb2.move(20, 40)
        cb2.stateChanged.connect(self.changeStatusBar)

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeStatusBar(self, state):
        checked = self.sender()
        if checked.isChecked():
            self.statusBar().showMessage(checked.text())
        else:
            self.statusBar().clearMessage()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
