import mysql.connector

try:
    # Create connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="testdb"
    )

    if conn.is_connected():
        print("✅ Successfully connected to MySQL database")
    else:
        print("❌ Connection failed")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    )
    """)

    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Alice", 21))
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Bob", 22))

    conn.commit()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\nStudents Table Data:")
    for row in rows:
        print(row)

except mysql.connector.Error as err:
    print(f"⚠ MySQL Error: {err}")

except Exception as e:
    print(f"⚠ Python Error: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
