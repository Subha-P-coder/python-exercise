# method overriding
class app1:
    def v1(self):
        print("bunch of code")

class app1_1(app1):
    def v2(self):
        print("i insert new code")
    def v1(self):
        print("i override the concept of v1") # overriding v1 is called polymorphism

a = app1_1()
a.v1()
a.v2()

# overloading
# no use of having same method(function) name in python
'''
class fun:
    def h1(self):
        print("h1")
    def h1(int a, int b):
        print(a+b)
    def h1(string a):
        print(a)
    
    
a = fun()
a.h1()
a.h1(2,4)
a.h1("subha")
'''
