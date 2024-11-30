from ..models.car import Car
from ..models.bike import Bike
from ..models.truck import Truck
from ..models.electric_car import ElectricCar
from ..adapters.electric_vehicle_adapter import ElectricVehicleAdapter


class VehicleFactory:
    _instance = None

    @staticmethod
    def get_instance():
        if VehicleFactory._instance is None:
            VehicleFactory._instance = VehicleFactory()
        return VehicleFactory._instance

    def create_vehicle(self, vehicle_type: str):
        if vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'bike':
            return Bike()
        elif vehicle_type == 'truck':
            return Truck()
        elif vehicle_type == 'electric_car':
            electric_car = ElectricCar(name="Tesla Model 3", wheels=4, battery_capacity=100)
            return ElectricVehicleAdapter(electric_car)
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")