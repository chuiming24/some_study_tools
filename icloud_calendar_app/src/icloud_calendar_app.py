from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QGridLayout


class FullWeb(object):
    def __init__(self):
        self.browser = QWebEngineView()
        self.javascript_array = []

    def setup_ui(self, main_window):
        grid = QGridLayout()
        main_window.setLayout(grid)
        self.browser = QWebEngineView()
        self.browser.load(QUrl("https://www.icloud.com/#calendar"))
        grid.addWidget(self.browser)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    from sys import argv, exit
    app = QApplication(argv)
    frame = QWidget()
    full_web = FullWeb()
    full_web.setup_ui(frame)
    frame.resize(1280, 720)
    frame.setWindowTitle('TT24KUN自用的icloud日历')
    frame.show()
    exit(app.exec_())

