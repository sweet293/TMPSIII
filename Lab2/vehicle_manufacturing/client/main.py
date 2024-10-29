import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../")


from vehicle_manufacturing.domain.factory.vehicle_factory import VehicleFactory


def main():
    factory = VehicleFactory.get_instance()

    car = factory.create_vehicle('car')
    print(car)

    bike = factory.create_vehicle('bike')
    print(bike)

    truck = factory.create_vehicle('truck')
    print(truck)


if __name__ == "__main__":
    main()
