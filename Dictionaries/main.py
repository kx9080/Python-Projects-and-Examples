student_names = ["Alice", "Bob", "Charlie", "Diana"]
grades = [85, 92, 78, 90]
courses = {
    "Alice" : "Mathematics",
    "Bob" : "Science",
    "Charlie" : "History",
    "Diana" : "Art"
}

def add_student(name, grade, course):
    if name in student_names:
        print(f"Student {name} already exists.")
        return
    student_names.append(name)
    grades.append(grade)
    courses[name] = course

input_name = input("Enter student name: ")
input_grade = int(input("Enter student grade: "))
input_course = input("Enter student course: ")

def remove_student(name):
    if name not in student_names:
        print(f"Student {name} does not exist.")
        return
    index = student_names.index(name)
    student_names.pop(index)
    grades.pop(index)
    del courses[name]

add_student(input_name, input_grade, input_course)
remove_student("Charlie")

print(student_names)
print(grades)
print(courses)

passing_students = [student for student in zip(student_names, grades) if student[1] >= 80]
print("Passing Students:", passing_students)