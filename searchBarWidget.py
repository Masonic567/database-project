from PyQt6.QtWidgets import QLineEdit, QPushButton, QHBoxLayout, QWidget

class searchBarWidget(QWidget):
    def __init__(self, parent = None, placeholderText = None, searchAction=None):
        super(searchBarWidget, self).__init__(parent)

        layout = QHBoxLayout()

        searchBar = QLineEdit(self)
        searchBtn = QPushButton(self)

        if placeholderText:
            searchBar.setPlaceholderText(placeholderText)

        searchBtn.clicked.connect(lambda: searchAction(searchBar.text()))
        searchBtn.setText('Search')

        layout.addWidget(searchBar)
        layout.addWidget(searchBtn)

        self.setLayout(layout)