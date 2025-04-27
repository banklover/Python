from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys

"""
    Python code to create a simple GUI application that displays a message in a window.
    1. Import necessary modules from PyQt5.
    2. Create a QApplication object.
    3. Create a main window and set its title and size.
    4. Create a label with a message.
    5. Center align the text and set a larger font size.
    6. Set the layout for the window.
    7. Show the window.
    Author: Peter Lee, Github Copilot
    Date:   Apr. 3, 2025
"""

app = QApplication(sys.argv)

# Create the main window
window = QWidget()
window.setWindowTitle("Message")
window.resize(400, 300)  # Set the window size to 400x300 pixels

# Create a label
label = QLabel("Hello, VS Code")

# Center align the text
label.setAlignment(Qt.AlignCenter)

# Make the font bigger
font = label.font()
font.setPointSize(16)  # Set font size to 16
label.setFont(font)

# Set layout
layout = QVBoxLayout()
layout.addWidget(label)
window.setLayout(layout)

# Show the window
window.show()

# Execute the application
sys.exit(app.exec_())
