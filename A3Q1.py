import psycopg2
from datetime import datetime
import customtkinter as ctk
from tkinter import messagebox
from tkinter import simpledialog

# Database connection parameters, bad practice to hardcode these values
dbname = "A3Q1"
user = "postgres"
password = "admin"
host = "localhost"

# Initialize the database connection
try:
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cur = conn.cursor()
except Exception as e:
    print(f"Database connection failed: {e}")
    exit(1)

# GUI Application
class SchoolApp(ctk.CTk):
    WIDTH = 600
    HEIGHT = 400

    def __init__(self):
        super().__init__()

        self.title("School Database Management")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # View All Students Button
        self.view_all_btn = ctk.CTkButton(self, text="View All Students", command=self.getAllStudents)
        self.view_all_btn.pack(pady=(20, 10))

        # Add New Student Button
        self.add_student_btn = ctk.CTkButton(self, text="Add New Student", command=self.addStudent)
        self.add_student_btn.pack(pady=10)

        # Update Student Email Button
        self.update_email_btn = ctk.CTkButton(self, text="Update Student Email", command=self.updateStudentEmail)
        self.update_email_btn.pack(pady=10)

        # Delete Student Button
        self.delete_student_btn = ctk.CTkButton(self, text="Delete Student", command=self.deleteStudent)
        self.delete_student_btn.pack(pady=10)

    def getAllStudents(self):
        try:
            cur.execute("SELECT * FROM students")
            records = cur.fetchall()
            all_students = "\n".join([str(record) for record in records])
            messagebox.showinfo("All Students", all_students)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def addStudent(self):
        first_name = simpledialog.askstring("Input", "Enter first name:", parent=self)
        last_name = simpledialog.askstring("Input", "Enter last name:", parent=self)
        email = simpledialog.askstring("Input", "Enter email:", parent=self)
        enrollment_date_str = simpledialog.askstring("Input", "Enter enrollment date (YYYY-MM-DD):", parent=self)
    
        # Initialize enrollment_date as None
        enrollment_date = None
    
        # Convert the enrollment date from string to date object
        try:
            enrollment_date = datetime.strptime(enrollment_date_str, '%Y-%m-%d').date()
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
    
        if enrollment_date:  # Proceed only if enrollment_date was successfully converted
            try:
                cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                            (first_name, last_name, email, enrollment_date))
                conn.commit()
                messagebox.showinfo("Success", "Student added successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
                conn.rollback()

    def updateStudentEmail(self):
        student_id = simpledialog.askinteger("Input", "Enter student ID:", parent=self)
        new_email = simpledialog.askstring("Input", "Enter new email:", parent=self)
        try:
            cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
            conn.commit()
            messagebox.showinfo("Success", "Email updated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            conn.rollback()

    def deleteStudent(self):
        student_id = simpledialog.askinteger("Input", "Enter student ID to delete:", parent=self)
        try:
            cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
            conn.commit()
            messagebox.showinfo("Success", "Student deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            conn.rollback()

# Run the application
if __name__ == "__main__":
    app = SchoolApp()
    app.mainloop()

# Don't forget to close the database connection when done
cur.close()
conn.close()