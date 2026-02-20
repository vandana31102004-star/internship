import sqlite3
import pandas as pd

# ===============================
# 1️⃣ CONNECT TO DATABASE
# ===============================
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# ===============================
# 2️⃣ CREATE TABLES
# ===============================
# Interns table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
)
""")

# Mentors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT NOT NULL,
    track TEXT NOT NULL
)
""")

# ===============================
# 3️⃣ INSERT SAMPLE DATA
# ===============================
intern_data = [
    (1, "Alice", "Data Science", 1500),
    (2, "Brian", "Web Dev", 1200),
    (3, "Catherine", "Data Science", 1600),
    (4, "David", "Cyber Security", 1400),
    (5, "Emma", "Web Dev", 1300)
]

mentor_data = [
    (1, "Dr. Smith", "Data Science"),
    (2, "Ms. Johnson", "Web Dev"),
    (3, "Mr. Lee", "Cyber Security")
]

cursor.executemany("INSERT OR REPLACE INTO interns VALUES (?, ?, ?, ?)", intern_data)
cursor.executemany("INSERT OR REPLACE INTO mentors VALUES (?, ?, ?)", mentor_data)
conn.commit()

# ===============================
# 4️⃣ INNER JOIN QUERY
# ===============================
join_query = """
SELECT interns.name AS intern_name,
       interns.track AS track,
       interns.stipend AS stipend,
       mentors.mentor_name AS mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track
"""

# ===============================
# 5️⃣ LOAD RESULTS INTO PANDAS
# ===============================
df = pd.read_sql_query(join_query, conn)
print("✅ Interns with Mentors:\n")
print(df)

# ===============================
# 6️⃣ OPTIONAL: FILTER AND SORT
# ===============================
# Example: Data Science interns
ds_interns = df[df['track'] == 'Data Science']
print("\n✅ Data Science Interns:\n", ds_interns)

# Example: Sort by stipend descending
sorted_df = df.sort_values(by='stipend', ascending=False)
print("\n✅ Interns Sorted by Stipend (High → Low):\n", sorted_df)

# ===============================
# 7️⃣ CLOSE CONNECTION
# ===============================
conn.close()

