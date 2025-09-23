class Towel:
    def __init__(self, color: str, size: str):
        self.color = color
        self.size = size
        self.wetness = 0

    def __str__(self):
        return f"color: {self.color}, tam: {self.size}, umi: {self.wetness}"

    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def wringOut(self) -> None:
        self.wetness = 0
        print("A toalha foi torcida, umidade zerada")

    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0

    def isDry(self) -> bool:
        return self.wetness == 0


toalha = Towel("vermelha", "G")
toalha.dry(10)
toalha.dry(40)
toalha.wringOut()
print(toalha)