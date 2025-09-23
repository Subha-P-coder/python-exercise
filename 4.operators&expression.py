#Arithmetic Operator
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

# comparison Operator
x = 5
y = 10
print (x == y)
print(x > y)
print(x<y)
print(x != y)
x+=y
print(x)

#logical operator
g = True
h = False

print(g and h)
print(g or h)
print(not h)

# use case arithmetic & comparison
amount = 1200
tax = amount * 0.18
total = amount + tax
print(total)

if total > 1000 :
    discount = total * 0.10
    total -= discount
print(total)

#logical & comparison
age =70
student = 'yes'

if age > 60 or student == 'yes':
    print("yes discount")
else:
    print('no discount')


