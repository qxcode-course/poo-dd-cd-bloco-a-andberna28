class Carro:
    def __init__(self, passageiros: int):
        self.passageiros: int = 0
        self.gas: int = 0
        self.km: int = 0

    def __str__(self):
        return f"pass: {self.passageiros}, gas: {self.gas}, km: {self.km}"

    def enter(self) -> None:
        self.passageiros += 1
        if self.passageiros > self.passMax():
            print("fail: limite de pessoas atingido")
            self.passageiros = self.passMax()

    def leave(self) -> None:
        self.passageiros -= 1
        if self.passageiros < 0:
            print("fail: nao ha ninguem no carro")
            self.passageiros = 0

    def fuel(self, increment: int) -> None:
        self.gas += increment
        if self.gas > self.gasMax():
            self.gas = self.gasMax()

    def drive(self, increment: int) -> None:
        if self.passageiros == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        elif self.gas < increment:
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.km += self.gas 
            self.gas = 0
        else:
            self.km += increment
            self.gas -= increment
            
        
    def passMax(self) -> int:
        return 2
    
    def gasMax(self) -> int:
        return 100

def main():
    carro = Carro(0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "enter":
            carro.enter()
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            increment: int = int(args[1])
            carro.fuel(increment)
        elif args[0] == "drive":
            increment: int = int(args[1])
            carro.drive(increment)
        elif args[0] == "show":
            print(carro)

main()