# Sample PyQT application from RealPython.com

import sys
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QLabel,
    QMainWindow,
    QMenu,
    QSpinBox,
    QToolBar,
)
from PyQt5.QtGui import (
    QIcon,
    QKeySequence,
)

import qrc_resources


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle("Python Menus & Toolbars")
        self.resize(400, 200)
        self.centralWidget = QLabel("Hello, World")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self._createActions()
        self._createMenuBar()
        self._createToolBars()
        # self._createContextMenu()
        self._connectActions()

    def _createActions(self):
        # Creating action using the first constructor
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        self.newAction.setIcon(QIcon(":file-new.svg"))
        # Creating actions using the second constructor
        self.openAction = QAction(QIcon(":file-open.svg"), "&Open...", self)
        self.saveAction = QAction(QIcon(":file-save.svg"), "&Save", self)
        self.exitAction = QAction("&Exit", self)
        self.copyAction = QAction(QIcon(":edit-copy.svg"), "&Copy", self)
        self.pasteAction = QAction(QIcon(":edit-paste.svg"), "&Paste", self)
        self.cutAction = QAction(QIcon(":edit-cut.svg"), "C&ut", self)

        #TODO: Check on the Help Menu title to see why the word 'Help' is not showing
        self.helpContentAction = QAction("&Help Content", self)

        self.aboutAction = QAction("&About", self)

    def _createContextMenu(self):
        self.centralWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.centralWidget.addAction(self.newAction)
        self.centralWidget.addAction(self.openAction)
        self.centralWidget.addAction(self.saveAction)
        self.centralWidget.addAction(self.copyAction)
        self.centralWidget.addAction(self.pasteAction)
        self.centralWidget.addAction(self.cutAction)

    def _createMenuBar(self):
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        # Add a separator before Exit
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)

        editMenu = menuBar.addMenu("&Edit")
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
        editMenu.addSeparator()

        # Find and Replace submenu in the edit menu after a separator
        findMenu = editMenu.addMenu("Find and Replace")
        findMenu.addAction("Find...")
        findMenu.addAction("Replace...")

        helpMenu = menuBar.addMenu(QIcon(":help-content.svg"), "&Help")
        helpMenu.addAction(self.helpContentAction)
        helpMenu.addAction(self.aboutAction)

    def _createToolBars(self):
        # File Toolbar
        fileToolBar = self.addToolBar("File")
        fileToolBar.setMovable(False)
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)
        # Edit Toolbar
        editToolBar = QToolBar("Edit", self)
        self.addToolBar(editToolBar)
        editToolBar.addAction(self.copyAction)
        editToolBar.addAction(self.pasteAction)
        editToolBar.addAction(self.cutAction)
        editToolBar.addSeparator()
        self.fontSizeSpinBox = QSpinBox()
        self.fontSizeSpinBox.setFocusPolicy(Qt.NoFocus)
        editToolBar.addWidget(self.fontSizeSpinBox)

        # commented out this section for the Help Toolbar
        # Using a QToolBar object and a toolbar area
        # helpToolBar = QToolBar("Help", self)
        # self.addToolBar(Qt.LeftToolBarArea, helpToolBar)

    def contextMenuEvent(self, event):
        #  Create a menu object with the central widget as parent
        menu = QMenu(self.centralWidget)
        #Populate the menu with actions
        menu.addAction(self.newAction)
        menu.addAction(self.openAction)
        menu.addAction(self.saveAction)
        # add a separator between the file actions and edit actions
        separator = QAction(self)
        separator.setSeparator(True)
        menu.addAction(separator)
        menu.addAction(self.copyAction)
        menu.addAction(self.pasteAction)
        menu.addAction(self.cutAction)
        # Launch the menu
        menu.exec(event.globalPos())

    def newFile(self):
        self.centralWidget.setText("<b>File > New</b> clicked")

    def openFile(self):
        self.centralWidget.setText("<b>File > Open...</b> clicked")

    def saveFile(self):
        self.centralWidget.setText("<b>File > Save</b> clicked")

    def copyContent(self):
        self.centralWidget.setText("<b>Edit > Copy</b> clicked")

    def pasteContent(self):
        self.centralWidget.setText("<b>Edit > Past</b> clicked")

    def cutContent(self):
        self.centralWidget.setText("<b>Edit > Cut</b> clicked")

    def helpContent(self):
        self.centralWidget.setText("<b>Help > Help Content...</b> clicked")

    def about(self):
        self.centralWidget.setText("<b>Help > About...</b> clicked")

    def _connectActions(self):
        # Connect File Actions
        self.newAction.triggered.connect(self.newFile)
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.exitAction.triggered.connect(self.close)

        # Connect Edit Actions
        self.copyAction.triggered.connect(self.copyContent)
        self.pasteAction.triggered.connect(self.pasteContent)
        self.cutAction.triggered.connect(self.cutContent)

        # Connect Help Actions
        self.helpContentAction.triggered.connect(self.helpContent)
        self.aboutAction.triggered.connect(self.about)

if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    # Create and show the main window
    win = Window()
    win.show()
    #  Run the event loop
    sys.exit(app.exec())
