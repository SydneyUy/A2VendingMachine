#Avalible snacks and drink as a list
snacks = [
    {'1':('Mini Pie',5)},
    {'2':('On-the-go Sandwich',5)},
    {'3':('Rock Candy',3)},
    {'4':('Creme de la Creme',4)} 
]

drinks = [
    {'1':('Cold Water',2)},
    {'2':('Minty tea',5)},
    {'3':('Warm Coco',4)},
    {'4':('Rocky soda',4)}
]

print ("Welcome to the Lodge-shop, anything that intrest you?")

#showing the user the snack choices
for item in snacks:
    for FNUM, FITEM in item.items():
        print(f"{FNUM}: {FITEM[0]} - ${FITEM[1]}")


# User makes a snack choice
choice = input("\n(Select a snack by entering the corresponding number):\n")
selected_snack = None
snack_price = 0

# Check if the choice exists in the snacks list
for item in snacks:
    if choice in item:
        selected_snack = item[choice]
        snack_price = selected_snack[1]

if selected_snack:
    print(f"{selected_snack[0]} (${snack_price}), good choice.\n")
else:
    print("We don't have that here.\n")


#Showing drinks to user
print ("Would you like a drink?")
for item in drinks:
    for NUM, ITEM in item.items():
        print(f"{NUM}: {ITEM[0]} - ${ITEM[1]}")

# User makes a drink choice
choice = input("\n(Select a drink by entering the corresponding number):\n")
selected_drink = None
drink_price = 0

#check if choice is there
for item in drinks:
    if choice in item:
        selected_drink = item[choice]
        drink_price = selected_drink[1]

if selected_drink:
    print(f"{selected_drink[0]} (${drink_price}), good choice.\n")
else:
    print("We don't have that here.\n")

# Calculate total cost
total_cost = snack_price + drink_price
print(f"So to make that clear...\nYou have ordered...{selected_snack[0] if selected_snack else 'no snacks'} and {selected_drink[0] if selected_drink else 'no drink'}.\n")
print(f"Your total is: ${total_cost}\n")



#Payment
if total_cost > 0:
    try:
        payment = float(input("(Please input the needed money:)\n$"))
        if payment >= total_cost:
            change = payment - total_cost
            print(f"Alright, here you go. and here is your change: ${change:.2f}\nThanks for visiting the Shop, come back anytime.")
        else:
            print(f"Thats not enough.")
    except ValueError:
        print('(Invalid input. Please enter a valid amount.)')

#If the user inputs none of the corresponding numbers or enters no number    
else:
    print ("..Seems like you have some trouble ordering. Come back anytime soon once you've thought of it.")






