class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus

# Usage
employee = Employee("Alice", 50000)
manager = Manager("Bob", 70000, 10000)

print(f"Employee salary: {employee.calculate_salary()}")
print(f"Manager salary: {manager.calculate_salary()}")
