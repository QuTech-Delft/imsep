# Advanced development cycle

This page is a continuation of the version control chapter, and addresses the more advanced topics related to Git:

- How can a branch model be set up for collaborative development?
- What are the causes of merge conflicts, and how can they be resolved?
- How to protect branches, and use merge requests to change them?
- How to review code from other collaborators?

## Commands

```shell
git push --set-upstream origin some-branch
git push -u origin some-branch

git push origin -d some-branch
git push origin -D some-branch

git push
```

## Branches

Lorem ipsum dolor sit amet consectetur adipiscing elit. Amet consectetur adipiscing elit quisque faucibus ex sapien. 
Quisque faucibus ex sapien vitae pellentesque sem placerat. Vitae pellentesque sem placerat in id cursus mi.

![Advanced cycle](../assets/images/git_2.jpg)

## Merge conflicts

Lorem ipsum dolor sit amet consectetur adipiscing elit. Adipiscing elit quisque faucibus ex sapien vitae pellentesque. 
Vitae pellentesque sem placerat in id cursus mi. Cursus mi pretium tellus duis convallis tempus leo. Tempus leo eu aenean sed diam urna tempor. 
Urna tempor pulvinar vivamus fringilla lacus nec metus.

```shell
cd path/to/dir
```

## Merge requests

Lorem ipsum dolor sit amet consectetur adipiscing elit. Adipiscing elit quisque faucibus ex sapien vitae pellentesque. 
Vitae pellentesque sem placerat in id cursus mi. Cursus mi pretium tellus duis convallis tempus leo. Tempus leo eu aenean sed diam urna tempor. 
Urna tempor pulvinar vivamus fringilla lacus nec metus.

## Code reviews

Lorem ipsum dolor sit amet consectetur adipiscing elit. Amet consectetur adipiscing elit quisque faucibus ex sapien. 
Quisque faucibus ex sapien vitae pellentesque sem placerat. Vitae pellentesque sem placerat in id cursus mi.

1. Lorem ipsum dolor sit amet consectetur adipiscing elit.
2. Lorem ipsum dolor sit amet consectetur adipiscing elit.
3. Lorem ipsum dolor sit amet consectetur adipiscing elit.
4. Lorem ipsum dolor sit amet consectetur adipiscing elit.

## Challenge time (...?)

1. Clone the IMSEP project from GitLab.
2. Make a feature branch named after the assigned shape (see snippet below).
3. Add the method and push to GitLab.
4. Create a merge request.
5. Check other merge requests.
6. Merge your own after approval.

```python
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
```
