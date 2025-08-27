from browser_test import Ui_MainWindow
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

app = QApplication([])
window = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(window)

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


ui.lineEdit.setText("https://www.google.com/")
ui.pushButton_4.clicked.connect(gotoUrl)
ui.lineEdit.returnPressed.connect(gotoUrl)

ui.pushButton.clicked.connect(ui.webEngineView.back)
ui.pushButton_2.clicked.connect(ui.webEngineView.forward)

ui.pushButton_7.clicked.connect(ui.webEngineView.reload)

ui.webEngineView.urlChanged.connect(setTopUrl)


window.show()
app.exec()