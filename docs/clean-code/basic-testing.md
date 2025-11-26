# An introduction to testing

Testing is crucial to code quality, and covering its fundamentals requires its own dedicated page. 

## Unit testing

Unit testing is the first step in testing software. A code block is tested for its correctness, this is usually
a function. If multiple scenario's exist (in the form of if-statements, for example) each scenario is tested.
This way, bugs existing on the lowest level can easily be found (e.g. a conditional incorrectly defined). 

### Setting up a unit test

Take the function defined below:

!!! example "my_module.py"
    
    ```python
    def calculate_total(cart: list[dict[str, int]], discount: float = 0) -> float:
        """
        Calculate the total price of the items in the shopping cart, and apply the discount rate.
        """
    
        if not cart:
            raise ValueError("Cart cannot be empty.")
        if not (0 <= discount <= 1):
            raise ValueError("Discount rate must be between 0 and 1.")
        
        subtotal = sum(item["price"] * item["quantity"] for item in cart)
        total = (1 - discount) * subtotal
        
        return total
    ```

!!! exercise

    How many unit tests would this code block need?

??? solution

    2 to check the conditionals, and 1 for the correct return value, thus 3 in total.

Different testing frameworks exist, the most common one being Python's built-in `unittest` module combined with [Pytest](https://docs.pytest.org/en/stable/).
For now, the `unittest` module can be seen as a framework to define the tests, and `pytest` to launch them.

!!! exercise

    Complete the unit tests using the template below.

    ```python
    from unittest import TestCase
    
    from my_module import calculate_total
    

    class TestMyModule(TestCase):
    
        def test_cart_empty(self) -> None:
            # hint: use a "with self.assertRaises()" block to check if an exception is raised.
            pass
        
        def test_invalid_discount(self) -> None:
            pass
        
        def test_total(self) -> None:
            # hint: use the "self.assertEqual()" method to check if the correct value is returned.
            pass
    ```

??? solution
    
    ```python
    from unittest import TestCase
    
    from my_module import calculate_total
    
    
    class TestMyModule(TestCase):
    
        def test_cart_empty(self) -> None:
            cart = []
            discount = 0
            
            with self.assertRaises(expected_exception=ValueError):
                calculate_total(cart=cart, discount=discount)
        
        def test_invalid_discount(self) -> None:
            item_1 = {"price": 1, "quantity": 3}
            item_2 = {"price": 2, "quantity": 4}
            
            cart = [item_1, item_2]
            discount = -1
            
            with self.assertRaises(expected_exception=ValueError):
                calculate_total(cart=cart, discount=discount)
        
        def test_total(self) -> None:
            item_1 = {"price": 1, "quantity": 3}
            item_2 = {"price": 2, "quantity": 4}
            
            cart = [item_1, item_2]
            discount = 0.5
            
            expected = 5.5
            calculated = calculate_total(cart=cart, discount=discount)
    
            self.assertEqual(first=expected, second=calculated)
    ```

If the same variables are used in multiple tests, it can be of use to define them at the class level.
The `TestCase` class works slightly different compared to regular Python classes. The `setUpClass` class method can be used to
set up items before the tests are run. The `setUp` method can be used to set up items before each test.

??? solution

    ```python
    from unittest import TestCase
    
    from my_module import calculate_total
    
    
    class TestMyModule(TestCase):

        @classmethod
        def setUpClass(cls) -> None:
            item_1 = {"price": 1, "quantity": 3}
            item_2 = {"price": 2, "quantity": 4}
    
            cls.cart = [item_1, item_2]
            cls.discount = 0.5
        
        def setUp(self) -> None:
            print("Running a test!")
    
        def test_cart_empty(self) -> None:
            cart = []
    
            with self.assertRaises(expected_exception=ValueError):
                calculate_total(cart=cart, discount=self.discount)
    
        def test_invalid_discount(self) -> None:
            discount = -1
    
            with self.assertRaises(expected_exception=ValueError):
                calculate_total(cart=self.cart, discount=discount)
    
        def test_total(self) -> None:
            expected = 5.5
            calculated = calculate_total(cart=self.cart, discount=self.discount)
    
            self.assertEqual(first=expected, second=calculated)
    ```

With the unit tests defined, they can be run using the following command:

```shell
pytest
```

The results from the test run will be printed in the console. See what happens when one of the expected exceptions is
changed to a `TypeError`, for example.

!!! note

    Most IDEs have an option to run the tests as well.

### Mocking an external component

Lorem ipsum dolor sit amet consectetur adipiscing elit. Amet consectetur adipiscing elit quisque faucibus ex sapien. 
Quisque faucibus ex sapien vitae pellentesque sem placerat. Vitae pellentesque sem placerat in id cursus mi.

## System testing

- Clear description of scenario and expected outcome.
- Provided example configuration (if any).
- Separate module from unit tests.
