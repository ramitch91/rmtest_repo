# Filename: signal_slots.py

"""Signals and slots example."""

import sys
import functools
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


def greeting(who):
    """Slot Function"""
    if msg.text():
        msg.setText("")
    else:
        msg.setText(f"Hello {who}")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and Slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
btn.clicked.connect(functools.partial(greeting, 'Ricky'))  # Connect clicked to greeting()

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec())
