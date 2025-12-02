#1
class BankAccount:
    def __init__(self, acc_no, owner, balance=0):
        self.account_number = acc_no
        self.owner_name = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current Balance:", self.balance)
#2
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def count_reviews(self):
        return len(self.reviews)

    def display_reviews(self):
        for r in self.reviews:
            print("-", r)
#3
class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    def set_name(self, name):
        if name != "":
            self._name = name

    def set_roll_no(self, roll):
        if 1 <= roll <= 100:
            self._roll_no = roll

    def set_marks(self, marks):
        if marks >= 0:
            self._marks = marks

    def get_name(self):
        return self._name

    def get_roll_no(self):
        return self._roll_no

    def get_marks(self):
        return self._marks
#4
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return 0.5 * self.b * self.h
#5
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc
#6
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def calculate_salary(self):
        return 5000

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 30000

class ContractEmployee(Employee):
    def calculate_salary(self):
        return 20000
#7
class Person:
    def __init__(self, name="", age=0, address=""):
        self.name = name
        self.age = age
        self.address = address

# Works as:
# Person("Payel")
# Person("Payel", 20)
# Person("Payel", 20, "Kolkata")
#8
class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1
#9
class Herbivore:
    def herb(self):
        print("Eats plants")

class Carnivore:
    def carn(self):
        print("Eats meat")

class Omnivore:
    def omni(self):
        print("Eats both")

class Bear(Herbivore, Carnivore, Omnivore):
    def info(self):
        print("Bear is an omnivore animal")
#10
class User:
    def __init__(self, name):
        self.name = name

class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

class ChatRoom:
    def __init__(self):
        self.users = []
        self.messages = []

    def join(self, user):
        self.users.append(user)
        print(user.name, "joined the chat")

    def leave(self, user):
        self.users.remove(user)
        print(user.name, "left the chat")

    def send_message(self, user, text):
        msg = Message(user.name, text)
        self.messages.append(msg)

    def show_chat(self):
        for m in self.messages:
            print(f"{m.sender}: {m.text}")
