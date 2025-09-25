class grandfather:
    def farming_land(self):
        print("4 acre farming land")
class dad(grandfather):
    def house(self):
        print("He has one big Yellow house")
class daughter(dad):
    def factory(self):
        print("I have one cement factory")
n = daughter()
n.factory()
n.house()
n.farming_land()