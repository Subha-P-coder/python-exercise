# example:1
driver_name = "driver shanmugam"

print(driver_name.upper())
print(driver_name.lower())
print(driver_name.capitalize())

# example:2
mobile = "7010617716"
masked = mobile[:2]+"******"+mobile[-2:]
print(masked)

# example: 3
song = "blank SPACE"
artist = "TAYLOR swift"

formatted = f"{song.title()} - {artist.title()}"
print(formatted)

#example: 4
location = 'dindigul'
fixed_location = location.replace('dindigul','coimbatore')
print(fixed_location)


#example: 5
message = 'Your uber booking id: UB12345. please keep it safe.'
booking_id = message.split(":")[1].split(".")[0].strip()
print(booking_id)

# delimiter
# 1,22,subha,dindigul 
# it separates the word right like comma its called delimiter

#example: 6
promo_msg = "use Zomoto100 to get 100 offer on your first order"

if "Zomoto100" in promo_msg:
    print('offer applied')

#example: 7
feedback = "The driver was polite and the ride was smooth"
print(feedback.find("polite"))

#example: 8 
name = "subha pandiyarajan"
initials = "".join([word[0].upper() for word in name.split()])
print(initials)

#example: 9
word = "The driver was polite and the ride was smooth"
word_clean = len(word.split())
print(word_clean)

