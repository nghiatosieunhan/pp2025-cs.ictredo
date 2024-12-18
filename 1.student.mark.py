def input_students():
    students = []
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
        students.append({"id": student_id, "name": name, "dob": dob, "marks": {}})
    return students

def input_courses():
    courses = []
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses.append({"id": course_id, "name": name})
    return courses

def input_marks(students, courses):
    if not students or not courses:
        print("No students or courses available!")
        return
    
    print("\nSelect a course to input marks:")
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course['name']} (ID: {course['id']})")
    
    course_choice = int(input("Enter the course number: ")) - 1
    selected_course = courses[course_choice]
    
    for student in students:
        marks = float(input(f"Enter marks for {student['name']} ({student['id']}) in course {selected_course['name']}: "))
        student["marks"][selected_course["id"]] = marks

def list_courses(courses):
    if not courses:
        print("No courses available!")
        return
    print("\nCourses List:")
    for course in courses:
        print(f"Course ID: {course['id']}, Course Name: {course['name']}")

def list_students(students):
    if not students:
        print("No students available!")
        return
    print("\nStudents List:")
    for student in students:
        print(f"Student ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}")

def show_student_marks(students, courses):
    if not students or not courses:
        print("No students or courses available!")
        return
    
    student_id = input("Enter student ID to view marks: ")
    student = next((s for s in students if s["id"] == student_id), None)
    
    if not student:
        print(f"No student found with ID {student_id}.")
        return
    
    print(f"\nMarks for {student['name']} ({student['id']}):")
    for course in courses:
        marks = student["marks"].get(course["id"], None)
        if marks is not None:
            print(f"{course['name']}: {marks}")
        else:
            print(f"{course['name']}: No marks entered.")

def main():
    students = input_students()
    courses = input_courses()

    while True:
        print("\nChoose an option:")
        print("1. List courses")
        print("2. List students")
        print("3. Input marks for students")
        print("4. Show student marks for a course")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            list_courses(courses)
        elif choice == 2:
            list_students(students)
        elif choice == 3:
            input_marks(students, courses)
        elif choice == 4:
            show_student_marks(students, courses)
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
