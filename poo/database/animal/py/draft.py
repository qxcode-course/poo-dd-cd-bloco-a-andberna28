class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def __str__(self):
        return f"{self.species}:{self.age}:{self.sound}"

    def ageBy(self, increment: int) -> None:
        self.age += self.increment
        if self.age >= 4:
            print("Warning: " + self.species + " morreu")
            self.wetness = self.getMaxWetness()

    # def getMaxAge(self)

def main():
    animal = Animal("", "")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "init":
            species = args[1]
            sound = args[2]
            animal = Animal(species, sound)
        elif args[0] == "show":
            print(animal)

main()