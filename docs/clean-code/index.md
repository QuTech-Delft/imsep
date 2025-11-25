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

## Quality

Tools like pylint etc.

## Docstrings

Introduction to type-hinting, different docstring formats, what should(n't) be in a docstring.
