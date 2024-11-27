from ..monitoring.observer import Observer

class BatteryObserver(Observer):
    def __init__(self, electric_car):
        self._electric_car = electric_car

    def update(self):
        battery_level = self._electric_car.battery_capacity
        if battery_level <= 20:
            print("Warning: Battery is low! Consider recharging soon.")
        elif battery_level == 0:
            print("Critical: Battery fully depleted!")
