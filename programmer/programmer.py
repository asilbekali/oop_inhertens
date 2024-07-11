class Developer:
    def __init__(self, sur_name, position, salary):
        self.sur_name = sur_name
        self.position = position
        self.salary = salary


class SoftwareEngineer(Developer):
    def __init__(self, sur_name, position, salary, bonus, department):
        super().__init__(sur_name, position, salary)
        self.department = department
        self.bonus = bonus

    def total_salary(self):
        return self.salary + self.bonus

    def data(self):
        return f"{self.department} {self.bonus} {self.salary}"


objects = []

try:
    for i in range(3):
        print(f"{i + 1} - Obyektni kiriting")
        sur_name = input("Surname: ")
        position = input("Position: ")
        salary = int(input("Salary: "))
        bonus = int(input("Bonus: "))
        department = input("Department: ")
        obj = SoftwareEngineer(sur_name, position, salary, bonus, department)
        objects.append(obj)
        print()
except Exception as e:
    print(f"Error: {e}")

departments = {}
for engineer in objects:
    if engineer.department not in departments:
        departments[engineer.department] = 0
    departments[engineer.department] += engineer.total_salary()

for department, total in departments.items():
    print(f"{department} - {total} $")
