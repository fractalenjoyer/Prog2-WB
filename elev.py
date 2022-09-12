class Elev:
    def __init__(self, namn: str, ålder: int, godkänd: bool):
        self.name = namn
        self.age = ålder
        self.happy = godkänd

b = Elev("Bengt", 12, True)

print(b.name)