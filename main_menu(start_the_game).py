import sys
from test_map import start_game, time
from PyQt5.QtWidgets import QApplication, QMainWindow
from design_main_menu import Ui_MainWindow


class Main_Menu(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_pygame)
        self.pushButton_3.clicked.connect(self._exit_of_window)

    def _exit_of_window(self):
        self.close()

    def start_pygame(self):
        self.close()
        if start_game(1):
            start_game(2)
        filename = f'{self.lineEdit.text()}.txt'
        result = open(filename, encoding='utf-8', mode='w')
        result.write(f'{self.lineEdit.text()} -- {time}')
        print(filename)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main_Menu()
    window.showFullScreen()
    sys.exit(app.exec_())
