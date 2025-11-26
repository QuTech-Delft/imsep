# Clean code

magine you are reading a well-organized book or following a simple recipe. Each step is clear, easy to understand, and there’s no unnecessary clutter. 
Now imagine the opposite, a messy, confusing set of instructions where you’re constantly backtracking to figure out what’s going on. 
This is the difference between “clean code” and messy code in programming. It promotes:

- Teamwork, other developers are less likely to get stuck deciphering code.
- Longevity, future changes can be applied more easily and the code tends to keep running longer without breaking.
- Quality, the chance of introducing bugs is smaller, and the overall user experience of the software is more likely to be positive.

!!! note

    The code examples used in this section are written in Python, but the principes they try to outline are applicable to any language!

## Design

Starting with a design can reduce the time spent coding tremendously. Constructing such a design for a new project is beyond the scope of this workshop,
but asking the following questions before, can already save some effort:

1. What is the [sequence](https://plantuml.com/sequence-diagram) of actions from user inputs to program outputs?
2. Which of these actions and data can be logically combined into [classes](https://plantuml.com/class-diagram)?
3. Can this sequence of actions be tested?
4. What would be a logical way to set up the package? To not end up with one `main` module, and a massive `helpers` module, for example.

## Readability

From the start, everything should be written in such a way to promote readability. From the highest level, e.g. modules, to function level,
the code should tell a story of what is happening. Variable names, and function parameters should promote in telling this story.
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

The profound difference in readability can clearly be seen from both examples. Even when codes solve more complex problems,
it can remain easily readable when sufficient effort is put in. A warning sign is when functions require more and more comments to make sense.
This is usually a good moment to refactor the original function into smaller ones with a specific purpose, review the design, etc.

!!! note

    Python has a wonderful module which highlights the importance of readability:

    ```python
    import this
    ```

    Not only is the printed message of use, have a look at the source code which generates the message!

## Style

As mentioned in the [code review](../version-control/advanced-cycle.md#code-reviews) section, immature teams tend to have
discussions about code style. "Should we use spaces between mathematical operations?", "In what order do we import other libraries?" are examples of such discussions.
Fortunately, as Python is a mature language, most of this has already been figured out, and guidelines exist known as [Python Enhancement Proposals](https://peps.python.org/)(PEP).
[PEP 8 ](https://peps.python.org/pep-0008/) focuses on code style, and packages exist which automatically enforce these guidelines. 

However, many good practices are not covered by these packages, and are often learnt through experience. 
The following examples highlight these with a short example in Python.

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
    
    The next example shows a case where separate lines would have improved readability massively:

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

5. The use of descriptive names. 

    Especially when coding mathematics, it is tempting to fall back to their abbreviations. Take the function for dynamic pressure for example:

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

Tools like pylint etc.

## Docstrings

Introduction to type-hinting, different docstring formats, what should(n't) be in a docstring.
