class Pokemon:
    def __init__(self, name, type, level, health):
        self.name = name
        self.type = type
        self.level = level
        self.health = health

    def attack(self):
        print(f"{self.name} attacks!")

    def show_details(self):
        print("Pokemon Details:")
        print("Name:", self.name)
        print("Type:", self.type)
        print("Level:", self.level)
        print("Health:", self.health)


# Creating objects
pikachu = Pokemon("Pikachu", "Electric", 10, 100)
charmander = Pokemon("Charmander", "Fire", 8, 90)

# Using objects
pikachu.show_details()
pikachu.attack()

print()

charmander.show_details()
charmander.attack()
