import sys
from utils import create_student_table
from handler import add_student_handler, view_students_handler, find_student_handler, update_student_handler, delete_student_handler


def display_menu() -> None:
    """Display the main menu options."""
    print("\n🏫 Student Management System")
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Find Student by Email")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def main() -> None:
    """Main application loop."""
    # Initialize database
    try:
        create_student_table()
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        sys.exit(1)
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            add_student_handler()
        elif choice == '2':
            view_students_handler()
        elif choice == '3':
            find_student_handler()
        elif choice == '4':
            update_student_handler()
        elif choice == '5':
            delete_student_handler()
        elif choice == '6':
            print("\nExiting application...")
            sys.exit(0)
        else:
            print("\n⚠️ Invalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    main()

