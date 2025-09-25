# one parent more child
class dad:
    def farming_land(self):
        print("4 acre farming land")
class daughter1(dad):
    def house(self):
        print("He has one big Yellow house")
class daughter2(dad):
    def factory(self):
        print("I have one cement factory")

d1 = daughter1()
d2 = daughter2()

d1.house()
d1.farming_land()

d2.factory()
d2.farming_land()