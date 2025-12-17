class Avenger:
    """A class representing an Avenger characters."""

    LEADERS = ["Captain America"]

    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender 
        self.super_power = super_power
        self.weapon = weapon 

    def get_info(self):
        """ to return all information about super hero"""

        info_string = (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Gender: {self.gender}\n"
            f"Super Power: {self.super_power}\n"
            f"Weapon: {self.weapon}\n"
        )
        return info_string
    
    def is_leader(self):
        if self.name in Avenger.LEADERS:
            return True
        else:
            return False

cap = Avenger(
    name = "Captain America",
    age = 106,
    gender = "Male",
    super_power = "Super Strenght",
    weapon = "Shield"
)

iron_man = Avenger(
    name = "IronMan aka Tony Stark",
    age = 53,
    gender = "Male",
    super_power = "Technology , Money",
    weapon = "Armour Suit",
)

black_widow = Avenger(
    name = "Black Widow aka Natasha Romanoff",
    age = 35,
    gender = "Female",
    super_power = "Martial Arts, SuperHuman",
    weapon = "Gadgets , batons",
)

hulk = Avenger(
    name = "Hulk aka Bruce Banner",
    age = 49,
    gender = "Male",
    super_power = "unlimited Strength",
    weapon = "None",
)

thor = Avenger(
    name = "Thor",
    age =1500,
    gender = "Male",
    super_power = "Super Energy",
    weapon = "Mjölnir",
)

hawkeye = Avenger(
    name = "Hawkeye aka Clint Barton",
    age = 48,
    gender = "Male",
    super_power = "Fighting Skills",
    weapon = "Bow and Arrow",
)

Avengers_team = [cap, iron_man, black_widow, hulk, thor, hawkeye]

print(" Avengers Roster and Information")

for hero in Avengers_team:
    print(hero.get_info())
    
    if hero.is_leader():
        print(f" Status: Leader of Avengers")
    else:
        print(f" Status: Team Member")
    
    print("-" * 30)
