class Vehicle:
    def __init__(self, name: str, wheels: int):
        self.name = name
        self.wheels = wheels

    def __str__(self):
        return f"{self.name} with {self.wheels} wheels"
