# An introduction to testing

!!! abstract "Overview"

    - What is a unit test, and how to write one?
    - How to mock external components when unit testing?
    - What is code coverage?
    - What is test-driven development, and how can it be applied?
    - What other types of testing exist?

## Unit testing

Unit testing is the first step in testing software. A code block is tested for its correctness, usually
limited to a function. If multiple scenarios exist (in the form of if-statements, for example), each scenario is tested.
This way, bugs existing on the lowest level can easily be found, and overall confidence in the code base grows.

### Setting up a unit test

Take the function from the previous page:

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

!!! tip "Question"

    How many unit tests would the `my_module.py` code need?
    
    ??? info "Solution"
    
        2 to check the conditionals, and 1 for the correct return value, thus 3 in total.

Different testing frameworks exist, the most common one being Python's built-in `unittest` package combined with [Pytest](https://docs.pytest.org/en/stable/).
For now, the `unittest` module can be seen as a framework to define the tests, and `pytest` to launch them.

!!! tip "Question"

    Complete the unit tests for the `my_module.py` code using the template below.

    !!! example "test_my_module.py"
    
        ```python
        from unittest import TestCase
        
        from my_module import calculate_total
        
    
        class TestMyModule(TestCase):
        
            def test_cart_empty(self) -> None:
                # hint: use a "with self.assertRaises" block to check if an exception is raised.
                pass
            
            def test_invalid_discount(self) -> None:
                pass
            
            def test_total(self) -> None:
                # hint: use the "self.assertEqual" method to check if the correct value is returned.
                pass
        ```

    ??? info "Solution"
        
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

!!! tip "Question"

    Use the `setUpClass` method to define the `cart` and `discount` variables for the unit tests defined in the previous question.
    
    ??? info "Solution"
    
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

!!! success "Pytest"

    ```text
    collected 3 items
    
    test_my_module.py ...          [100%]
    
    ==== 3 passed in 0.01s ====
    ```

The results from the test run will be printed in the console. See what happens when one of the expected exceptions is
changed to a `TypeError`, for example.

!!! note

    Most IDEs have an option to run the tests as well.

### Mocking an external component

What happens if a function calls another function? From a unit testing perspective, this function is external and should be replaced with
whatever it returns. This process is known as "mocking", and `unittest` provides a module for this.
If not mocked, this could cascade into testing multiple functions and/or classes at once. Even though this is still useful,
it is known as an integration test. These tests should only be defined once the unit tests succeed. 
The example from the previous section has been extended with another function to define the shopping cart:

!!! example "my_module.py"
    
    ```python
    def get_cart() -> list[dict[str, int]]:
        """
        Get a shopping cart filled with pre-defined items.
        """
        
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

!!! tip "Question"

    Complete the unit tests using the template below. The `test_invalid_discount` has already been filled in to give a hint.
    The `get_cart` function remains untested in this example.

    !!! example "test_my_module.py"
    
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

    ??? info "Solution"
    
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

### Test coverage

When writing unit tests, it is good practice to cover the entire code base. This is known as the "test coverage", and
various tools exist to measure it. In Python, `pytest` can be combined with the [coverage](https://coverage.readthedocs.io/en/latest/) package to measure and report the coverage:

```shell
coverage run -m pytest
coverage report
```

With a coverage below 100%, two scenarios exist:

1. Part of the desired functionality remains untested, thus an extra unit test must be written to cover it.
2. The tests fully cover the desired functionality, and part of the source code can be removed, as it is redundant.

### Test-driven development

Software engineering has various design philosophies, one of which is test-driven development (TDD). It argues that software development should
start by writing the unit test, instead of after. This way, the developer is forced to write out all the expected conditionals, errors, and return values beforehand,
instead of during.

This philosophy, combined with a design, can lead to a far better understanding of what needs to be coded compared to just starting right away.
To put the idea into practice, take the following example. A csv-file which could contain empty values needs to be converted into an array.
If an empty value is found, the code needs to raise an error. Similarly, when a user saves the file to an unknown location.

!!! example "TDD"
    
    ```python
    from unittest import TestCase
    

    class MyTest(TestCase):
        
        def test_read_csv(self) -> None:
            # test for return value of a read csv function
            pass
        
        def test_read_csv_none_values(self) -> None:
            # test for when the read csv function encounters none values
            pass
        
        def test_convert_to_array(self) -> None:
            # test for return value of a convert to array function
            pass
        
        def test_convert_to_array_unknown_path(self) -> None:
            # test for when the convert to array function encounters wrong inputs
            pass
    ```

Without filling in the details, the previous example already helps with setting up the "skeleton" of the source code.
It will likely consist of two functions, each with an if-statement which raises an error. The philosophy also helps 
to better apply object-oriented programming (OOP). By thinking of all the design choices beforehand, it is easier to find
related objects and identify potential use cases for inheritance instead of refactoring the source code during development.

## System testing

Continuing with the shopping cart example, adding an item to a cart and calculating the cost is often not the final result
of a software piece. Usually, the user adds items to the cart via a GUI, pays via an external provider, and new
entries are made in a database. When testing in this scope, the test is known as a system test. These could be defined to measure the application performance,
functionalities, etc. 

Unit tests do not cover a sequence of events, nor their results. A software component might be perfect in calculating the total of shopping carts,
but what if another crashes based on this output? However, without unit tests, debugging such a malfunctioning sequence would be difficult.
Thus, both tests compliment one another, and together they give a good overview of the software capabilities. The system tests highly depend on what is being tested, 
but the following guidelines could help:

- Provide a clear description of the scenario and the expected outcome.
- Provide a configuration of the application (if needed).
- Separate the system tests from the other tests.

## Further reading

Various other kinds of testing exist, but are beyond the scope of this workshop. Software testing is regarded as a profession on its own,
and more information about this topic can be found [here](https://www.geeksforgeeks.org/software-testing/types-software-testing/).
The sheer number of different tests can be overwhelming at first, but keep in mind that all of them serve a single purpose, 
to find faults in the software before the user does. 
