from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
import database
from enterInfoDialog import enterInfoDialog
from searchBarWidget import searchBarWidget
import datetime

class personalLoanListWidget(QWidget):
    def __init__(self, parent = None):
        super(personalLoanListWidget, self).__init__(parent)
        layout = QVBoxLayout()
        mainwidget = personalLoanList()
        layout.addWidget(mainwidget)

        deleteButton = QPushButton(self)
        deleteButton.setText('Delete Selected')
        deleteButton.clicked.connect(mainwidget.deleteLoan)

        addButton = QPushButton(self)
        addButton.setText('Add New Personal Loan')
        addButton.clicked.connect(mainwidget.addLoan)

        bottomLayout = QHBoxLayout()
        bottomLayout.addWidget(deleteButton)
        bottomLayout.addWidget(addButton)
        layout.addLayout(bottomLayout)

        layout.addWidget(searchBarWidget(self, 'Search Loan ID', lambda x: mainwidget.openDialog(int(x))))

        self.setLayout(layout)

class personalLoanList(QListWidget):
    def __init__(self, parent = None):
        super(personalLoanList, self).__init__(parent)        
        self.itemDoubleClicked.connect(self.handleDoubleClick)
        self.itemClicked.connect(self.handleSingleClick)
        
        self.editing = None
        self.refresh()
    
    def refresh(self):
        self.data = database.getPersonalLoans()
        self.clear()
        for i in self.data:
            self.addItem(
                f'id: {i[1]}, client: {i[0]}, amount: {i[3]}'
            )
    
    def handleSingleClick(self, item):
        text = item.text()
        endidx = text.index(',')
        startidx = text.index(':')+2
        self.editing = int(text[startidx:endidx])

    def handleDoubleClick(self, item: QListWidgetItem):
        self.handleSingleClick(item)
        self.openDialog()

    def openDialog(self, loanId = None):
        if self.editing is None:
            self.editing = loanId

        target = None
        for i in self.data:
            if i[1] == self.editing:
                target = i
                break
        else:
            return

        data = {
            'Client ID': target[0],
            'Loan Amount': target[3],
            'Interest Rate': target[4],
            'Start Date': target[6],
            'End Date': target[7],
            'Number of Payments': target[8],
            'Amount Paid': target[5],
            'Purpose': target[2]
        }

        popup = enterInfoDialog(self, data, self.saveData)
        popup.open()

    def saveData(self, data:dict):
        database.updatePersonalLoan(
            int(data['Client ID']),
            data['Purpose'],
            float(data['Loan Amount']),
            float(data['Interest Rate']),
            float(data['Amount Paid']),
            datetime.datetime.strptime(data['Start Date'], '%Y-%m-%d %H:%M:%S'),
            datetime.datetime.strptime(data['End Date'], '%Y-%m-%d %H:%M:%S'),
            int(data['Number of Payments']),
            self.editing
        )

        self.editing = None
        self.refresh()

    def newData(self, data):
        database.addPersonalLoan(
            int(data['Client ID']),
            data['Purpose'],
            float(data['Loan Amount']),
            float(data['Interest Rate']),
            float(data['Amount Paid']),
            datetime.datetime.strptime(data['Start Date'], '%Y-%m-%d %H:%M:%S'),
            datetime.datetime.strptime(data['End Date'], '%Y-%m-%d %H:%M:%S'),
            int(data['Number of Payments'])
        )
        self.refresh()
    
    def deleteLoan(self):
        database.deletePersonalLoan(self.editing)
        self.editing = None
        self.refresh()

    def addLoan(self):
        data = [
            'Client ID',
            'Loan Amount',
            'Interest Rate',
            'Start Date',
            'End Date',
            'Number of Payments',
            'Amount Paid',
            'Purpose'
        ]
        popup = enterInfoDialog(self, data, self.newData)
        popup.open()