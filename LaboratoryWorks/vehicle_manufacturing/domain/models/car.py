from .vehicle import Vehicle

class Car(Vehicle):
    def __init__(self):
        super().__init__('Car', 4)
