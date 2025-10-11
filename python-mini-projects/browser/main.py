from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys


# main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
    
        # create a QWebEngineView widget
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)

        self.showMaximized()

        navbar = QToolBar()
        navbar.adjustSize()
        self.addToolBar(navbar)

        # add a back button
        back_btn = QAction("⮜", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # forward button
        forward_btn = QAction("⮞", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # reload button
        reload_btn = QAction("⟳", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # add a url bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.open_url)
        navbar.addWidget(self.url_bar)

        # update url bar when browser url changes
        self.browser.urlChanged.connect(self.update_url)

    def open_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))


    def update_url(self, q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName("My Own Browser")
window = MainWindow()
app.exec_()