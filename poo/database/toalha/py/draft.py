class Towel:
    def __init__(self, color: str, size: str):
        self.color = color
        self.size = size
        self.wetness = 0

    def __str__(self):
        return f"color: {self.color}, tam: {self.size}, umi: {self.wetness}"


toalha = Towel("red", "G")
toalha2 = Towel("black", "P")

print(toalha.color)
toalha.color = "white"
print(toalha.color)
print(toalha.size)
print(toalha.wetness)