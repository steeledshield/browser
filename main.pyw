from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class MyWebBrowser():

    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle("SteeledSurf")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        self.refresh_btn = QPushButton("R")
        self.refresh_btn.setMinimumHeight(30)

        self.home_btn = QPushButton("H")
        self.home_btn.setMinimumHeight(30)

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.refresh_btn)
        self.horizontal.addWidget(self.home_btn)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)

        self.browser = QWebEngineView()

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.home_btn.clicked.connect(lambda: self.navigate_home(self.url_bar.toPlainText()))
        self.refresh_btn.clicked.connect(self.browser.reload)

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http" and "file"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

    def navigate_home(self, url):
        url = "http://www.google.com"
        self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

app = QApplication([])
window = MyWebBrowser()
app.exec_()