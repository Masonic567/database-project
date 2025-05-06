import database
import datetime


database.dropTables()
database.createTables()

database.addClient('1', 'owo', 100)
database.addClient('2', 'owo', 100)
database.addClient('3', 'owo', 100)
database.addClient('4', 'owo', 100)
database.addClient('5', 'owo', 100)
database.addClient('6', 'owo', 100)
database.addClient('7', 'owo', 100)
database.addClient('8', 'owo', 100)
database.addClient('9', 'owo', 100)
database.addClient('10', 'owo', 100)

database.addAutoLoan(
    1, 'jsadkga', 100, 0.1, datetime.datetime.now(), datetime.datetime.now(), 12, 'your mom', 'uwu', 0, 2035
)


# cursor = database.connection.cursor()
# res = cursor.execute('SELECT * from client')
# # res.fetchall()
# print(res.fetchall())
