import sqlite3
import pandas as pd

# Create / Connect to database
conn = sqlite3.connect("interns.db")
cursor = conn.cursor()

# Drop table if exists (so code runs clean every time)
cursor.execute("DROP TABLE IF EXISTS interns")

# Create table
cursor.execute("""
CREATE TABLE interns (
    intern_name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# Insert sample data
intern_data = [
    ('Alice', 'Data Science', 6000),
    ('Bob', 'Web Development', 4000),
    ('Charlie', 'Data Science', 7000),
    ('David', 'Cyber Security', 5500),
    ('Eva', 'Web Development', 4500),
    ('Frank', 'Data Science', 5200)
]

cursor.executemany("INSERT INTO interns VALUES (?, ?, ?)", intern_data)
conn.commit()

# 1️⃣ FILTER: Data Science interns with stipend > 5000
query_filter = """
SELECT intern_name, track, stipend
FROM interns
WHERE track = 'Data Science'
AND stipend > 5000;
"""
df_filter = pd.read_sql_query(query_filter, conn)
print("Filtered Data:\n", df_filter)

# 2️⃣ AGGREGATE: Average stipend per track
query_avg = """
SELECT track, AVG(stipend) AS average_stipend
FROM interns
GROUP BY track;
"""
df_avg = pd.read_sql_query(query_avg, conn)
print("\nAverage Stipend per Track:\n", df_avg)

# 3️⃣ COUNT: Number of interns per track
query_count = """
SELECT track, COUNT(*) AS total_interns
FROM interns
GROUP BY track;
"""
df_count = pd.read_sql_query(query_count, conn)
print("\nTotal Interns per Track:\n", df_count)

conn.close()

