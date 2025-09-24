playlist  = ["shape of you", "Believer", "Blank Space","you make me do"]

print("spotify playlist:",playlist)

#append
playlist.append("Jump")
print("after append:",playlist)

#insert
playlist.insert(1,"Lover")
print("after insert:", playlist)

#remove
playlist.remove("Lover")
print("After remove:",playlist)

#pop
playlist.pop()
print("after pop",playlist)

# reverse
playlist.reverse()
print("after reverse:",playlist)

#list Slicing
print("First 2 songs:",playlist[0:2])
print("First 2 songs:",playlist[1:3])
print("last 2 songs:",playlist[-2:])
print("first two:",playlist[:2])

#list iteration
favorite_foods = ["Dosa", "idli", "parotta","icecream","biriyani","sapathi"]

# you can update  in lists but you can't change in tuples because it is immutable
favorite_foods[1] = "vada"
print(favorite_foods)

for food in favorite_foods:
    print(food)


#check if item exist
# example1
for song in playlist:
    if "Believer" in song:
        print(song + " by subha")
    elif "Shape of you":
        print(song + " by subha")
    elif "Blank Space":
        print(song," by subha")
 
# example2
if "Dosa" in favorite_foods:
    print("yes")

# lists are mutable 
mixed = [1,"subha",23,"dindigul"]
print(mixed)
print(mixed[2])

#index position
for i, songs in enumerate(playlist):
    print(f"songs {i} : {songs}")