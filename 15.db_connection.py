import mysql.connector

# Create connection
conn = mysql.connector.connect(
    host="localhost",        # or "127.0.0.1"
    user="root",             # your MySQL username
    password="root", # your MySQL password
    database="testdb"        # database name
)

# Check connection
if conn.is_connected():
    print("✅ Successfully connected to MySQL database")

# Create a cursor object to execute queries
cursor = conn.cursor()

# Example: Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
)
""")

# Insert data
cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Alice", 21))
cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Bob", 22))

# Commit changes
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\nStudents Table Data:")
for row in rows:
    print(row)

# Close connection
cursor.close()
conn.close()
