a={1,2,3}
b = set(a)
print(b)

c= set([2,3,4])
print(c)

uber_cities=["chennai","banglore",'delhi','hydrebad']
unique= set(uber_cities)
print(unique)

# union, intersection, difference
city1 = {"karur","dindigul","madurai","coimbatore"}
city2={'coimbatore',"chennai","banglore","hawii"}

print(city1.union(city2))
print(city1.intersection(city2))
print(city1.difference(city2))
print(city2.difference(city1))

city1.add("kerala")
print(city1)

city1.remove("dindigul")
print(city1)

# print(city1[1]) # index position are not show an output it throw an error

# we can't update but we can only insert and then remove
my_set ={1,2,3}
my_set.add(99)
my_set.remove(2)
# safer option to remove or check particular number is not there in variables (discard)
my_set.discard(8)
print(my_set)

