# ----------------------------------------
# 1. Importing the library
# ----------------------------------------
import sqlite3 as sqs

# ----------------------------------------
# 2. Connecting to the database
# (Creates 'stu.db' if it does not exist)
# ----------------------------------------
conn = sqs.connect("stu.db")
print("Database connected successfully!")

# ----------------------------------------
# 3. Creating a cursor
# ----------------------------------------
cursor = conn.cursor()

# ----------------------------------------
# 4. Creating a table (if not exists)
# ----------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
""")
conn.commit()
print("Table created successfully!")

# ----------------------------------------
# 5. Inserting data
# ----------------------------------------
cursor.execute(
    "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", 
    ("Alice", 20, "A")
)
conn.commit()
print("Data inserted successfully!")

# ----------------------------------------
# 6. Fetching & displaying data
# ----------------------------------------
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("\nCurrent Students:")
for row in rows:
    print(row)

# fetchall() --> returns all rows
# fetchone() --> returns first row
# fetchmany(n) --> returns first n rows

# ----------------------------------------
# 7. Updating data
# ----------------------------------------
cursor.execute("UPDATE students SET grade = ? WHERE name = ?", ("B+", "Alice"))
conn.commit()
print("\nData updated successfully!")

# Fetch again to verify update
cursor.execute("SELECT * FROM students")
print("After Update:")
for row in cursor.fetchall():
    print(row)

# ----------------------------------------
# 8. Deleting data7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
# ----------------------------------------
cursor.execute("DELETE FROM students WHERE name = ?", ("Alice",))
conn.commit()
print("\nData deleted successfully!")

# Fetch again to verify deletion
cursor.execute("SELECT * FROM students")
print("After Deletion:")
print(cursor.fetchall())

# ----------------------------------------
# 9. Using 'with' statement for auto-close
# ----------------------------------------
print("\nUsing 'with' statement to read data:")
with sqs.connect("stu.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    print(cursor.fetchall())

# ----------------------------------------
# 10. Closing the connection
# ----------------------------------------
conn.close()
print("\nDatabase connection closed!")
