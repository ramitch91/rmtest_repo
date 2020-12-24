# Sample PyQT application from RealPython.com

import sys
from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QIcon,
    QKeySequence,
)
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QLabel,
    QMainWindow,
    QMenu,
    QSpinBox,
    QToolBar,
)


# NOTE: Uncomment this import to enable icons
import qrc_resources


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.setWindowTitle("Python Menus & Toolbars")
        self.resize(800, 400)
        self.centralWidget = QLabel("Hello, World")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
        self._createActions()
        self._createMenuBar()
        self._createToolBars()
        self._createStatusBar()

        # Uncomment the call to ._createContextMenu() below to create a context
        # menu using menu policies. To test this out, you also need to comment
        # out .contextMenuEvent() and uncomment ._createContextMenu()
        # self._createContextMenu()

        self._connectActions()

    def _createActions(self):
        # File Actions
        # Create actions using the first constructor
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        self.newAction.setIcon(QIcon(":file-new.svg"))

        # Creating actions using the second constructor
        self.openAction = QAction(QIcon(":file-open.svg"), "&Open...", self)
        self.saveAction = QAction(QIcon(":file-save.svg"), "&Save", self)
        self.exitAction = QAction("&Exit", self)

        # Shortcut keys for the file items
        self.newAction.setShortcut("Ctrl+N")
        self.openAction.setShortcut("Ctrl+O")
        self.saveAction.setShortcut("Ctrl+S")

        # Adding help tips
        newTip = "Create a new file"
        self.newAction.setStatusTip(newTip)
        self.newAction.setToolTip(newTip)
        openTip = "Open an existing file"
        self.openAction.setStatusTip(openTip)
        self.openAction.setToolTip(openTip)
        saveTip = "Save current file"
        self.saveAction.setStatusTip(saveTip)
        self.saveAction.setToolTip(saveTip)
        exitTip = "Exit program"
        self.exitAction.setStatusTip(exitTip)
        self.exitAction.setToolTip(exitTip)

        # Edit Actions
        self.copyAction = QAction(QIcon(":edit-copy.svg"), "&Copy", self)
        self.pasteAction = QAction(QIcon(":edit-paste.svg"), "&Paste", self)
        self.cutAction = QAction(QIcon(":edit-cut.svg"), "C&ut", self)
        self.findAction = QAction("F&ind", self)
        self.replaceAction = QAction("&Replace", self)

        # Adding help tips
        copyTip = "Copy content"
        self.copyAction.setStatusTip(copyTip)
        self.copyAction.setToolTip(copyTip)
        pasteTip = "Paste content"
        self.pasteAction.setStatusTip(pasteTip)
        self.pasteAction.setToolTip(pasteTip)
        cutTip = "Cut content"
        self.cutAction.setStatusTip(cutTip)
        self.cutAction.setToolTip(cutTip)
        findTip = "Find content"
        self.findAction.setStatusTip(findTip)
        self.findAction.setToolTip(findTip)
        replaceTip = "Replace content"
        self.replaceAction.setStatusTip(replaceTip)
        self.replaceAction.setToolTip(replaceTip)

        # Shortcut keys for the edit items (using standard keys)
        self.copyAction.setShortcut(QKeySequence.Copy)
        self.pasteAction.setShortcut(QKeySequence.Paste)
        self.cutAction.setShortcut(QKeySequence.Cut)

        # TODO: Check on the Help Menu title to see why the word 'Help' is not showing
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
        self.centralWidget.addAction(self.findAction)
        self.centralWidget.addAction(self.replaceAction)

    def _createMenuBar(self):
        menuBar = self.menuBar()

        # Creating menus using a QMenu object
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        self.openRecentMenu = fileMenu.addMenu("Open Recent")
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
        findMenu.addAction(self.findAction)
        findMenu.addAction(self.replaceAction)

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

        # Add separator between edit functions and the widgets
        editToolBar.addSeparator()

        # Widgets
        self.fontSizeSpinBox = QSpinBox()
        self.fontSizeSpinBox.setFocusPolicy(Qt.NoFocus)
        editToolBar.addWidget(self.fontSizeSpinBox)

        # commented out this section for the Help Toolbar
        # Using a QToolBar object and a toolbar area
        # helpToolBar = QToolBar("Help", self)
        # self.addToolBar(Qt.LeftToolBarArea, helpToolBar)

    def contextMenuEvent(self, event):
        # Create a menu object with the central widget as parent
        menu = QMenu(self.centralWidget)

        # Populate the menu with actions
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

    # Slots
    def newFile(self):
        # Logic for creating a new file goes here...
        self.centralWidget.setText("<b>File > New</b> clicked")

    def openFile(self):
        # Logic for opening an existing file goes here...
        self.centralWidget.setText("<b>File > Open...</b> clicked")

    def saveFile(self):
        # Logic for saving a file goes here...
        self.centralWidget.setText("<b>File > Save</b> clicked")

    def copyContent(self):
        # Logic for copying content goes here...
        self.centralWidget.setText("<b>Edit > Copy</b> clicked")

    def pasteContent(self):
        # Logic for pasting content goes here...
        self.centralWidget.setText("<b>Edit > Past</b> clicked")

    def cutContent(self):
        # Logic for cutting content goes here...
        self.centralWidget.setText("<b>Edit > Cut</b> clicked")

    def helpContent(self):
        # Logic for launching help goes here]
        self.centralWidget.setText("<b>Help > Help Content...</b> clicked")

    def about(self):
        # Logic for showing an about dialog content goes here...
        self.centralWidget.setText("<b>Help > About...</b> clicked")

    def findContent(self):
        self.centralWidget.setText("<b>Edit > Find > Find...</b> clicked")

    def replaceContent(self):
        self.centralWidget.setText("<b>Edit > Find > Replace...</b> clicked")

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
        self.findAction.triggered.connect(self.findContent)
        self.replaceAction.triggered.connect(self.replaceContent)

        # Connect Help Actions
        self.helpContentAction.triggered.connect(self.helpContent)
        self.aboutAction.triggered.connect(self.about)

        # Connect Open Recent to dynamically populate it
        self.openRecentMenu.aboutToShow.connect(self.populateOpenRecent)

    def populateOpenRecent(self):
        # Step 1. Remove the old options from the menu
        self.openRecentMenu.clear()
        # Step 2. Dynamically create  the actions
        actions = []
        filenames = [f"File-{n}" for n in range(5)]
        for filename in filenames:
            action = QAction(filename, self)
            action.triggered.connect(partial(self.openRecentFile, filename))
            actions.append(action)
        # Step 3. Add the actions to the  menu
        self.openRecentMenu.addActions(actions)

    def openRecentFile(self, filename):
        # Logic for opening a recent file goes here...
        self.centralWidget.setText(f"<b>{filename}</b> opened")

    def _createStatusBar(self):
        self.statusbar = self.statusBar()
        # Adding a temporary message
        self.statusbar.showMessage("Ready", 3000)
        # Adding a permanent message
        self.wcLabel = QLabel(f"{self.getWordCount()} Words")
        self.statusbar.addPermanentWidget(self.wcLabel)

    def getWordCount(self):
        #Logic for computing the word count goes here...
        return 42


if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    # Create and show the main window
    win = Window()
    win.show()
    #  Run the event loop
    sys.exit(app.exec())
