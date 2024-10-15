menu ={
    'Ragi ball': 30,
    'South meal':100,
    'North meal':80,
    'Coffe':20,
    'Tea':15,
}

print("Welcome to Python restuarant ")
print("Our menu is as follows ")
print(" Ragi ball = 30\n South meal = 100\n North meal = 80\n Coffe = 20\n Tea = 15 ")

order=0

item1=input("Enter item you  want = ")
if item1 in menu:
    order+=menu[item1]
    print(f"your {item1} has been added ")
else:
    print(f"item not available ")

another_order=input("do you want enter another item (yes/no)=")

if another_order == "yes":
    item2=input("enter the 2nd item = ")

    if item2 in menu:
        order+=menu[item2]
        print(f"Your bill is {order} ")
    else:
        print("item not available ")
print("Thank You visit again")