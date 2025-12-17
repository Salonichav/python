class CoffeeMachine:
    def __init__(self):
    
        self.water = 500     
        self.milk = 300       
        self.coffee = 100     
        self.money = 0.0

        self.coffee_price = 50.0
    def print_report(self):
        print("\n--- Coffee Machine Report ---")
        print(f"Water: {self.water} ml")
        print(f"Milk: {self.milk} ml")
        print(f"Coffee: {self.coffee} g")
        print(f"Money: ₹{self.money}")
        print("-----------------------------")

    def check_resources(self):
        if self.water < 200:
            print("Sorry, not enough water.")
            return False
        if self.milk < 100:
            print("Sorry, not enough milk.")
            return False
        if self.coffee < 20:
            print("Sorry, not enough coffee.")
            return False
        return True
    def process_coins(self):
        print("\nPlease insert coins:")
        ten = int(input("How many ₹10 coins?: "))
        twenty = int(input("How many ₹20 coins?: "))
        fifty = int(input("How many ₹50 coins?: "))

        total = ten * 10 + twenty * 20 + fifty * 50
        print(f"Total money inserted: ₹{total}")
        return total
    def check_transaction(self, money_received):
        if money_received >= self.coffee_price:
            change = money_received - self.coffee_price
            print(f"Transaction successful! Change returned: ₹{change}")
            self.money += self.coffee_price
            return True
        else:
            print("Sorry, not enough money. Money refunded.")
            return False
    def make_coffee(self):
        self.water -= 200
        self.milk -= 100
        self.coffee -= 20
        print("\n Your coffee is ready! Enjoy ")


