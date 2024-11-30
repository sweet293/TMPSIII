from ..models.vehicle import Vehicle

class VehicleDecorator(Vehicle):
    def __init__(self, vehicle: Vehicle):
        self._vehicle = vehicle

    def __str__(self):
        return str(self._vehicle)
