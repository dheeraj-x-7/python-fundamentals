from abc import ABC, abstractmethod
# for abstract class we need to import ABC class and for abstract method we need to import abstractmethod from abc module

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
# we can't make instance of abstract
# every child class of a abstract class need to define the method that is abstract method in abstract class.
class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Card(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")

class Cash(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")

payments = [UPI(), Card(), Cash()]

for i in payments:
    i.pay(100)