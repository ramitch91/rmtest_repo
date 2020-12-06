# Filename: Helloworld.py
"""Simple Hello World example with PyQt5."""

import sys

# Import 'QApplication' and all the  required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# Create an instance of QApplication
app = QApplication(sys.argv)
# if you are not passing any command line arguments in
# you could use QApplication([])

# Create an instance of your application's GUI
window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)

# Show you application' GUI
window.show()

# Run your application's event loop (ro main loop)
sys.exit(app.exec_())

