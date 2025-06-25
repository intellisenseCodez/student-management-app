import sqlite3
from typing import Any, Dict, List, Optional
from student import Student
from utils import get_connection


def create_new_user(name: str, age: int, email: str, gender: Optional[str] = None, courses_taken: Optional[List[str]] = None) -> str:
    """Creates a new student record in the database.
    
    Args:
        name: Student's full name
        age: Student's age (must be positive)
        email: Student's email
        gender: Student's gender (optional)
        courses_taken: List of courses taken (optional)
        
    Returns:
        str: The generated student ID
        
    Raises:
        ValueError: If age is not positive
        sqlite3.Error: If database operation fails
    """

    # Validate inputs
    if age <= 0:
        raise ValueError("⚠️ Age must be a positive number")
    
    # Create student object
    student = Student(name=name,age=age,email=email,gender=gender,courses_taken=courses_taken or [])
    
    
    # Convert courses to string representation
    courses_str = student.courses_to_string()
    
    # make connection
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO students(student_id,name,age,email,gender,courses) 
                VALUES (?, ?, ?, ?, ?, ?);
                """,(student.student_id,student.name,student.age,student.email,student.gender,courses_str))
            conn.commit()

            return student.email
    
    except sqlite3.Error as e:
        print(f"❌ Error creating student: {e}")
        raise



def find_user(student_email: str) -> Optional[Dict[str, Any]]:
    """Find a student by their Email.
    
    Args:
        student_email: The Email of the student to find
        
    Returns:
        A dictionary of student data if found, None otherwise
        
    Raises:
        sqlite3.Error: If there's a database error
    """
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            # Use parameterized query to prevent SQL injection
            cursor.execute("""
                SELECT * FROM students
                WHERE email = ?;
            """, (student_email,))
            
            student = cursor.fetchone() # fetch only one user with the email
            
            if student:
                return {
                    "Name": student[1],
                    "Age": student[2],
                    "Email": student[3],
                    "Gender": student[4],
                    "Courses": student[5]
                }
            print(f"⚠️ No student found with Email: {student_email}")
            return None
            
    except sqlite3.Error as e:
        print(f"❌ Error finding student: {e}")
        raise


def update_user(student_email: str,name: Optional[str] = None,age: Optional[int] = None,email: Optional[str] = None,gender: Optional[str] = None,courses: Optional[List[str]] = None
) -> None:
    """Update a student's record.
    
    Args:
        student_email: Email of student to update
        name: New name (optional)
        age: New age (optional)
        email: New email (optional)
        gender: New gender (optional)
        courses: New courses (optional)
        
    Raises:
        ValueError: If student not found or invalid data
        sqlite3.Error: If database operation fails
    """
    # Get existing student data
    student = find_user(student_email)
    if not student:
        raise ValueError(f"❌ Student with Email {student_email} not found")
    
    # Prepare update data
    update_data = {
        "Name": name if name is not None else student["Name"],
        "Age": age if age is not None else student["Age"],
        "Email": email if email is not None else student["Email"],
        "Gender": gender if gender is not None else student["Gender"],
        "Courses": str(courses) if courses is not None else student["Courses"],
    }
    
    # Validate age if being updated
    if age is not None and age <= 0:
        raise ValueError("⚠️ Age must be a positive number")
    
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE students
                SET name = ?, age = ?, email = ?, gender = ?, courses = ?
                WHERE email = ?;
            """, (
                update_data["Name"],
                update_data["Age"],
                update_data["Email"],
                update_data["Gender"],
                update_data["Courses"],
                student_email
            ))
            conn.commit()
        print(f"✅ Student with Email: {student_email} updated successfully")
        
    except sqlite3.Error as e:
        print(f"❌ Error updating student: {e}")
        raise
    
        
def delete_user(student_email: str) -> bool:
    """Delete a student record from the database.
    
    Args:
        student_email: Email of the student to delete
        
    Returns:
        bool: True if deletion was successful, False if student not found
        
    Raises:
        sqlite3.Error: If there's a database error
    """
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            
            # First check if student exists
            student = find_user(student_email)
            if not student:
                raise ValueError(f"⚠️ Student with email {student_email} not found")
            
            # Delete the student
            cursor.execute("""
                DELETE FROM students
                WHERE email = ?;
            """, (student_email,))
            conn.commit()
            
            print(f"✅ Student with Email: {student_email} deleted successfully")
            return True
            
    except sqlite3.Error as e:
        print(f"❌ Error deleting student: {e}")
        raise

def view_users() -> List[Dict[str, Any]]:
    """Retrieve all student records from the database.
    
    Returns:
        List of dictionaries containing student data
        
    Raises:
        sqlite3.Error: If there's a database error
    """
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM students
                ORDER BY name ASC;
            """)
            
            students = []
            for student in cursor.fetchall():
                students.append({
                    "Name": student[1],
                    "Age": student[2],
                    "Email": student[3],
                    "Gender": student[4],
                    "Courses": student[5]
                })
            
            return students
            
    except sqlite3.Error as e:
        print(f"❌ Error retrieving students: {e}")
        raise