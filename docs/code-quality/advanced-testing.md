# Advanced testing features

!!! abstract "Overview"

    - What is code coverage?
    - What is test-driven development, and how can it be applied?

## Test coverage

When writing unit tests, it is good practice to cover the entire code base. This is known as the test "coverage", and
various tools exist to measure it. In Python, `pytest` can be combined with the [coverage](https://coverage.readthedocs.io/en/latest/) package to measure and report the coverage:

```shell
coverage run -m pytest
coverage report
```

With a coverage below 100%, two scenarios exist:

1. Part of the desired functionality remains untested, thus an extra unit test must be written to cover it.
2. The tests fully cover the desired functionality, and part of the source code can be removed, as it is redundant.

## Test-driven development

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
related objects, and identify potential use cases for inheritance, instead of refactoring the source code during development.
