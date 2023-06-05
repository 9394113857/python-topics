# Certainly! Here's an example of how to use SQLite in Python to create a database, define tables, and perform basic CRUD (Create, Read, Update, Delete) operations:
import sqlite3

# Connect to the SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('../mydatabase.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table
create_table_query = '''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT
    )
'''
cursor.execute(create_table_query)

# Insert records into the table
insert_query = '''
    INSERT INTO employees (name, age, department) VALUES (?, ?, ?)
'''
data = [
    ('John Doe', 30, 'IT'),
    ('Jane Smith', 35, 'HR'),
    ('Mark Johnson', 28, 'Finance'),
]
cursor.executemany(insert_query, data)

# Commit the changes to the database
conn.commit()

# Fetch and display records from the table
select_query = '''
    SELECT * FROM employees
'''
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    print(row)

# Update a record
update_query = '''
    UPDATE employees SET department = ? WHERE id = ?
'''
new_department = 'Sales'
employee_id = 2
cursor.execute(update_query, (new_department, employee_id))
conn.commit()

# Delete a record
delete_query = '''
    DELETE FROM employees WHERE id = ?
'''
employee_id = 3
cursor.execute(delete_query, (employee_id,))
conn.commit()

# Close the cursor and the database connection
cursor.close()
conn.close()
