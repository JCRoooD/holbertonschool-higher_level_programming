![GIF](https://media.giphy.com/media/HlqvH9JrahLZ6/giphy.gif)

# Python Rectangle Class

This is a Python project that defines a `Rectangle` class with various attributes and methods for working with rectangles.

## Project Structure

The project includes the following Python files:

1. `0-rectangle.py`: Defines an empty `Rectangle` class.
2. `1-rectangle.py`: Defines a `Rectangle` class with properties for `width` and `height`.
3. `2-rectangle.py`: Adds methods for calculating the area and perimeter of the rectangle.
4. `3-rectangle.py`: Enhances the class to provide string representation.
5. `4-rectangle.py`: Implements the `__repr__` method for a string representation that can be used with `eval()`.
6. `5-rectangle.py`: Adds functionality to handle instance deletion.
7. `6-rectangle.py`: Extends the class with a class attribute to count instances.
8. `7-rectangle.py`: Allows customizing the character used for string representation.
9. `8-rectangle.py`: Adds a static method for comparing rectangles and a class method to create squares.

## Usage

You can use the provided classes for working with rectangles and squares in your Python programs. Here's a basic example of how to use the `Rectangle` class:

```python
from 9-rectangle import Rectangle

# Create a rectangle instance
my_rectangle = Rectangle(4, 6)

# Calculate the area and perimeter
area = my_rectangle.area()
perimeter = my_rectangle.perimeter()

print(f"Area: {area}, Perimeter: {perimeter}")

# Customize the string representation character
my_rectangle.print_symbol = "X"

print(str(my_rectangle))