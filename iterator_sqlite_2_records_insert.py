import sqlite3

# Connect to a database (creates a new database if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert data into the table
cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", ('John Doe', 25))
cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", ('Jane Smith', 30))

# Commit the changes to the database
conn.commit()

# Query the database and fetch the results
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

# Display the results
for row in rows:
    print(row)

# Close the cursor and the connection
cursor.close()
conn.close()
