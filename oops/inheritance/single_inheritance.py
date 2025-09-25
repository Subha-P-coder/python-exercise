class dad:
    def house(self):
        print("He has one big Yellow house")
class daughter(dad):
    def factory(self):
        print("I have one cement factory")
n = daughter()
n.factory()
n.house()

# if i work in tech company there is one coder  already write the code but i dont want that code 
# that cases i am not gonna delete the content but i override in class below example

class app1:
    def v1(self):
        print("bunch of code")

class app1_1(app1):
    def v2(self):
        print("i insert new code")
    def v1(self):
        print("i override the concept of v1")

a = app1_1()
a.v1()
a.v2()