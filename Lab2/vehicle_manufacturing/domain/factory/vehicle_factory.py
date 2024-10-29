from ..models.car import Car
from ..models.bike import Bike
from ..models.truck import Truck


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
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
