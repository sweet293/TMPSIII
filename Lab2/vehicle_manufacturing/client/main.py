import sys
import os

from vehicle_manufacturing.domain.decorators.gps_decorator import GPSDecorator

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../")

from vehicle_manufacturing.domain.adapters.electric_vehicle_adapter import ElectricVehicleAdapter
from vehicle_manufacturing.domain.monitoring.battery_observer import BatteryObserver
from vehicle_manufacturing.domain.factory.vehicle_factory import VehicleFactory


def main():
    factory = VehicleFactory.get_instance()

    bike1 = factory.create_vehicle('bike')
    print(bike1)


    '''car = factory.create_vehicle('car')
    print("Standard car:", car)

    # Create an electric car
    electric_car1 = factory.create_vehicle('electric_car')
    print("Electric car:", electric_car1)

    # Decorate the car with GPS
    gps_bike = GPSDecorator(bike1)
    print("Bike with GPS:", gps_bike)'''

    # Create an electric car
    electric_car = factory.create_vehicle('electric_car')

    # Attach observers
    battery_observer = BatteryObserver(electric_car)
    electric_car.attach(battery_observer)

    # Simulate driving
    for _ in range(12):  # Drive until the battery is depleted
        electric_car.drive()


if __name__ == "__main__":
    main()
