import sqlite3
import pandas as pd

# 1️⃣ Connect to database (or create it)
conn = sqlite3.connect("interns.db")
cursor = conn.cursor()

# 2️⃣ Drop tables if they exist (clean run)
cursor.execute("DROP TABLE IF EXISTS interns")
cursor.execute("DROP TABLE IF EXISTS mentors")

# 3️⃣ Create interns table
cursor.execute("""
CREATE TABLE interns (
    intern_id INTEGER PRIMARY KEY,
    intern_name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# Insert sample data for interns
intern_data = [
    (1, 'Alice', 'Data Science', 6000),
    (2, 'Bob', 'Web Development', 4000),
    (3, 'Charlie', 'Data Science', 7000),
    (4, 'David', 'Cyber Security', 5500),
    (5, 'Eva', 'Web Development', 4500),
    (6, 'Frank', 'Data Science', 5200)
]
cursor.executemany("INSERT INTO interns VALUES (?, ?, ?, ?)", intern_data)

# 4️⃣ Create mentors table
cursor.execute("""
CREATE TABLE mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT,
    track TEXT
)
""")

# Insert sample data for mentors
mentor_data = [
    (1, 'Prof. Smith', 'Data Science'),
    (2, 'Dr. Johnson', 'Web Development'),
    (3, 'Ms. Davis', 'Cyber Security')
]
cursor.executemany("INSERT INTO mentors VALUES (?, ?, ?)", mentor_data)

conn.commit()

# 5️⃣ INNER JOIN: List interns with their mentor
query_join = """
SELECT interns.intern_name, interns.track, interns.stipend, mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
"""

# Load result into Pandas DataFrame
df_join = pd.read_sql_query(query_join, conn)
print("Interns with their Mentor:\n", df_join)

# Close connection
conn.close()
