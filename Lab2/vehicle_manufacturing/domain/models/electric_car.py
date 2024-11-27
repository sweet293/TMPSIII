from ..monitoring.subject import Subject
from ..models.vehicle import Vehicle

class ElectricCar(Vehicle, Subject):
    def __init__(self):
        Vehicle.__init__(self, 'Electric Car', 4)
        Subject.__init__(self)
        self.battery_capacity = 100  # Example battery capacity in kWh

    def drive(self):
        # Simulate battery consumption
        if self.battery_capacity > 0:
            self.battery_capacity -= 10
            print(f"Driving... Battery at {self.battery_capacity}%")
            self.notify()
        else:
            print("Battery depleted! Please recharge.")

    def __str__(self):
        return f"{self.name} with {self.wheels} wheels and a battery capacity of {self.battery_capacity}%"
