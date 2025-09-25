# example1
class student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def display(self):
        print(f"My name is {self.name} and my grade is {self.grade}")

s = student("subha",'o+')
s.display()

# example2
class employee:

    def __init__(self, name, aadhar):
        self.name = name
        self.aadhar = aadhar
    
    def enter_office(self):
        print(f"My name is {self.name} and my Aadhar number is {self.aadhar}")
    def open_bank_account(self):
        print(f"Bank account opened for {self.name} with Aadhar number {self.aadhar}")

emp1 = employee("subha","1234-5678-9012")

emp1.enter_office()
emp1.open_bank_account()

# without constructor
class math:
    def square(self,n):
        return n*n
    def cube(self,n):
        return n*n*n
m = math()
print(m.square(3))
print(m.cube(3))
