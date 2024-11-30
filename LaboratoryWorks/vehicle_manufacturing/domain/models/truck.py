from .vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self):
        super().__init__('Truck', 6)
