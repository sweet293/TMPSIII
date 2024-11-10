from .vehicle import Vehicle

class ElectricCar(Vehicle):
    def __init__(self):
        super().__init__('Electric Car', 4)
        self.battery_capacity = 100  # Example battery capacity in kWh

    def __str__(self):
        return f"{self.name} with {self.wheels} wheels and a battery capacity of {self.battery_capacity} kWh"
