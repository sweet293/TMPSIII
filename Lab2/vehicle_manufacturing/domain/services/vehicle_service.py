from ..factory.vehicle_factory import VehicleFactory

class VehicleService:
    def __init__(self):
        self.factory = VehicleFactory.get_instance()

    def create_standard_vehicle(self, vehicle_type: str):
        return self.factory.create_vehicle(vehicle_type)

    def create_electric_vehicle(self):
        return self.factory.create_vehicle('electric_car')
