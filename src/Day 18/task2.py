import sqlite3
import pandas as pd

# ===============================
# 1️⃣ CONNECT TO DATABASE
# ===============================
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# ===============================
# 2️⃣ FILTER: Data Science interns with stipend > 5000
# ===============================
filter_query = """
SELECT name, track, stipend
FROM interns
WHERE track = 'Data Science' AND stipend > 5000
"""
df_filter = pd.read_sql_query(filter_query, conn)
print("✅ Data Science Interns with stipend > 5000:\n")
print(df_filter)

# ===============================
# 3️⃣ AGGREGATE: Average stipend per track
# ===============================
avg_query = """
SELECT track, AVG(stipend) AS average_stipend
FROM interns
GROUP BY track
"""
df_avg = pd.read_sql_query(avg_query, conn)
print("\n✅ Average stipend per track:\n")
print(df_avg)

# ===============================
# 4️⃣ COUNT: Number of interns per track
# ===============================
count_query = """
SELECT track, COUNT(*) AS intern_count
FROM interns
GROUP BY track
"""
df_count = pd.read_sql_query(count_query, conn)
print("\n✅ Number of interns per track:\n")
print(df_count)

# ===============================
# 5️⃣ CLOSE CONNECTION
# ===============================
conn.close()
