# Behavioral Design Patterns
## Author: Andreea Burdui

## Objectives:

- Study and understand the Behavioral Design Patterns.
- As a continuation of the previous laboratory work, think about what communication between software entities might be involed in your system.
- Implement some additional functionalities using behavioral design patterns.

## Used Design Patterns

- Observer

# Implementation

In this project i used the design pattern - Observer for continuing the implemention of a Vehicle Manufacturing System.
## 1. Observer

Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.
In this project, the implementation demonstrates the Observer Pattern, where changes in the subject (electric car's battery) trigger appropriate actions in the observer (warnings).

The Subject class maintains a list of observers and notifies them of changes: 
 * attach(observer): adds an observer to the list, 
 * detach(observer): removes an observer, 
 * notify(): calls the update() method on all observers to inform them of changes.

```bash
class Subject:
    def __init__(self):
        self._observers = []  #list to hold attached observers

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()
```
Observer defines an interface with the update() method that all concrete observers must implement for specific reactions to changes.

```bash
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass
```
ElectricCar acts as the "Concrete Subject," notifying observers of changes in battery capacity.
 * drive(): Simulates driving, decreases battery capacity, and triggers notify() to update observers.

```bash
class ElectricCar(Vehicle, Subject):
    def __init__(self):
        Vehicle.__init__(self, name='Electric Car', wheels=4)
        Subject.__init__(self)
        self.battery_capacity = 100  # battery starts at 100%

    def drive(self):
        if self.battery_capacity > 0:
            self.battery_capacity -= 10
            print(f"Driving... Battery at {self.battery_capacity}%")
            self.notify()  # notifies observers of the change
        else:
            print("Battery depleted! Please recharge.")

    def __str__(self):
        return f"{self.name} with {self.wheels} wheels and a battery capacity of {self.battery_capacity}%"
```

Example output when driving:

>Driving... Battery at 90%
Driving... Battery at 80%

BatteryObserver monitors the battery level of ElectricCar.
 * update(): Responds to notifications from the subject (electric car). Displays warnings based on battery level.

```bash
class BatteryObserver(Observer):
    def __init__(self, electric_car):
        self._electric_car = electric_car

    def update(self):
        battery_level = self._electric_car.battery_capacity
        if battery_level <= 20:
            print("Warning: Battery is low! Consider recharging soon.")
        elif battery_level == 0:
            print("Critical: Battery fully depleted!")
```
Example output when battery is draining:
 > Warning: Battery is low! Consider recharging soon.
Critical: Battery fully depleted!

 ## How the process works:
1. Calling drive(): The main() function calls the drive() method on the ElectricCar object, simulating the car being driven.
2. Battery Decrease: Inside drive(), the battery_capacity is reduced by 10% (if it's above 0). This reflects the car using its battery while driving.
3. Notifying Observers: After the battery decreases, the notify() method (from the Subject class) is called. This loops through all attached observers and calls their update() method. 
4. Observer Reaction: The BatteryObserver reacts in its update() method by checking the new battery_capacity and printing warnings if the level is low (≤20%) or fully depleted (0%).
5. Repeat: The loop in main() calls drive() multiple times, repeating this process until the battery is drained. If the battery is at 0%, the car displays a "Battery depleted" message and stops notifying observers.

## Output:
This is the final output you would see after running the entire program (with 12 calls to drive() in the loop):

```
Driving... Battery at 90%
Driving... Battery at 80%
Driving... Battery at 70%
Driving... Battery at 60%
Driving... Battery at 50%
Driving... Battery at 40%
Driving... Battery at 30%
Driving... Battery at 20%
Warning: Battery is low! Consider recharging soon.
Driving... Battery at 10%
Critical: Battery is almost depleted!
Driving... Battery at 0%
Critical: Battery fully depleted!
Battery depleted! Please recharge.
Battery depleted! Please recharge.
```
## Conclusion
In this laboratory work, i implemented a behavioral design pattern — Observer Pattern. By integrating this essential part, i created a mechanism where the state of an electric vehicle, such as its battery level, was continuously monitored and updates were sent to observers in real time. This pattern showcased how behavioral design can enhance responsiveness and improve communication between objects without tight coupling.


