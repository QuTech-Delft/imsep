# Python

This workshop is not meant to teach programming in Python. It serves as a reference language to understand the underlying development principles.
Many of these principles are transferable to other programming languages. 
The examples shown on this page build towards the minimal basis for object-oriented programming in Python.

During the workshop, Python is used to demonstrate the importance of code quality and testing.
Additionally, it is used to explain software distribution and dependency management.

## Basics

In its basic form, Python can be used as a sequence of statements to get a certain result.
The example below gives a script to calculate the total value of a shopping cart.

```python
shopping_cart = {
    "apples": {"price": 0.50, "quantity": 4},
    "oranges": {"price": 0.75, "quantity": 2}
}
discount = 0.5

subtotal = sum(item['price'] * item['quantity'] for item in shopping_cart)

total = subtotal * (1 - discount)
print(total)
```

## Functions

Functions are the first step in making the code more reusable. 
The snippet below uses two functions and a "main guard" to calculate the total value.
A "main guard" ensures the function is not called when this Python module is imported into another module.

```python
def calculate_total(shopping_cart, discount):
    subtotal = sum(item['price'] * item['quantity'] for item in shopping_cart)
    total = subtotal * (1 - discount)
    return total


def main():
    shopping_cart = {
        "apples": {"price": 0.50, "quantity": 4},
        "oranges": {"price": 0.75, "quantity": 2}
    }
    discount = 0.5
    
    total = calculate_total(shopping_cart=shopping_cart, discount=discount)
    print(total)


if __name__ == "__main__":
    main()
```

## Error handling

The snippet below gives the syntax to raise errors and catch them.

```python
def calculate_total(shopping_cart, discount):
    if not shopping_cart:
        raise ValueError("Cart cannot be empty.")
    if not (0 <= discount <= 1):
        raise ValueError("Discount must be between 0 and 1.")
    
    subtotal = sum(item['price'] * item['quantity'] for item in shopping_cart)
    total = subtotal * (1 - discount)
    return total


def main():
    shopping_cart = {
        "apples": {"price": 0.50, "quantity": 4},
        "oranges": {"price": 0.75, "quantity": 2}
    }
    discount = 1.2
    
    try:
        total = calculate_total(shopping_cart=shopping_cart, discount=discount)
        print(total)
    except ValueError:
        print("Something went wrong!")


if __name__ == "__main__":
    main()
```

## Classes

Classes are another step in the direction of reusable code. It combines data, known as attributes, 
and the methods which manipulate/use them. Programming a class is explained in the sub-sections below. 

### Initialising classes

All (standard) classes require a constructor, which in Python is done via the `__init__` [magic method](#magic-methods).
In the example below, the `ShoppingCart` class is initialised with its items.

```python
class ShoppingCart:

    def __init__(self, apples, oranges):
        self.items = {
            "apples": {"price": 0.50, "quantity": apples},
            "oranges": {"price": 0.75, "quantity": oranges}
    }


def main():
    shopping_cart = ShoppingCart(apples=4, oranges=2)
    print(shopping_cart.items)


if __name__ == "__main__":
    main()
```

### Methods

In the snippet below, the `calculate_total` method is added to the class, which gets its data from the `items` attribute.
This piece of code is now fully standalone and can be reused anywhere without adding duplication.

```python
class ShoppingCart:

    def __init__(self, apples, oranges):
        self.items = {
            "apples": {"price": 0.50, "quantity": apples},
            "oranges": {"price": 0.75, "quantity": oranges}
    }
        
    def calculate_total(self, discount):
        if not (0 <= discount <= 1):
            raise ValueError("Discount must be between 0 and 1.")
        
        subtotal = sum(item['price'] * item['quantity'] for item in self.items)
        total = subtotal * (1 - discount)
        return total


def main():
    shopping_cart = ShoppingCart(apples=4, oranges=2)
    total = shopping_cart.calculate_total()
    print(total)


if __name__ == "__main__":
    main()
```

### Magic methods

Classes have their own special methods which serve different functions. As mentioned before, 
the `__init__` method is used to construct a class. In the snippet below,
the `__str__` magic method is used to change the behaviour of the class when it is printed.

```python
class ShoppingCart:

    def __init__(self, apples, oranges):
        self.items = {
            "apples": {"price": 0.50, "quantity": apples},
            "oranges": {"price": 0.75, "quantity": oranges}
    }
        
    def __str__(self):
        apples = self.items["apples"]["quantity"]
        oranges = self.items["oranges"]["quantity"]
        return f"A shopping cart with {apples} apples and {oranges} oranges."


def main():
    shopping_cart = ShoppingCart(apples=4, oranges=2)
    print(shopping_cart)


if __name__ == "__main__":
    main()
```

### Inheritance

Take the following classes listed below:

```python
class Car:
    def __init__(self, model):
        self.model = model
        self.move = "drive"
    
    def move(self):
        print(f"I am able to {self.move}!")


class Boat:
    def __init__(self, model):
        self.model = model
        self.move = "sail"
        
    def move(self):
        print(f"I am able to {self.move}!")


class Plane:
    def __init__(self, model, wings):
        self.model = model
        self.move = "fly"
        self.wings = wings
        
    def move(self):
        print(f"I am able to {self.move}!")
    
    def safety_check(self):
        if not self.wings:
            raise ValueError("This plane will not fly!")
```

They all share a common properties, which can be defined in a parent class. Each child class will inherit these properties.
In Python, it is possible to add new properties, or override the properties from the parent class, if needed:

```python
class Vehicle:
    def __init__(self, model, move):
        self.model = model
        self.move = move
    
    def move(self):
        print(f"I am able to {self.move}!")


class Car(Vehicle):
    def __init__(self, model):
        super().__init__(model=model, move="drive")


class Boat(Vehicle):
    def __init__(self, model):
        super().__init__(model=model, move="sail")


class Plane(Vehicle):
    def __init__(self, model, wings):
        super().__init__(model=model, move="fly")

        self.wings = wings

    def safety_check(self):
        if not self.wings:
            raise ValueError("This plane will not fly!")

        
class BrokenCar(Car):
    def __init__(self, model):
        super().__init__(model=model)
        
    def move(self):
        print(f"I am unable to {self.move}!")
```
