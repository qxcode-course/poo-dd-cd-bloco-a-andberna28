class Calculadora:
    def __init__(self, batteryMax: int):
        self.display: float = 0
        self.batteryMax: int = batteryMax
        self.battery: int = 0

    def __str__(self):
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def charge(self, increment: int) -> None:
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def sum(self, a: float, b: float):
        if self.battery == 0:
            print("fail: bateria insuficiente")
        else:
            self.display = a + b
            self.battery -= 1

    def div(self, den: float, num: float):
        if self.battery == 0:
            print("fail: bateria insuficiente")
        elif num == 0:
            print("fail: divisao por zero")
            self.battery -= 1
        else:
            self.display = den / num
            self.battery -= 1

def main():
    calculadora = Calculadora(0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "init":
            batteryMax = int(args[1])
            calculadora = Calculadora(batteryMax)
        elif args[0] == "charge":
            increment: int = int(args[1])
            calculadora.charge(increment)
        elif args[0] == "sum":
            a: float = float(args[1])
            b: float = float(args[2])
            calculadora.sum(a, b)
        elif args[0] == "div":
            den: float = float(args[1])
            num: float = float(args[2])
            calculadora.div(den, num)
        elif args[0] == "show":
            print(calculadora)

main()