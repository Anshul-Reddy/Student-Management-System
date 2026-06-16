import tkinter as tk
import mysql.connector
from tkinter import messagebox

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database = "student_db"
)
cursor = connection.cursor()

def add_student():
    name = name_entry.get()
    roll_no = int(roll_entry.get())
    marks = int(marks_entry.get())
    cursor.execute(
        "SELECT * FROM students WHERE roll_no = %s",(roll_no,)
    )
    existing_student = cursor.fetchone()
    if existing_student:
        messagebox.showerror(
            "Error",
            "Roll Number Already Exists."
        )
        return
    query = """
    INSERT INTO students(name,roll_no,marks)
    VALUES(%s,%s,%s)
    """
    values = (name,roll_no,marks)
    cursor.execute(query,values)
    connection.commit()
    name_entry.delete(0,tk.END)
    roll_entry.delete(0,tk.END)
    marks_entry.delete(0,tk.END)

    messagebox.showinfo(
        "Success",
        "Student Added Successfully!"
    )

def view_students():
    new_window = tk.Toplevel(root)
    new_window.title("Student Records")
    new_window.geometry("500x300")

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    heading = tk.Label(
        new_window,
        text="STUDENT RECORDS",
        font=("Arial",16,"bold")
    )
    heading.pack(pady=20)
    for student in students:
        label = tk.Label(
            new_window,
            text=(f"ID:{student[0]} |"
                f"Name:{student[1]} |"
                f"Roll No:{student[2]} |"
                f"Marks:{student[3]}"
            ),
            font=("Arial",12)
        )
        label.pack(pady=5)

def search_student():
    #roll_no = int(roll_entry.get())
    if roll_entry.get() == "":
        messagebox.showerror(
            "Error",
            "Please enter Roll Number!"
        )
        return
    roll_no = int(roll_entry.get())
    query="""
    SELECT * FROM students
    WHERE roll_no = %s
    """
    cursor.execute(query,(roll_no,))
    student = cursor.fetchone()

    if student:
        name_entry.delete(0,tk.END)
        marks_entry.delete(0,tk.END)

        name_entry.insert(0,student[1])
        marks_entry.insert(0,student[3])
        messagebox.showinfo(
            "StudentFound",
            f"Name: {student[1]}\n"
            f"Roll No: {student[2]}\n"
            f"Marks: {student[3]}"
        )
    else:
        messagebox.showerror(
            "Not Found",
            "Student does not Exist!"
        )

def update_student():
    if roll_entry.get() == "" or marks_entry.get() == "":
        messagebox.showerror(
            "Error",
            "Please Enter Roll No and the Marks!"
        )
        return
    
    roll_no = int(roll_entry.get())
    new_marks = int(marks_entry.get())

    query = """
    UPDATE students
    SET marks = %s
    WHERE roll_no = %s
    """
    values = (new_marks,roll_no)
    cursor.execute(query,values)
    connection.commit()

    messagebox.showinfo(
        "Success",
        "Marks Updated Successfully!"
    )

def delete_student():
    if roll_entry.get() == "":
        messagebox.showerror(
            "Error",
            "Please Enter a Roll Number!"
        )
        return
    roll_no = int(roll_entry.get())
    answer=messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this student?"
    )
    if not answer:
        return
    query = """
    DELETE FROM students
    WHERE roll_no = %s
    """
    cursor.execute(query, (roll_no,))
    connection.commit()
    messagebox.showinfo(
        "Success","Student Deleted Successfully!")
    name_entry.delete(0,tk.END)
    roll_entry.delete(0,tk.END)
    marks_entry.delete(0,tk.END)

root = tk.Tk()
root.title("Student Management System")
root.geometry("600x555")

heading = tk.Label(
    root,
    text = "STUDENT MANAGEMENT SYSTEM v1.0",
    font = ("Arial",16,"bold")
)
heading.pack(pady=20)

name_label = tk.Label(
    root,
    text = "Name:",
    font=("Arial",10)
)
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack(pady=20)    

roll_label = tk.Label(
    root,
    text="Roll No:"
)
roll_label.pack()
roll_entry = tk.Entry(root)
roll_entry.pack(pady=20)

marks_label = tk.Label(
    root,
    text = "Marks:"
)
marks_label.pack()
marks_entry=tk.Entry(root)
marks_entry.pack(pady=5)

add_button = tk.Button(
    root,
    text="Add Student",
    width = 15,
    command = add_student
)
add_button.pack(pady=15)

view_button = tk.Button(
    root,
    text="View Student",
    width = 15,
    command = view_students
)
view_button.pack(pady=15)

search_button = tk.Button(
    root,text="Search Student",width = 15,command = search_student)
search_button.pack(pady=15)

update_button = tk.Button(
    root,text="Update Student",width = 15,command= update_student)
update_button.pack(pady=15)

delete_button = tk.Button(
    root,text="Delete Student",width = 15,command = delete_student
)
delete_button.pack(pady=15)
root.mainloop()