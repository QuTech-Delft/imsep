# Code quality

!!! abstract "Overview"
   
    - Why is code quality of importance?
    - What elements define the quality of code?
    - What are best practices to follow for each of these elements?

## Clean code

Imagine you are reading a well-organized book or following a simple recipe. Each step is clear, easy to understand, and there’s no unnecessary clutter. 
Now imagine the opposite, a messy, confusing set of instructions where you’re constantly backtracking to figure out what’s going on. 
This is the difference between “clean code” and messy code in programming. Clean code promotes:

- Teamwork, other developers are less likely to get stuck deciphering code.
- Longevity, future changes can be applied more easily and the code tends to keep running longer without breaking.
- Quality, the chance of introducing bugs is smaller, and the overall user experience of the software is more likely to be positive.

!!! note

    The snippets used in this chapter are written in Python, but the principes they try to outline are applicable to any language!

## Design

In mechanical engineering, engineers don't just start building. Usually, an elaborate design process precedes the manufacturing and test phases.
Software engineering has the benefit of not requiring materials, but the same principles apply. 
Constructing a complete design from scratch is beyond the scope of this workshop,
but asking the following questions, can already save some effort in the development phase:

1. What does the user expect from the program?
2. What is the [sequence](https://plantuml.com/sequence-diagram) of actions from the program to meet these expectations?
3. Which of these actions and associated data can be logically combined into [classes](https://plantuml.com/class-diagram)?
4. Can this sequence of actions be tested?
5. What would be a logical way to set up the package? To not end up with one `main` module, and a massive `helpers` module, for example.

## Readability

Right from the start, everything should be written in such a way to promote readability. From the highest level, e.g. modules, to function level,
it should tell a story of what is happening. Variable names, and function parameters should further promote in telling this story.
A tedious function can quickly become unreadable when this ideology is not followed:

!!! exercise "What is going on?"
    
    ```python
    def calc_t(c, disc):
        if not c or not (0 <= disc <= 1):
            raise ValueError
        return (1 - disc) * sum(i["Pr"] * i["Qu"] for i in c)
    ```

Before opening the code block below, realise how much time it took to decipher these lines of (independent) code. 
Now imagine a code base which is written entirely like this, with different function calls within each function, 
combined with specific syntax from other libraries, like Numpy or Pandas...

??? solution "Oh ..."

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

The profound difference in readability can clearly be seen. Even when codes solve more complex problems,
it can maintain its readability when sufficient effort is put in. A warning sign is when functions require more and more comments to make sense.
This is usually a good moment to refactor the original function into smaller ones with a specific purpose, review the design, etc.

!!! note

    Python has a wonderful built-in package which highlights the importance of readability:

    ```python
    import this
    ```

    Not only is the printed message of use, have a look at the source code which generates the message!

## Style

As mentioned in the [code review](../version-control/advanced-cycle.md#code-reviews) section, immature teams tend to have
discussions about code style. "Should we use spaces between mathematical operations?", "In what order do we import other libraries?" are examples of such discussions.
Fortunately, as Python is a mature language, most of this has already been figured out. Guidelines exist known as the [Python Enhancement Proposals](https://peps.python.org/) (PEP).

[PEP 8](https://peps.python.org/pep-0008/) focuses on code style, and packages exist which automatically enforce these guidelines.
However, many good practices are not covered by these packages, and are often learnt through experience. 
The following examples highlight these with a Python snippet:

1. The use of visual clustering, so that parts of the code that “belong” together are easily recognisable:

    !!! example "No clustering"
         
         ```python
         def calculate_total(cart, discount_rate):
            if not cart:
               raise ValueError("Cart cannot be empty.")
            if not (0 <= discount_rate <= 1):
               raise ValueError("Discount rate must be between 0 and 1.")
            subtotal = sum(item['price'] * item['quantity'] for item in cart)
            discount = subtotal * discount_rate
            total = subtotal - discount
            return total
         ```
    
    Each cluster could be seperated by comment, however, when written properly, these comments are often not needed.
    In the example below, these (redundant) comments are given to illustrate the effect of clustering.
    
    !!! example "Clustered"
         
         ```python
         def calculate_total(cart, discount_rate):
            
            # check inputs
            if not cart:
               raise ValueError("Cart cannot be empty.")
            if not (0 <= discount_rate <= 1):
               raise ValueError("Discount rate must be between 0 and 1.")
            
            # calculate totals
            subtotal = sum(item["price"] * item["quantity"] for item in cart)
            total = (1 - discount) * subtotal
            
            # return total
            return total
         ```

2. Declare variables close to their usage:
    
    !!! example "All placed on top"
       
        ```python
        def calculate_average_grades(students):
            total_grades = 0
            count = len(students)
    
            if not students:
                raise ValueError("The students list cannot be empty.")
    
            for student in students:
                total_grades += student['grade']
    
            average_grade = total_grades / count
    
            return average_grade
        ```
    
    !!! example "Declared close to their usage"
       
        ```python
        def calculate_average_grades(students):
    
            if not students:
                raise ValueError("The students list cannot be empty.")
            
            total_grades = 0
    
            for student in students:
                total_grades += student["grade"]
    
            count = len(students)
            average_grade = total_grades / count
    
            return average_grade
        ```

3. Only summarise code when it remains readable:

    !!! example "Previous example as a one-liner"

        ```python
        def calculate_average_grades(students):
    
            if not students:
                raise ValueError("The students list cannot be empty.")
            
            return sum([student["grade"] for student in students]) / len(students)
        ```
    
    The next example shows a case where separate lines would have improved readability:

    !!! example "Incomprehensible one-liner"
    
        ```python
        def get_unique_even_cubed_double_of_positive_numbers(numbers):
            return list(map(lambda x: round(x**3, 2), filter(lambda x: x % 2 == 0, set(map(lambda y: y * 3, [i for i in numbers if i > 0])))))
        ```

    !!! exercise
    
        What should the previous function return with an input of `[1, 2, 3]`?

    ??? solution
        
        Don't attempt to understand this code, life is too short! Make a respectiful comment to the developer about the code style instead.

4. Logical flow of classes and/or functions:

    !!! example "random order"

        ```python
        def main():
            helper_1()
            helper_2()

        def helper_2():
            helper_3()
            helper_4()

        def helper_3():
            pass
        
        def helper_1():
            pass

        def helper_4():
            pass
        ```
    
    !!! example "ordered"

        ```python
        def main():
            helper_1()
            helper_2()

        def helper_1():
            pass

        def helper_2():
            helper_3()
            helper_4()

        def helper_3():
            pass

        def helper_4():
            pass
        ```
    
    !!! note
        
        In classes there is the extra element of different method types, e.g. a class method after a static method.
        There is no right or wrong in mixing, as long as it makes sense to the reader.

5. The use of descriptive names:

    Especially when coding mathematics, it is tempting to fall back to their mathematical descriptors. Take the function for dynamic pressure for example:

    !!! example "Dynamic pressure"
    
        $$
        p = \frac{1}{2} * \rho * V^2
        $$
    
    How to code this? It matters on the context. If it is software coded by mainly physicists for other physicists in the same field,
    falling back to the mathematical descriptors could be acceptable (whilst using a descriptive function name):
    
    !!! example "Mathematical code"

        ```python
        def calculate_dynamic_pressure(rho: float, v: float) -> float:
            return 0.5 * rho * v ** 2
        ```
    
    Note that a lowercase `v` is used. Style guidelines for the programming language should always come first, and mathematical styling second.
    In Python, an uppercase name suggests either a class or a type, thus using `V` would be plain wrong here. If this causes a clash with another function,
    it is recommended to switch back to descriptive names instead.

    !!! warning
    
        Imagine having two mathematical functions both taking `v` as an input, but it signifies something else. One the uppercase mathemetical descriptor,
        and the other one the lowercase. Debugging this piece of code would be unnecessarily difficult.

    When it is clear that developers without in-depth knowledge of the mathematical methods will collaborate, descriptive names should be used.
    This also includes the scenario in which the development team consists of physicists, but the software will be maintained by non-physicists.
    Using the same example, but descriptive:

    !!! example "Descriptive code"

        ```python
        def calculate_dynamic_pressure(density: float, velocity: float):
            return 0.5 * density * velocity ** 2
        ```

    There are countless examples where abbreviated variable names cause confusion, and contests actually exist in which to write the most incomprehensible code as possible,
    but this is usually not desired in the working environment. 

## Quality

Next to the styling and readability, the actual quality of the code is of importance as well. This can range from unnecessary duplication, 
unused variables, to more error-prone mistakes, like re-declaring the same variable with a different type. This would be impossible in a language as C++,
but is allowed in a dynamically-typed language like Python. 

Various tools exist to help improve the code quality, and mature teams usually have these checks enforced. For Python,
a tool like [Pylint](https://www.pylint.org/) can help identify "[code smells](https://refactoring.guru/refactoring/smells)" and most IDEs have built-in quality checks as well.
Running it on the following piece of code will result in a few suggestions:

!!! example "bad_example.py"
    
    ```python
    import math
    
    def addNumbers(a, b): return a + b
    
    
    def divide_numbers(a, b):
        if b == 0:
            print("Cannot divide by zero")
            return None
        return a / b
    ```
    
    ```text
    ************* Module bad_example
    bad_example.py:34:0: C0304: Final newline missing (missing-final-newline)
    bad_example.py:1:0: C0114: Missing module docstring (missing-module-docstring)
    bad_example.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
    bad_example.py:4:0: C0103: Function name "addNumbers" doesn't conform to snake_case naming style (invalid-name)
    bad_example.py:4:22: C0321: More than one statement on a single line (multiple-statements)
    bad_example.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
    bad_example.py:1:0: W0611: Unused import math (unused-import)
    
    -----------------------------------
    Your code has been rated at 5.91/10
    ```

For Python specifically, type-hinting is good practice. It is not enforced, but it makes the code:

1. easier to use.
2. less likely to crash.
3. help developers identify mistakes in their code.

A full explanation of type-hinting is beyond the scope of this workshop, but the basics can be applied easily. 
Each parameter and return value should be type-hinted, and cases when it can be unclear what the type should be:

```python
class MyClass:

    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
        self.c: list[int] = []
    
    def my_method(self, c: int) -> int:
        self.c.append(c)
        return self.a + self.b + sum(self.c)


def my_function(my_class: MyClass) -> None:
    print(my_class.a + my_class.b)
```

[Mypy](https://mypy.readthedocs.io/en/stable/#) can be used for both checking type-hinting and explanations as to why certain variables are incorrectly typed.
Sometimes, it can be an arduous job to correctly type-hint code (especially with Mypy in "strict" mode), but it will always lead to better code quality.

## Docstrings

Certain elements should always be in a docstring, namely:

- A brief description of what the function does.
- What are the inputs, their type, with a brief description.
- What does the function return, if anything?

Optionally, it is nice to have:

- A list of the errors which can be raised with their description.
- If the docstring start to turn into a story, or if it simply cannot be properly described with text alone, it is recommended to include a "See Also" section.
It can contain a link to the design documentation, research paper, etc.
- Examples of what the function calculates based on the inputs, e.g.:

    ```python
    from numpy import arange, argmax, round as numpy_round, zeros
    from numpy.typing import ndarray
    
    def convert_array(inputs: ndarray) -> ndarray:
        """
        Convert a floating point array into an array with one true index per row.
    
        Args:
            inputs: Array containing floating point values between 0 and 1.
    
        Returns:
            Array with one true index per row.
    
        Examples:
            - [[0.4], [0.5], [0.6]] is converted to [[0], [0], [1]].
            - [[0.1, 0.2, 0.7], [0.4, 0.4, 0.2], [0.3, 0.3, 0.4]] is converted to [[0, 0, 1], [1, 0, 0], [0, 0, 1]].
        """
        if inputs.shape[-1] > 1:
            maximums = argmax(inputs, axis=1)
    
            outputs = zeros(shape=inputs.shape)
            outputs[arange(outputs.shape[0]), maximums] = 1
    
        else:
            outputs = numpy_round(inputs)
    
        return outputs
    ```
  
    In the above example, it would be difficult to understand the description and associated syntax. The examples make the calculations feel more intuitive.

## Further reading

[Next up](./basic-testing.md) is an introduction to code testing. On this page, the basics of unit testing are covered, with an introduction to system tests. 
The subsequent [page](./advanced-testing.md) delves further into unit testing with more advanced topics, like code coverage.
