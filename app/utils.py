import uuid
import sqlite3
import os
from pathlib import Path

BASE_PATH = Path(__file__).parent.parent
DATABASE_PATH = os.path.join(BASE_PATH, "students.db") 

def generate_user_id() -> str:
    """Generate a unique 8-character user ID using UUID.
    
    Returns:
        str: First 8 characters of a UUID4 string
    """
    return str(uuid.uuid4()).split("-")[0]


def get_connection(db_path: str = "students.db") -> sqlite3.Connection:
    """Create and return a database connection."""
    conn = sqlite3.connect(db_path)
    return conn


def create_student_table(db_path: str = "students.db") -> None:
    """Create the students table if it doesn't exist.
    
    Args:
        db_path: Path to the SQLite database file
        
    Raises:
        sqlite3.Error: If table creation fails
    """
    try:
        with get_connection(db_path) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students(
                    student_id VARCHAR(8) NOT NULL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    age INTEGER NOT NULL CHECK (age > 0),
                    email VARCHAR(255) UNIQUE,
                    gender VARCHAR(6),
                    courses TEXT
                );
            """)
            connection.commit()
    except sqlite3.Error as e:
        print(f"❌ Error creating student table: {e}")
        raise


