from file1 import dad


class daughter(dad):
    def factory(self):
        print("I have one white cement factory")
    def house(self):
        print("I paint wash house into white color")

d = daughter()
d.factory()
d.house()