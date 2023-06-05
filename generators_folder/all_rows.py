# Certainly! Here's an example of how you can print all the rows in the employees table with their headings in the console:
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('../mydatabase.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Retrieve the table schema
describe_query = '''
    PRAGMA table_info(employees)
'''
cursor.execute(describe_query)
table_schema = cursor.fetchall()

# Print column names as headings
column_names = [column[1] for column in table_schema]
print(" | ".join(column_names))

# Retrieve all rows from the table
select_query = '''
    SELECT * FROM employees
'''
cursor.execute(select_query)
rows = cursor.fetchall()

# Print rows
for row in rows:
    print(" | ".join(str(value) for value in row))

# Close the cursor and the database connection
cursor.close()
conn.close()
