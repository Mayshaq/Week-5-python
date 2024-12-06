class Superhero:
    def __init__(self, name, power, weakness, city):
        self.name = name
        self.power = power
        self.weakness = weakness
        self.city = city
    
    def introduce(self):
        return f"I am {self.name}, the protector of {self.city}! My power is {self.power}."

    def reveal_weakness(self):
        return f"Even the mighty {self.name} has a weakness: {self.weakness}."

# Creating a derived class to add more functionality
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, weakness, city, altitude_limit):
        super().__init__(name, power, weakness, city)
        self.altitude_limit = altitude_limit

    def introduce(self):
        return super().introduce() + f" I can also fly up to {self.altitude_limit} meters!"


hero = Superhero("Flash", "Speed", "Strength", "Central City")
flyer = FlyingSuperhero("Superman", "fly", "speed in the ground", "Metropolis", 5000)

print(hero.introduce())
print(hero.reveal_weakness())
print(flyer.introduce())
