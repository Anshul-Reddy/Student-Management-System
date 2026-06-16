import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "root",
    database = "student_db"
)

cursor = connection.cursor()

def add_student():
    name  = input("Enter Name: ")
    roll_no = int(input("Enter Roll no: "))
    marks = int(input("Enter Marks: "))

    query = """
    INSERT INTO students(name,roll_no,marks)
    VALUES(%s,%s,%s)
    """
    values = (name,roll_no,marks)
    cursor.execute(query,values)
    connection.commit()
    print("Student Added Successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("\n Student Records:\n")
    for student in students:
        print(student)

def search_students():
    roll_no = int(input("Enter Roll No to Search: "))

    query = """
    SELECT * FROM students
    WHERE roll_no = %s
    """
    cursor.execute(query,(roll_no,))
    student = cursor.fetchone()

    if student:
        print("\nStudent Found:")
        print(student)
    else:
        print("Student Not Found.")

def update_student():
    roll_no = int(input("Enter Roll No: "))
    new_marks = int(input("Enter New Marks: "))

    query = """
    UPDATE students
    SET marks = %s
    WHERE roll_no = %s
    """
    values = (new_marks,roll_no)
    cursor.execute(query,values)
    connection.commit()
    print("Marks Updated Successfully!")

def delete_student():

    roll_no = int(input("Enter the Roll.No to Delete: "))
    confirm = input("Are You Sure? (yes/no): ")
    if confirm.lower() == "yes":#in ["y","yes"]:

        query = """
        DELETE FROM students
        WHERE roll_no = %s
        """
        cursor.execute(query,(roll_no,))
        connection.commit()
        print("Student Deleted Successfully..")
    else:
        print("Deletion Cancelled.")

while True:
    print("\n=====STUDENT MANAGEMENT SYSTEM=====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_students()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank You..")
        break
