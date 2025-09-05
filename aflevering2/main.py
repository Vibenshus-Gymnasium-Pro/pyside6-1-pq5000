from browser import Ui_MainWindow
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QToolButton, QSizePolicy, QSpacerItem,
    QWidget)

app = QApplication([])
window = QMainWindow()
ui = Ui_MainWindow()

openTabs = []


class tab():
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self._tab = QHBoxLayout()


    def deleteTab(self):
        print(f"Deleting tab with title {self.title} and url {self.url}")
        
        while self._tab.count():
            x = self._tab.takeAt(0)
            x.widget().setParent(None) 

        self._tab.setParent(None)
        openTabs.remove(self)
        print(f"Current tabs are open: {[i.title for i in openTabs]}")
    

    def addAsNew(self):
            self._tab.setSpacing(0)
            ui.tb1 = QToolButton(ui.horizontalLayoutWidget)
            ui.tb1.setMinimumSize(QSize(100, 0))
            ui.tb1.setCheckable(True)
            ui.tb1.setChecked(False)
            ui.tb1.setText(self.title)
            self._tab.addWidget(ui.tb1)
            self._tab.setAlignment(Qt.AlignmentFlag.AlignLeft)

            ui.tb2 = QToolButton(ui.horizontalLayoutWidget)
            ui.tb2.setObjectName(u"toolButton")
            ui.tb2.setText("x")
            self._tab.addWidget(ui.tb2)
            ui.horizontalLayout.addLayout(self._tab)

            ui.tb2.clicked.connect(self.deleteTab)

def addNewTab():
    print("Adding new tab...")
    _tab = tab("Google", "https://www.google.com")
    _tab.addAsNew()
    openTabs.append(_tab)

def gotoUrl():
    url = ui.lineEdit.text()
    if not url.startswith("http"):
        url = "http://" + url
    ui.webEngineView.setUrl(QUrl(url))
    print(f"Gone to url: {url}")
    ui.lineEdit.unsetCursor()

def setTopUrl():
    url = str(ui.webEngineView.url())
    ui.lineEdit.setText(str(url[21:url.__len__()-2]))

def bindUI():
    ui.lineEdit.setText("https://www.google.com/")
    ui.gotoURL_b.clicked.connect(gotoUrl)
    ui.lineEdit.returnPressed.connect(gotoUrl)

    ui.pushButton.clicked.connect(ui.webEngineView.back)
    ui.pushButton_2.clicked.connect(ui.webEngineView.forward)

    ui.pushButton_7.clicked.connect(ui.webEngineView.reload)

    ui.webEngineView.urlChanged.connect(setTopUrl)

    ui.newtab_b.clicked.connect(addNewTab)

    

def startBrowser():
    print("Starting browser...")
    ui.setupUi(window)
    window.show()
    bindUI()
    app.exec()

if __name__ == "__main__":
    startBrowser()
    