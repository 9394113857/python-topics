import sqlite3

class EmployeeIterator:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.cursor = None

    def __iter__(self):
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM employees")
        return self

    def __next__(self):
        row = self.cursor.fetchone()
        if row is None:
            self.cursor.close()
            self.connection.close()
            raise StopIteration
        return row

# Create an instance of the iterator
iterator = EmployeeIterator('mydatabase.db')

# Iterate over the rows using the iterator
for row in iterator:
    print(row)
