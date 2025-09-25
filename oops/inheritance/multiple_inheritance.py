# more than one parent and more than one child
class grandfather:
    def farming_land(self):
        print("4 acre farming land")

class dad:
    def house(self):
        print("He has one big Yellow house")

class mom:
    def shop(self):
        print("one shop")

class daughter1(dad,mom,grandfather):
    def factory(self):
        print("I have one cement factory")

class daughter2(dad,mom,grandfather):
    def factory(self):
        print("I have one institute")
        

d1 = daughter1()
d1.factory()
d1.farming_land()
d1.house()

d2 = daughter2()
d2.factory()
d2.farming_land()
d2.house()