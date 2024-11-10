from .vehicle_decorator import VehicleDecorator

class GPSDecorator(VehicleDecorator):
    def __str__(self):
        return super().__str__() + " + GPS"
