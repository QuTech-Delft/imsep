from operator import length_hint

# Python

## Basics

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

### Initialising classes

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

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.move = "drive"
    
    def move(self):
        print(self.move)


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.move = "sail"
        
    def move(self):
        print(self.move)


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.move = "fly"
        
    def move(self):
        print(self.move)
```

```python
class Vehicle:
    def __init__(self, brand, model, move):
        self.brand = brand
        self.model = model
        self.move = move
    
    def move(self):
        print(self.move)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand=brand, model=model, move="drive")


class Boat(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand=brand, model=model, move="sail")


class Plane(Vehicle):
    def __init__(self, brand, model, wings):
        super().__init__(brand=brand, model=model, move="fly")

        self.wings = wings

    def safety_check(self):
        if not self.wings:
            raise ValueError("This plane will not fly!")
```
