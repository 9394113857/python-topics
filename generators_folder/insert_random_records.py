# Certainly! Here's an example of how you can insert 100 random records into the employees table in the SQLite database:
import sqlite3
import random
import string

# Connect to the SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('../mydatabase.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Function to generate random names
def generate_random_name():
    length = random.randint(5, 10)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Insert 100 random records into the table
insert_query = '''
    INSERT INTO employees (name, age, department) VALUES (?, ?, ?)
'''

for _ in range(100):
    name = generate_random_name()
    age = random.randint(22, 60)
    department = random.choice(['IT', 'HR', 'Finance', 'Sales'])
    cursor.execute(insert_query, (name, age, department))

# Commit the changes to the database
conn.commit()

# Close the cursor and the database connection
cursor.close()
conn.close()
