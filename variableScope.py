# L ---> E ---> G ---> B

# L -- Local scope
# it is only access with in the function
def order():
    food = "Curd Rice"
    print("Your Order is:",food)
order()
# if i try to access outside of the function it makes error
# print(food)

#E -- Enclosing
def cart():
    discount = 15

    def check_out():
        print("applying discount",discount)
    check_out()
cart()
# discount is outer function of check_out but it inside the cart function 

#G -- Global
user_id = "subha123"
def homePage():
    print("welcome:",user_id)
def profilePage():
    print("welcome to profilePage:",user_id)

homePage()
profilePage()


# Built-in
print(__file__)

# total useCase
delivery_partner = "Swiggy"

def hotel():
    item = "pizza"
    def order_now():
        quantity=2
        print(f"ordering {quantity} {item} using {delivery_partner}")
    order_now()
hotel()
