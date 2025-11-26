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

Different testing frameworks exist, the most common one being Python's built-in `unittest` package combined with [Pytest](https://docs.pytest.org/en/stable/).
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

What happens if a function calls another function? From a unit testing perspective, this function is external should be replaced with
whatever it returns. This process is known as "mocking", and the `unittest` package provides a module for this.
If not mocked, this could cascade into testing multiple functions and/or classes at once. Even though this is still useful,
it is known as an integration test. These tests should only be defined once unit testing succeeds. 
The example from the previous section has been extended with another function, to define the shopping cart:

!!! example "my_module.py"
    
    ```python
    def get_cart() -> list[dict[str, int]]:
        cart = []
        
        for price in range(1, 3):
            quantity = price + 1
            cart.append({"price": price, "quantity": quantity})
        
        return cart

    
    def calculate_total(discount: float = 0) -> float:
        """
        Calculate the total price of the items in the shopping cart, and apply the discount rate.
        """
        
        if not (0 <= discount <= 1):
            raise ValueError("Discount rate must be between 0 and 1.")

        cart = get_cart()
        subtotal = sum(item["price"] * item["quantity"] for item in cart)
        total = (1 - discount) * subtotal
        
        return total
    ```

!!! exercise

    Complete the unit tests using the template below, the `test_invalid_discount` has already been filled in to give a hint.
    The `get_cart` function remains untested in this example.

    ```python
    from unittest import TestCase
    from unittest.mock import MagicMock, patch
    
    from my_module import calculate_total
    
    
    class TestMyModule(TestCase):
    
        @classmethod
        def setUpClass(cls) -> None:
            item_1 = {"price": 1, "quantity": 3}
            item_2 = {"price": 2, "quantity": 4}
    
            cls.cart = [item_1, item_2]
            cls.discount = 0.5
    
        @patch(target="my_module.get_cart")
        def test_invalid_discount(self, mock_cart: MagicMock) -> None:
            mock_cart.return_value = self.cart
            discount = -1
    
            with self.assertRaises(expected_exception=ValueError):
                calculate_total(discount=discount)
    
        def test_total(self) -> None:
            pass
    ```

??? solution

    ```python
    from unittest import TestCase
    from unittest.mock import MagicMock, patch
    
    from my_module import calculate_total
    
    
    class TestMyModule(TestCase):
    
        @classmethod
        def setUpClass(cls) -> None:
            item_1 = {"price": 1, "quantity": 3}
            item_2 = {"price": 2, "quantity": 4}
    
            cls.cart = [item_1, item_2]
            cls.discount = 0.5
    
        @patch(target="my_module.get_cart")
        def test_invalid_discount(self, mock_cart: MagicMock) -> None:
            mock_cart.return_value = self.cart
            discount = -1
    
            with self.assertRaises(expected_exception=ValueError):
                calculate_total(discount=discount)
    
        @patch(target="my_module.get_cart")
        def test_total(self, mock_cart: MagicMock) -> None:
            mock_cart.return_value = self.cart
    
            expected = 5.5
            calculated = calculate_total(discount=self.discount)
    
            self.assertEqual(first=expected, second=calculated)
    ```

## System testing

Continuing with the shopping cart example, adding an item to a cart and calculate the cost is often not the end result
of a piece of software. Usually, the user adds items to the cart via a GUI, pays via an external provider, and new
entries are made in a database. When testing in this scope, the test is known as a system test. This could be measuring the application performance,
functionalities, etc. 

With only unit tests, nothing is said about the final results of the software. It might be perfect in calculating the total of a shopping cart,
but was this needed in the first place? However, without unit tests, debugging a malfunctioning feature would be difficult, where to start?
So, in terms of what should be tested, both should exist. The system test highly depends on what is being tested, but the following guidelines could help:

- Provide a clear description of the scenario and the expected outcome.
- Provide a configuration of the application (if needed).
- Separate the system tests from the other tests.
  
Sometimes it can also be of use to check the interactions between a few components. These tests are known as integration tests,
and sit between the unit and system tests. Different kinds of other tests exist, but all of them serve a single purpose,
find faults in the software before the user does.

## Summary

In short, different levels of testing exist. Each level increases the scope of the test. The following levels were
discussed on this page:

1. Unit testing, the smallest scope, usually a single function. External components can be mocked.
2. Integration testing, could scope different components, like multiple functions and/or classes.
3. System testing, spans the entire application. Aims to check if the user requirements are met.

Various other types of testing exist, but these are beyond the scope of this workshop.

## Further reading

The next [page](./advanced-testing.md) delves further into unit testing with more advanced topics, like code coverage.
