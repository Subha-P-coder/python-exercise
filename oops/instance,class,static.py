class Employee:
    company = "TechCorp"   # Class variable (shared by all objects)

    def __init__(self, name, salary):
        self.name = name       # Instance variable (unique per object)
        self.salary = salary

    # Instance Method → works with object data (self)
    def show_details(self):
        print(f"Employee: {self.name}, Salary: {self.salary}, Company: {Employee.company}")

    # Class Method → works with class-level data (cls)
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
        print(f"Company changed to: {cls.company}")

    # Static Method → independent, utility function (no self, no cls)
    @staticmethod
    def is_high_salary(salary):
        return salary > 50000


# Create objects
emp1 = Employee("Alice", 40000)
emp2 = Employee("Bob", 60000)

# Instance Method → needs object
emp1.show_details()
emp2.show_details()

# Class Method → can be called with class or object
Employee.change_company("WebTech")   # changes company for all
emp1.show_details()
emp2.show_details()

# Static Method → called with class or object (utility function)
print("Alice high salary?", Employee.is_high_salary(emp1.salary))
print("Bob high salary?", emp2.is_high_salary(emp2.salary))
