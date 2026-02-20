import sqlite3

# Create / connect to database file
conn = sqlite3.connect("mydatabase.db")

print("Connected successfully!")

# Create a cursor
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Insert data
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("John", 22))

# Save changes
conn.commit()

# Read data
cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)

# Close connection
conn.close()

