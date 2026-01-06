from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self) -> int:
        """
        Calculates the area of the shape.

        Returns:
            Area of the shape.
        """


class Square(Shape):
    pass


class Rectangle(Shape):
    pass


class Circle(Shape):
    pass


class Elipse(Shape):
    pass


class Triangle(Shape):
    pass


class Trapezoid(Shape):
    pass
