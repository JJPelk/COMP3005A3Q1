School Database Management Application
Overview
This School Database Management Application provides a user-friendly graphical interface for performing CRUD operations on a students table within a PostgreSQL database. Users can view all students, add new students, update students' email addresses, and delete students from the database.

Video demonstration: https://www.youtube.com/watch?v=cxpl2wDF0PA

Features
View All Students: Display all student records from the database.
Add New Student: Add a new student record, specifying their first name, last name, email, and enrollment date.
Update Student Email: Update the email address of an existing student using their student ID.
Delete Student: Remove a student record from the database using their student ID.
Prerequisites
Before running the application, ensure you have the following installed:

Python (3.6 or later)
PostgreSQL (9.6 or later)
Pip (Python package installer)

Installation Steps

- To install the required Python packages, run:

	pip install psycopg2 customtkinter

- Ensure PostgreSQL is installed and running on your system.
- Create a new PostgreSQL database for the application.
- Use the provided SQL scripts to create the students table and populate it with initial data.

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

Configuration

- Edit the A3Q1.py file to configure the database connection settings. Replace the placeholder values in the dbname, user, password, and host variables with your actual database details.

Running the Application

- To run the application, navigate to the project directory in your terminal and execute:

	python A3Q1.py

