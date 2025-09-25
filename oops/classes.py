# class inside function is called method
# class outside function is called function

# example1
class student:
    def say_hello(self):
        print("i am student")
s = student()
s.say_hello()

# example2
class student:
    def sum(self, a,b):
        return a+b
s= student()
print(s.sum(4,5))


# example3
class student:
    def sum(self, n):
        return n
s= student()
print(s.sum("subha"))