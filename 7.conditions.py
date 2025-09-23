# if
age = 50 

if age >= 18:
    print("You can eligible to vote")
else:
    print("You can't eligible to vote")

# elseif elif
mark = 75

if mark >= 90:
    print("grade A++")
elif mark >= 70:
    print("grade B")
elif mark >= 60:
    print("grade C")
else:
    print("Fail")


# nested-if
age =18
has_license = "yes"

if age>=18:
    if has_license == "yes":
        print("you can drive")
    else:
        print("Go and take license")
else:
    print("you are too young to drive so wait until you can eligible for drive")

# one if but two conditions
mark = 55
attendance = 78

if mark >=55 and attendance >=70:
    print("you're allowed for exam")
else:
    print("you're not allowed for exam")


#or
recharge_amt = 1000
data_balance = 1.5

if recharge_amt >=1200 or data_balance >=1:
    print("you're eligible for bonus data")
else:
    print("you're not eligible for bonus data")


# exercise
order_amt = 1200
days = 'sat'
membership = 'no'

if (order_amt >=1200 and days in['sat','sun']) or membership == "gold":
    print("20% discount")
else:
    print("no discount")

# loops
# for loop
names = ['john','carter','marina','joseph']

for text in names:
    print(text.capitalize())
    print(text.upper())
    print(text.lower())
    print(text.title())

# while loop
corrected_pin = '1234'
entered_pin = ''

while entered_pin != corrected_pin:
    entered_pin = input("Enter your correct pin:")
print("access granted")

# break
for i in range (10):
    if i ==5:
        break
    print(i)

# continue
n = [1,2,3,7,5,8,90,12]

for num in n:
    if num ==5:
        continue
    print(num)

# pass
for i in range(5):
    pass
# pass is a placeholder statement in Python.
# It does nothing, but it’s syntactically required where a statement is needed.
# Useful when you want to write code that is not implemented yet.


# exercise 1
count = 5

while count > 0:
    print(f"countdown: {count}")
    count -= 1
print("TimesUp!")

# exercise2
items = []

while True:
    item = input("Add item (type 'done' to finish):")
    if item.lower() == 'done':
        break
    items.append(item)
print("Items in Cart:",items)