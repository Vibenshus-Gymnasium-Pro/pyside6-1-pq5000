from PySide6.QtCore import Qt, QUrl, QRect, QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QToolButton, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from browser import Ui_MainWindow

app = QApplication([])
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

openTabs = []
currentTab = None

current_connections = []

class Tab:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        

        self.tab_container = QWidget()
        self._tab = QHBoxLayout(self.tab_container)
        self._tab.setContentsMargins(0, 0, 0, 0)
        
        self.webview = QWebEngineView()
        self.tb1 = None
        self.tb2 = None
    
    def deleteTab(self):
        global currentTab
        
        if self.webview:
            self.webview.urlChanged.disconnect()
        
        if self.tb1:
            self.tb1.clicked.disconnect()
        
        if self.tb2:
            self.tb2.clicked.disconnect()
        

        if self in openTabs:
            openTabs.remove(self)

        if self.webview:
            self.webview.hide()
            self.webview.setParent(None)
            self.webview.deleteLater()
        
        if self.tab_container:
            ui.horizontalLayout.removeWidget(self.tab_container)
            self.tab_container.setParent(None)
            self.tab_container.deleteLater()
        

        if currentTab == self:
            if openTabs:
                currentTab = openTabs[-1]
                currentTab.set_active()
            else:
                currentTab = None
                clearWebUI()
    
    def setTabName(self):
        if not self.webview or not self.tb1:
            return
            
        url_string = self.webview.url().toString()
        
        slashindexes = [i for i, x in enumerate(url_string) if x == "/"]
        
        start_idx = slashindexes[1]+1
        end_idx = slashindexes[2]

        cuturl = url_string[start_idx:end_idx]

        self.tb1.setText(cuturl)
    
    def addAsNew(self):
        self.tb1 = QToolButton()
        self.tb1.setMinimumSize(QSize(100, 0))
        self.tb1.setCheckable(True)
        self.tb1.setText(self.title)
        
        self.tb2 = QToolButton()
        self.tb2.setText("x")
        self.tb2.setMaximumSize(QSize(20, 20))
        
        self._tab.addWidget(self.tb1)
        self._tab.addWidget(self.tb2)
        self._tab.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        ui.horizontalLayout.addWidget(self.tab_container)
        

        self.tb1.clicked.connect(self.setActive)
        self.tb2.clicked.connect(self.deleteTab)
        

        self.webview.setParent(ui.centralwidget)
        self.webview.setGeometry(QRect(0, 80, 1071, 631))
        self.webview.setUrl(QUrl(self.url))
        self.webview.hide()
        self.webview.urlChanged.connect(self.setTabName)
    
    def setActive(self):
        global currentTab
        
        if currentTab and currentTab != self:
            currentTab.tb1.setChecked(False)
            currentTab.webview.hide()
        

        currentTab = self
        self.tb1.setChecked(True)
        self.webview.show()
        self.webview.raise_()
        ui.lineEdit.setText(self.webview.url().toString())
        bindWebUI()

def clearWebUI():
    global current_connections
    
    for connection in current_connections:
        try:
            connection.disconnect()
        except:
            pass  
    current_connections.clear()

def bindWebUI():

    global current_connections
    
    if not currentTab:
        clearWebUI()
        return
    

    clearWebUI()
    

    try:
        conn1 = ui.pushButton.clicked.connect(currentTab.webview.back)
        conn2 = ui.pushButton_2.clicked.connect(currentTab.webview.forward)
        conn3 = ui.pushButton_7.clicked.connect(currentTab.webview.reload)
        conn4 = currentTab.webview.urlChanged.connect(setTopUrl)
        
    except Exception as e:
        print(f"Error binding web UI: {e}")

def addNewTab():
    global currentTab
    print("Adding new tab...")
    
    new_tab = Tab("New Tab", "https://www.google.com")
    new_tab.addAsNew()
    openTabs.append(new_tab)
    new_tab.setActive()

def gotoUrl():
    if not currentTab:
        return
    
    url = ui.lineEdit.text().strip()
    if not url:
        return
        
    if not url.startswith("http"):
        url = "http://" + url
    
    try:
        currentTab.webview.setUrl(QUrl(url))
        print(f"Gone to url: {url}")
    except Exception as e:
        print(f"Error navigating to URL: {e}")

def setTopUrl():
    if currentTab and currentTab.webview:
        try:
            current_url = currentTab.webview.url().toString()
            ui.lineEdit.setText(current_url)
        except Exception as e:
            print(f"Error setting top URL: {e}")

def bindUI():
    ui.lineEdit.setText("https://www.google.com/")
    ui.gotoURL_b.clicked.connect(gotoUrl)
    ui.lineEdit.returnPressed.connect(gotoUrl)
    ui.newtab_b.clicked.connect(addNewTab)

def startBrowser():
    print("Starting browser...")
    window.show()
    bindUI()
    
    addNewTab()
    
    app.exec()

if __name__ == "__main__":
    startBrowser()
