import sys
from view.view import Ui_MainWindow
from PyQt5 import QtWidgets
from model.language_request import LanguageRequest
from model.html_formatter import HtmlFormatter


class Controller(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    controller connects view gui and model logic

    :author: Benjamin Bulis
    :version: V1.0
    """

    language_requester = LanguageRequest()
    html_formatter = HtmlFormatter()

    def check_language(self):
        """
        checks language and connects to the language service

        :return: no return value
        """
        input = self.ui.inputField.toPlainText()
        json_result = self.language_requester.language(input)
        html_result = self.html_formatter.formatter(json_result)
        self.display_output(html_result)

    def display_output(self, output: str):
        """
        it displays output to the output field

        :param output: output string
        :return:
        """
        self.ui.outputField.clear()
        self.ui.outputField.append(output)

    def __init__(self):
        """
        init methode starts gui
        """
        super().__init__(None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.checkButton.clicked.connect(self.check_language)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windows = Controller()
    windows.show()
    sys.exit(app.exec_())