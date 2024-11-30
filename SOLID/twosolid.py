class User:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f"User: {self.name}, Orders: {len(self.orders)}"

class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

    def __str__(self):
        return f"Order #{self.order_id}: ${self.amount}"

class OrderProcessor:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def process_order(self, order, user):
        print(f"Processing {order} for {user}")
        self.payment_processor.process_payment(order.amount)
        user.add_order(order)

# Base class for payments
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses should implement this method!")

# Different payment methods (OCP in action)
class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ${amount}")

# Example usage
user = User("John Doe")
order = Order(1, 100.0)

# Processing the order with PayPal
paypal_payment = PayPalPayment()
order_processor = OrderProcessor(paypal_payment)
order_processor.process_order(order, user)

# Processing the order with Credit Card
credit_card_payment = CreditCardPayment()
order_processor = OrderProcessor(credit_card_payment)
order_processor.process_order(Order(2, 50.0), user)

print(user)

