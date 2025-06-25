from typing import List, Optional, Dict, Any
from utils import generate_user_id

class Student():
    """A class representing a student with personal and academic information."""

    # constructor
    def __init__(self, name: str, age: int, email: str, gender: Optional[str], courses_taken: Optional[List[str]] = None):
        """Initialize a Student instance.
        
        Args:
            name: The student's name
            age: The student's age
            email: The student's email address
            gender: The student's gender (optional)
            courses_taken: List of courses taken by the student (optional)
        """
        self.student_id: str = generate_user_id()
        self.name: str = name
        self.age: int = age
        self.gender: str = gender
        self.email: str = email
        self.courses_taken: List[str] = courses_taken or []


    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the student's information to a dictionary.
        
        Returns:
            A dictionary containing all student attributes.
        """
        return {
            "Student ID": self.student_id,
            "Name": self.name,
            "Age": self.age,
            "Email": self.email,
            "Gender": self.gender,
            "Courses": self.courses_taken.copy()  # Return a copy of courses_taken
        }
    
    
    def courses_to_string(self) -> str:
        """Convert the list of courses to a string representation.
        
        Returns:
            A string representation of the courses list.
        """
        return str(self.courses_taken)
    

    def __repr__(self) -> str:
        """String representation of the Student object."""
        return f"Student(student_id={self.student_id!r}, name={self.name!r}, age={self.age!r})"
