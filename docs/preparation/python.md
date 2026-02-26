# Python

## Basics

```python
shopping_cart = {
    "apples": {"price": 0.50, "quantity": 4},
    "oranges": {"price": 0.75, "quantity": 2}
}
discount = 0.5

subtotal_apples = shopping_cart["apples"]["price"] * shopping_cart["apples"]["quantity"]
subtotal_oranges = shopping_cart["oranges"]["price"] * shopping_cart["oranges"]["quantity"]
subtotal = subtotal_apples + subtotal_oranges

total = subtotal * (1 - discount)
print(total)
```

### Loops

```python
shopping_cart = {
    "apples": {"price": 0.50, "quantity": 4},
    "oranges": {"price": 0.75, "quantity": 2}
}
discount = 0.5

subtotal = 0

for item in shopping_cart:
    subtotal += item['price'] * item['quantity']

total = subtotal * (1 - discount)
print(total)
```

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

### Functions

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

### Error handling

```python
def division(x):
    try:
        1 / x
    except ZeroDivisionError:
        print("Anomaly encountered!")

def breaking_badly():
    raise ValueError("This function must not be called!")

def main():
    division(x=1)
    division(x=0)
    
    breaking_badly()
        
        
if __name__ == "__main__":
    main()
```

### If-else statements

### Error handling

## Classes

### Initialising classes

### Methods

### Magic methods

### Inheritance
