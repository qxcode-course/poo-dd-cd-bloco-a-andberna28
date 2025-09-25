class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def __str__(self):
        return f"{self.species}:{self.age}:{self.sound}"

    def ageBy(self, increment: int) -> None:
        self.age += increment
        if self.age >= self.getMaxAge():
            print("warning: " + self.species + " morreu")
            self.age = self.getMaxAge()

    def noise(self) -> None:
        if  self.age == 0:
            print("---")
        elif self.age == self.getMaxAge():
            print("RIP")
        else:
            print(self.sound)

    def getMaxAge(self) -> int:
        return 4

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
        elif args[0] == "grow":
            increment: int = int(args[1])
            animal.ageBy(increment)
        elif args[0] == "noise":
            animal.noise()

main()