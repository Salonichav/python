

MENU = {
    "espresso": {"ingredients": {"water": 50, "milk": 0,   "coffee": 18}, "cost": 1.50},
    "latte":    {"ingredients": {"water": 200,"milk": 150, "coffee": 24}, "cost": 2.50},
    "cappuccino":{"ingredients":{"water": 250,"milk": 100, "coffee": 24}, "cost": 3.00}
}

resources = {"water": 300, "milk": 200, "coffee": 100}
money = 0.0

def print_report():
    """Show current resources and money earned."""
    print("\n--- Machine Report ---")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")
    print("----------------------\n")

def is_resource_sufficient(order_ingredients):
    """Return True if enough resources to make the drink, else False."""
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry, not enough {item}.")
            return False
    return True

def process_coins():
    """Return total from coins inserted by user."""
    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters? "))   
        dimes = int(input("How many dimes? "))         
        nickels = int(input("How many nickels? "))     
        pennies = int(input("How many pennies? "))   
    except ValueError:
        print("Invalid input. Assuming 0 coins.")
        return 0.0
    total = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
    return round(total, 2)

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from resources and 'make' the coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy! \n")

def refill_resources():
    """Refill resources to default/full amounts (simple refill)."""
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 100
    print("Resources refilled.\n")

machine_on = True

print("Welcome to the Python Coffee Machine!")
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino)\n"
                   "Type 'report' to see resources, 'refill' to refill, or 'off' to turn off: ").lower()

    if choice == "off":
        machine_on = False
        print("Turning off. Goodbye!")
    elif choice == "report":
        print_report()
    elif choice == "refill":
        refill_resources()
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            cost = drink["cost"]
            if payment < cost:
                print(f"Sorry that's not enough money. Money refunded: ${payment:.2f}\n")
            else:
                change = round(payment - cost, 2)
                money += cost  
                if change > 0:
                    print(f"Here is ${change:.2f} in change.")
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid option. Please choose a valid command.\n")
