import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle("PyQt5验证")
    win.resize(300,150)
    label = QLabel("PyQt5 安装成功！", win)
    label.move(80,50)
    win.show()
    sys.exit(app.exec_())
