# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")

# Class 1 (inherits from Person) - hierarchical part
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def show_student(self):
        print(f"Student ID: {self.student_id}")

# Class 2 (inherits from Person) - hierarchical part
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show_teacher(self):
        print(f"Subject: {self.subject}")

# Class 3 (inherits from both Student and Teacher) - multiple inheritance part
class TeachingAssistant(Student, Teacher):
    def __init__(self, name, student_id, subject):
        Student.__init__(self, name, student_id)
        Teacher.__init__(self, name, subject)

    def show_ta(self):
        print(f"TA Name: {self.name}, ID: {self.student_id}, Subject: {self.subject}")

# Creating object
ta1 = TeachingAssistant("Alice", "S123", "Math")

# Using methods
ta1.show_name()       # from Person
ta1.show_student()    # from Student
ta1.show_teacher()    # from Teacher
ta1.show_ta()         # from TeachingAssistant


    #        Person
    #        /    \
    #    Student   Teacher
    #        \      /
    #     TeachingAssistant
