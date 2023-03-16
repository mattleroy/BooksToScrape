from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

import main


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        quit_action = QAction('Quit', self)
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

        button = QPushButton("OI", self)
        button.setCheckable(True)
        button.clicked.connect(self.clicked_button)
        self.setCentralWidget(button)

        self.setWindowTitle("Books To Scrape")

        self.list_widget = QListWidget()

        data = main.scrape_data(1)
        self.list_widget.addItems(data)

        # Connect itemClicked signal
        self.list_widget.itemClicked.connect(self.on_item_clicked)

        # Add QListWidget to a layout
        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)

        # Create QLabel to display the selected item
        self.selected_item_label = QLabel()
        layout.addWidget(self.selected_item_label)

        # Create widget to hold the layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def on_item_clicked(self, item):
        selected_item_text = item.text()
        self.selected_item_label.setText(f"Selected Item: {selected_item_text}")

        #Using SelectedItemWindow class (NOTE: not having self below makes the window disappear instantly)
        self.selected_item_window = SelectedItemWindow(selected_item_text)
        self.selected_item_window.show()

    def clicked_button(self):
        print("Clicked OI")

class SelectedItemWindow(QMainWindow):
    def __init__(self, selected_item_text):
        super().__init__()

        self.setWindowTitle(selected_item_text)

        selected_item_label = QLabel(selected_item_text)

        # Add the QLabel to a layout
        layout = QVBoxLayout()
        layout.addWidget(selected_item_label)

        widget = QWidget()
        widget.setLayout(layout)
        self.set(widget)


app = QApplication([])  # Remember this is the event loop

window = MainWindow()
window.show()

app.exec_()
