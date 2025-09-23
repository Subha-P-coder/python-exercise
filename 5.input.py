'''
#input
a = input("Enter number one:")
b = input("Enter number two")

print(a+b) #o/p: string
c = int(input("Enter number one:"))
d = int(input("Enter number two"))

print(c+d)
'''

#suppose we cant use input as well as hard code typing that cases we can use schedule(system argument)
# for example
import sys;

full_name = sys.argv[1]
last_name = sys.argv[2]

email = full_name.lower().replace(' ','.')+last_name+'@company.com'


print("\n ---Your Profile---")
print("FullName:",full_name+last_name)
print("Generated Email:",email)

name = ' '.join(sys.argv[1:])
name = ''.join(sys.argv[1:])
print(name)


