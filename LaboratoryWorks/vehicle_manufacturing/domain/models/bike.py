from .vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self):
        super().__init__('Bike', 2)
