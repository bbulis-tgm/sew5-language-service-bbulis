import sys
from view.view import Ui_MainWindow
from PyQt5 import QtWidgets
from model.language_request import LanguageRequest


class Controller(QtWidgets.QMainWindow, Ui_MainWindow):
    """

    :author: Benjamin Bulis
    :version: V1.0
    """
    pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windows = Controller()
    windows.show()
    sys.exit(app.exec_())