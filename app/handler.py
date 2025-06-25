from database import create_new_user, delete_user, find_user, update_user, view_users

def get_student_info() -> dict:
    """Collect student information from user input."""
    print("\nEnter Student Details:")
    name = input("Name: ").strip()
    
    while True:
        try:
            age = int(input("Age: ").strip())
            if age <= 0:
                raise ValueError("⚠️ Age must be positive")
            break
        except ValueError as e:
            print(f"❌ Invalid age: {e}")
    
    gender = input("Gender: ").strip()
    email = input("Email: ").strip() or None
    
    courses = []
    print("Enter courses (optional - leave empty to finish):")
    while True:
        course = input("Course:").strip()
        if not course:
            break
        courses.append(course)
    
    return {
        "name": name,
        "age": age,
        "email": email,
        "gender": gender,
        "courses": courses if courses else None
    }

def add_student_handler() -> None:
    """Handle the add student workflow."""
    student_data = get_student_info()
    try:
        student_id = create_new_user(
            name=student_data["name"],
            age=student_data["age"],
            email=student_data["email"],
            gender=student_data["gender"],
            courses_taken=student_data["courses"]
        )
        print(f"\n✅ Student added successfully with ID: {student_id}")
    except Exception as e:
        print(f"\n❌ Error adding student: {e}")

def view_students_handler() -> None:
    """Display all students."""
    try:
        students = view_users()
        if not students:
            print("\n⚠️ No students found in database")
            return
        
        print("\nList of Students:")
        for student in students:
            print(f"Name: {student['Name']}")
            print(f"Age: {student['Age']}")
            print(f"Email: {student['Email']}")
            print(f"Gender: {student['Gender']}")
            print(f"Courses: {student['Courses']}")
            print("-" * 30)
    except Exception as e:
        print(f"\n❌ Error retrieving students: {e}")


def find_student_handler() -> None:
    """Find and display a single student."""
    student_email = input("\nEnter Student Email to find: ").strip()
    try:
        student = find_user(student_email)
        if student:
            print("\nStudent Found:")
            print(f"Name: {student['Name']}")
            print(f"Age: {student['Age']}")
            print(f"Email: {student['Email']}")
            print(f"Gender: {student['Gender']}")
            print(f"Courses: {student['Courses']}")
        else:
            print("\n⚠️ Student not found")
    except Exception as e:
        print(f"\n❌ Error finding student: {e}")


def update_student_handler() -> None:
    """Handle the student update workflow."""
    student_email = input("\nEnter Student Email to update: ").strip()
    
    # First verify student exists
    try:
        student = find_user(student_email)
        if not student:
            print("\n⚠️ Student not found")
            return
    except Exception as e:
        print(f"\n❌ Error finding student: {e}")
        return
    
    print("\nLeave field blank to keep current value")
    print(f"Current name: {student['Name']}")
    name = input("New name: ").strip() or None
    
    age = None
    while True:
        age_input = input(f"Current age: {student['Age']}\nNew age: ").strip()
        if not age_input:
            break
        try:
            age = int(age_input)
            if age <= 0:
                raise ValueError("⚠️ Age must be positive")
            break
        except ValueError as e:
            print(f"❌ Invalid age: {e}")
    
    print(f"Current gender: {student['Gender']}")
    gender = input("New gender: ").strip() or None
    
    print(f"Current email: {student['Email']}")
    email = input("New email: ").strip() or None
    
    print(f"Current courses: {student['Courses']}")
    print("Enter new courses (one per line, leave empty to finish):")
    courses = []
    while True:
        course = input("Course: ").strip()
        if not course:
            break
        courses.append(course)
    
    try:
        update_user(
            student_email=student_email,
            name=name,
            age=age,
            email=email,
            gender=gender,
            courses=courses if courses else None
        )
        print("\n✅ Student updated successfully")
    except Exception as e:
        print(f"\n❌ Error updating student: {e}")


def delete_student_handler() -> None:
    """Handle the student deletion workflow."""
    student_email = input("\nEnter Student Email to delete: ").strip()
    
    # First verify student exists
    try:
        student = find_user(student_email)
        if not student:
            print("\n⚠️ Student not found")
            return
        
        print("\nStudent to be deleted:")
        print(f"Email: {student['Email']}")
        print(f"Name: {student['Name']}")
        
        confirmation = input("\nAre you sure you want to delete this student? (y/n): ").strip().lower()
        if confirmation == 'y':
            if delete_user(student_email):
                print("\n✅ Student deleted successfully")
            else:
                print("\n❌ Failed to delete student")
        else:
            print("\n❌ Deletion cancelled")
    except Exception as e:
        print(f"\n❌ Error deleting student: {e}")