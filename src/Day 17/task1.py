import sqlite3

# 1️⃣ Connect to (or create) the database
conn = sqlite3.connect("internship.db")

cursor = conn.cursor()

# 2️⃣ Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
)
""")

# 3️⃣ Insert 5 sample rows
intern_data = [
    (1, "Alice", "Data Science", 1500),
    (2, "Brian", "Web Dev", 1200),
    (3, "Catherine", "Data Science", 1600),
    (4, "David", "Cyber Security", 1400),
    (5, "Emma", "Web Dev", 1300)
]

cursor.executemany("INSERT OR REPLACE INTO interns VALUES (?, ?, ?, ?)", intern_data)

conn.commit()

# 4️⃣ Query ONLY name and track
cursor.execute("SELECT name, track FROM interns")

rows = cursor.fetchall()

print("Intern Name and Track:")
for row in rows:
    print(row)

# Close connection
conn.close()
