from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QApplication, QTabWidget
from loginDialog import loginDialog
from customerListWidget import customerListWidget
from autoLoanListWidget import autoLoanListWidget
from personalLoanListWidget import personalLoanListWidget
from sys import argv
import database

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        loginPopup = loginDialog()
        loginPopup.exec()

        self.widget = QTabWidget()

        # only show customer list when logged in as admin
        if not database.userid:
            self.widget.addTab(customerListWidget(), 'Customer List')

        self.widget.addTab(autoLoanListWidget(), 'Auto Loans')
        self.widget.addTab(personalLoanListWidget(), 'Personal Loans')

        self.setCentralWidget(self.widget)

if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()