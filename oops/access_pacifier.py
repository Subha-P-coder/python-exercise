# private,public,protected

# variable access
class parent:
    
    def __init__(self):
        self.public_var = "I am Public"
        self._protected_var = "I am Protected"
        self.__private_var = "I  am Private"

    def access_from_same_class(self):
        print("Inside Parent Class")
        print("public:",self.public_var)
        print("Protected:",self._protected_var)
        print("private:", self.__private_var)

class child(parent):
    def access_from_sub_class(self):
        print("Inside sub Class")
        print("public:",self.public_var)
        print("Protected:",self._protected_var)
        try:
            print("private:", self._parent__private_var) #name mangling
        except Exception:
            print("Private can't access")

class stranger:
    def access_from_other_class(self,obj):
        print("Inside other Class")
        print("public:",obj.public_var)
        print("Protected:",obj._protected_var)
        try:
            print("private:", obj.__private_var)
        except Exception:
            print("Private can't access")
    
p = parent()
c = child()
s = stranger()

print("\n Access From Same class:")
p.access_from_same_class()

print("\n Access From Sub class:")
c.access_from_sub_class()

print("\n Access From other class:")
s.access_from_other_class(p)


# method access
class Parent:
    # Public method
    def public_method(self):
        print("Public method")

    # Protected method (by convention)
    def _protected_method(self):
        print("Protected method")

    # Private method
    def __private_method(self):
        print("Private method")

    def access_from_same_class(self):
        print("Inside Parent Class")
        self.public_method()
        self._protected_method()
        self.__private_method()


class Child(Parent):
    def access_from_sub_class(self):
        print("Inside Child Class")
        self.public_method()
        self._protected_method()
        try:
            self.__private_method()  # ❌ private not accessible
        except AttributeError:
            print("Private can't be accessed from Child")


class Stranger:
    def access_from_other_class(self, obj):
        print("Inside Stranger Class")
        obj.public_method()
        obj._protected_method()
        try:
            obj.__private_method()  # ❌ private not accessible
        except AttributeError:
            print("Private can't be accessed from Stranger")


# Objects
p = Parent()
c = Child()
s = Stranger()

print("\nAccess From Same Class:")
p.access_from_same_class()

print("\nAccess From Child Class:")
c.access_from_sub_class()

print("\nAccess From Stranger Class:")
s.access_from_other_class(p)
