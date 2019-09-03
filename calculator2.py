
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon,QPixmap

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        Button7 = QPushButton('7',self)
        Button8 = QPushButton('8',self)
        Button9 = QPushButton('9',self)
        Button4 = QPushButton('4',self)
        Button5 = QPushButton('5',self)
        Button6 = QPushButton('6',self)
        Button1 = QPushButton('1',self)
        Button2 = QPushButton('2',self)
        Button3 = QPushButton('3',self)
        Button0 = QPushButton('0',self)
        ButtonDel = QPushButton('Del',self)
# Button0.resize(Button0.sizeHint(150,80)      
        Button7.move(20,53)
        Button8.move(100,53)
        Button9.move(180,53)
        Button4.move(20,83)
        Button5.move(100,83)
        Button6.move(180,83)
        Button1.move(20,113)
        Button2.move(100,113)
        Button3.move(180,113)
        Button0.move(20,143)
        ButtonDel.move(180,143)

        self.setWindowTitle('Calculator')
        self.setGeometry(300,300,300,200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
