import sys
import os

from vehicle_manufacturing.domain.decorators.gps_decorator import GPSDecorator

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../")


from vehicle_manufacturing.domain.factory.vehicle_factory import VehicleFactory


def main():
    factory = VehicleFactory.get_instance()

    bike1 = factory.create_vehicle('bike')

    car = factory.create_vehicle('car')
    print("Standard car:", car)

    # Decorate the car with GPS
    gps_bike = GPSDecorator(bike1)
    print("bike with GPS:", gps_bike)


if __name__ == "__main__":
    main()
