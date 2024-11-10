from ..models.vehicle import Vehicle
from ..models.electric_car import ElectricCar

class ElectricVehicleAdapter(Vehicle):
    def __init__(self, electric_car: ElectricCar):
        self.electric_car = electric_car

    def __str__(self):
        return f"Electric {self.electric_car.name} with {self.electric_car.wheels} wheels and battery capacity {self.electric_car.battery_capacity}"
