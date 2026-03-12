import json

class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks
        }


class StudentManager:
    def __init__(self):
        self.students = []
        self.file_name = "students.json"
        self.load_data()

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        student = Student(student_id, name, age, course, marks)
        self.students.append(student)

        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        print("\nStudent List")
        print("-" * 50)

        for s in self.students:
            print(f"ID: {s.student_id}")
            print(f"Name: {s.name}")
            print(f"Age: {s.age}")
            print(f"Course: {s.course}")
            print(f"Marks: {s.marks}")
            print("-" * 50)

    def search_student(self):
        sid = input("Enter Student ID to search: ")

        for s in self.students:
            if s.student_id == sid:
                print("Student Found:")
                print(f"Name: {s.name}")
                print(f"Age: {s.age}")
                print(f"Course: {s.course}")
                print(f"Marks: {s.marks}")
                return

        print("Student not found.")

    def update_student(self):
        sid = input("Enter Student ID to update: ")

        for s in self.students:
            if s.student_id == sid:
                s.name = input("Enter new name: ")
                s.age = int(input("Enter new age: "))
                s.course = input("Enter new course: ")
                s.marks = float(input("Enter new marks: "))
                print("Student updated successfully!")
                return

        print("Student not found.")

    def delete_student(self):
        sid = input("Enter Student ID to delete: ")

        for s in self.students:
            if s.student_id == sid:
                self.students.remove(s)
                print("Student deleted successfully!")
                return

        print("Student not found.")

    def save_data(self):
        data = [s.to_dict() for s in self.students]

        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

        print("Data saved successfully.")

    def load_data(self):
        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)

                for item in data:
                    student = Student(
                        item["student_id"],
                        item["name"],
                        item["age"],
                        item["course"],
                        item["marks"]
                    )

                    self.students.append(student)

        except FileNotFoundError:
            pass


def main():
    manager = StudentManager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save Data")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            manager.search_student()

        elif choice == "4":
            manager.update_student()

        elif choice == "5":
            manager.delete_student()

        elif choice == "6":
            manager.save_data()

        elif choice == "7":
            manager.save_data()
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
