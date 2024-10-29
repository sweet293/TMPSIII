# Implement 2 SOLID principles

## Author: Andreea Burdui

## Objectives:

- Implement 2 SOLID letters in a simple project.

## Used SOLID principles

- Single Responsibility Principle
- Open-Closed Principle

# Implementation

This project demonstrates the Single Responsibility Principle (SRP) and the Open-Closed Principle (OCP) through an Order Management System.

## 1. Single Responsibility Principle

SRP states that a class should have only one responsibility. Each class in the project focuses on a distinct task. Here, the User class is responsible for handling user-related tasks like storing the user's name and managing their list of orders.

```bash
class User:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f"User: {self.name}, Orders: {len(self.orders)}"
```
Responsibility: Manages user data and their orders.

## 2. Open-Closed Principle

OCP states that a class should be open for extension but closed for modification. In this code, the PaymentProcessor class and its subclasses implement this by allowing new payment methods without modifying existing code.The PaymentProcessor class can be extended to support new payment methods, without changing the existing logic.

```bash
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses should implement this method!")

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ${amount}")
```
Therefore, it is:
- Open for Extension: New payment methods will be added as subclasses.
- Closed for Modification: Existing payment logic doesn't need to be modified to add new payment methods.


