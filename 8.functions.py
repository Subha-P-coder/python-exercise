# normal function
def function_name():
    print("Welcome to function")
function_name()

# function with one arg
def great(name):
    print(f"Hello {name}, Welcome to thailand")
great("subha")

# function with 2 arguments
def sum(a,b):
    print(a+b)
sum(1,2)

# function with return
def add(a,b):
    return(a+b)
result = add(1,2)
print(result)

# function with *args
def add(*args):
    total =0 
    for num in args:
        total += num
    return total
print(add(1,2,2,3,54))

# function with **kwargs
def create_profile(**kwargs):
    print("---your profile---")
    for key,value in kwargs.items():
        print(f"{key} : {value}")
create_profile(name="subha",age=23,city="dindigul")


