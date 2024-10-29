# Creational Design Patterns

## Author: Andreea Burdui

## Objectives:

- Get familiar with the Creational DPs;
- Choose a specific domain;
- Implement at least 3 CDPs for the specific domain;

## Used Design Patterns

- Factory Method
- Singleton
- Builder

# Implementation

This project i used the design patterns - Factory Method, Singleton and Builder for implementing a Vehicle Manufacturing System.
## 1. Factory Method

The Factory Method defines a method, which should be used for creating objects instead of using a direct constructor call (new operator). Subclasses can override this method to change the class of objects that will be created.
```bash
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type: str):
        if vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'bike':
            return Bike()
        elif vehicle_type == 'truck':
            return Truck()
        else:
            raise ValueError(f"unknown vehicle type: {vehicle_type}")
```
Responsibility: The VehicleFactory class will serve as the factory for creating different types of vehicles without specifying their concrete classes.

## 2. Singleton

Singleton is a creational design pattern, which ensures that only one object of its kind exists and provides a single point of access to it for any other code. This is useful for classes that manage shared resources, like configuration settings or connection pools.
```bash
class VehicleFactory:
    _instance = None

    @staticmethod
    def get_instance():
        if VehicleFactory._instance is None:
            VehicleFactory._instance = VehicleFactory()
        return VehicleFactory._instance
```
Responsibility: The VehicleFactory can be implemented as a singleton to ensure that only one instance of the factory is created throughout the application.

## 3. Builder

Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.
```bash
class VehicleBuilder:
    def __init__(self):
        self.vehicle = Vehicle('', 0)

    def set_name(self, name: str):
        self.vehicle.name = name
        return self

    def set_wheels(self, wheels: int):
        self.vehicle.wheels = wheels
        return self

    def build(self):
        return self.vehicle
```
Responsibility: The builder was implemented for constructing complex vehicle configurations (ex. adding features or specifications) by creating a separate VehicleBuilder class.


