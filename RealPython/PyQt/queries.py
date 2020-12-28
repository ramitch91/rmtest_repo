import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# Create the connection
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("contacts.sqlite")

# Open the connection
if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)

# Create a query and execute it right away using .exec()
createTableQuery = QSqlQuery()
createTableQuery.exec(
    """
    CREATE TABLE contacts(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(40) NOT NULL,
        job VARCHAR(50),
        email VARCHAR(40) NOT NULL
    )
    """
)

print(con.tables())

# Creating a query for later execution using .prepare()
# and the ODBC style for the placeholders
# id field is not needed since it is auto incremented
insertDataQuery = QSqlQuery()
insertDataQuery.prepare(
    """
    INSERT INTO contacts (
        name,
        job,
        email
    )
    VALUES (?, ?, ?)
    """
)

# Sample data
data = [
    ("Joe", "Senior Web Developer", "joe@example.com"),
    ("Lara", "Project Manager", "lara@example.com"),
    ("David", "Data Analyst", "david@example.com"),
    ("Jane", "Senior Python Developer", "jane@example.com"),
]

# Unpack each tuple in data and then use .addBindValue to insert data
# Since we are using positional placeholders, the order in which we call
# .addBindValue() will define the order in which each value is passed
# to the corresponding placeholder
for name, job, email in data:
    insertDataQuery.addBindValue(name)
    insertDataQuery.addBindValue(job)
    insertDataQuery.addBindValue(email)
    insertDataQuery.exec()

"""
In PyQt, combining .prepare(), .bindValue(), and .addBindValue() fully 
protects you against SQL injection attacks, so this is the way to go 
when you’re taking untrusted input to complete your queries.
"""
