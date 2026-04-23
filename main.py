import sqlite3


# ---------- Database Connection ----------
def connect_db():
    return sqlite3.connect("students.db")


# ---------- Create Table ----------
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT
    )
    """)
    conn.commit()


# ---------- Add Student ----------
def add_student(conn):
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    conn.commit()
    print("✅ Student added successfully!")


# ---------- View Students ----------
def view_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\n📋 Student Records:")
    if not rows:
        print("No records found.")
    else:
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]}")


# ---------- Delete Student ----------
def delete_student(conn):
    student_id = int(input("Enter Student ID to delete: "))

    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print("❌ No record found with this ID")
    else:
        print("🗑️ Student deleted successfully")


# ---------- Search Student ----------
def search_student(conn):
    name = input("Enter name to search: ")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()

    print("\n🔍 Search Results:")
    if not rows:
        print("No matching records found.")
    else:
        for row in rows:
            print(row)


# ---------- Main Menu ----------
def main():
    conn = connect_db()
    create_table(conn)

    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(conn)
        elif choice == "2":
            view_students(conn)
        elif choice == "3":
            search_student(conn)
        elif choice == "4":
            delete_student(conn)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.")

    conn.close()


# ---------- Run Program ----------
if __name__ == "__main__":
    main()
