import time

# Person Class
class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def set_address(self, new_address):
        self.address = new_address

    def to_string(self):
        return f"\nName: {self.name}\nAddress: {self.address}"


# Student Class
class Student(Person):
    def __init__(self, name, address, courses=None, grades=None, num_courses=0):
        super().__init__(name, address)
        self.courses = courses if courses is not None else []
        self.grades = grades if grades is not None else []
        self.num_courses = num_courses

    def add_course_grade(self, course, grade):
        self.courses.append(course)
        self.grades.append(grade)
        self.num_courses += 1

    def print_grades(self):
        for course, grade in zip(self.courses, self.grades):
            print(f"Course: {course}\nGrade: {grade}")

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


# Teacher Class
class Teacher(Person):
    def __init__(self, name, address, courses=None, num_courses=0):
        super().__init__(name, address)
        self.courses = courses if courses is not None else []
        self.num_courses = num_courses

    def add_course(self, course):
        self.courses.append(course)
        self.num_courses += 1

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            self.num_courses -= 1

    def to_string(self):
        return f"\nName: {self.name}\nAddress: {self.address}\nCourses: {', '.join(self.courses)}"


# Objects
ali = Student("Ali", "Fergana", [], [])
vali = Teacher("Mr. John", "Tashkent", [])


try:
    user_input = int(input("1: Student\n2: Teacher\nEnter: "))
    while True:
        if user_input == 1:
            user_choice = int(input("\n1: To string\n2: Add Course Grades\n3: Print Grades\n4: Get Average Grades\n5: Exit\nEnter: "))

            if user_choice == 1:
                print(ali.to_string())
            elif user_choice == 2:
                course = input("Enter course name: ")
                grade = int(input("Enter course grade: "))
                ali.add_course_grade(course, grade)
            elif user_choice == 3:
                ali.print_grades()
            elif user_choice == 4:
                print(f"Average grade: {ali.get_average_grade()}")
            elif user_choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice!")
            time.sleep(1)

        elif user_input == 2:
            user_choice = int(input("\n1: To string\n2: Add Course\n3: Remove Course\n4: Exit\nEnter: "))

            if user_choice == 1:
                print(vali.to_string())
            elif user_choice == 2:
                course = input("Enter course name: ")
                vali.add_course(course)
            elif user_choice == 3:
                course = input("Enter course name to remove: ")
                vali.remove_course(course)
            elif user_choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice!")
            time.sleep(1)

except ValueError:
    print("Only numbers enter!!!")
except AttributeError:
    print("Make sure the instances are correctly defined and are instances of their respective classes.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")