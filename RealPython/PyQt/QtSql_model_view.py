import sys

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableView
)


class Contacts(QMainWindow):
    def __init__(self, parent=None):
        super(Contacts, self).__init__(parent)
        self.setWindowTitle("QTableView Example")
        self.resize(550, 250)

        # Set up the model
        self.model = QSqlTableModel(self)
        self.model.setTable("contacts")
        # EditStrategy can be set to OnFieldChange, OnRowChange or OnManualSubmit
        # OnFieldChange will modify the record immediately upon ENTER or selecting another field
        # OnRowChange will modify the record upon selecting a field in a different row
        # OnManualSubmit will cache all changes until either submitAll() or revertAll() is called
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Job")
        self.model.setHeaderData(3, Qt.Horizontal, "Email")
        self.model.select()

        # Set up the view
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)


def createConnection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("contacts.sqlite")
    if not con.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True


app = QApplication(sys.argv)
if not createConnection():
    sys.exit(1)
win = Contacts()
win.show()
sys.exit(app.exec_())
