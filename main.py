from pizzapy import Customer, StoreLocator, Order, CreditCard, ConsoleInput


def searchMenu(menu):
    print("You are now searching the menu....")
    
    item = input("Type an item to look for: ").strip().lower()

    if len(item) > 1:
        item = item[0].upper() + item[1:]
        print(f"Result for: {item}")
        menu.search(Name=item)  # class method, takes 1 args
        print()
    else:
        print("No result")

def addToOrder(order):
    print("Please type the codes of the items you'd like to order....")
    print("Press Enter to Stop ordering")
    while True:
        item = input("Code:").upper().strip()
        try:
            order.add_item(item)
        except:
            if item == "":
                break
            print("Invalid Code")

# Class method accessing new_customer
customer = ConsoleInput.get_new_customer()

# Class Storelocator finding the store
my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
print("\nClosest Store:")
print(my_local_dominos)
print("\nMENU\n")

ans = input("Would you like to order from this store? (Y/N)")
if ans.lower() not in ["yes", "y"]:
    print("Good Bye. Thank you")
    quit()

# menu object
menu = my_local_dominos.get_menu()

# order pizza
order = Order.begin_customer_order(customer, my_local_dominos) #, country = "code") 

while True:
    searchMenu(menu)
    addToOrder(order)
    answer = input("Would like to add more items (y/n)? ")
    if answer.lower() not in ["yes", "y"]:
        break

total = 0
tax = 0
print("\nYour order is as follows....")
for item in order.data["Products"]:
    price = float(item["Price"])
    print(f"{item["Code"]} ${price:.2f}")
    total += price


tax += (0.07 * total)
print("Your order total is: $" + str(total))
print(f"Your total after tax is: $ {total + tax}")

# enter credit card or pay cash
payment = input("Will you be paying with CASH or Credit Card? (CASH, CREDIT CARD)")
if payment.lower() in ["card" , "credit_card"]:
    card = ConsoleInput.get_credit_card()
else:
    card = False

# place an order
final_ans = input("Would you like to place this order? (y/n)")
if ans.lower() in ["y", "yes"]:
    order.place(card)
    my_local_dominos.place_order(order, card)
    print("Order Placed")
else:
    print("Good Bye, Thank you!")