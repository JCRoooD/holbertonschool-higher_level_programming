![GIF](https://media.giphy.com/media/3oKIPjHCmuXqdVvak8/giphy.gif)

# Classes and Objects

This project involves creating a Python class called Square that defines a square with various attributes and methods. The project is divided into several tasks, each building upon the previous one.

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All code will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- All code files should end with a new line.
- The first line of all code files should be exactly `#!/usr/bin/python3`.
- A README.md file, at the root of the project folder, is mandatory.
- Your code should adhere to the pycodestyle (version 2.7.*) style guide.
- All code files must be executable.
- The length of your code files will be tested using wc.
- All modules should have documentation.
- All classes should have documentation.
- All functions (inside and outside a class) should have documentation.

### Tasks

#### Task 0: My first square
- Write an empty class `Square` that defines a square.
- You are not allowed to import any modules.

#### Task 1: Square with size
- Write a class `Square` that defines a square with a private instance attribute `size`.
- Instantiation with size (no type/value verification).
- You are not allowed to import any modules.

#### Task 2: Size validation
- Write a class `Square` that defines a square with a private instance attribute `size`.
- Instantiation with optional size: `def __init__(self, size=0)`.
- `size` must be an integer; otherwise, raise a `TypeError` exception with the message "size must be an integer".
- If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0".
- You are not allowed to import any modules.

#### Task 3: Area of a square
- Write a class `Square` that defines a square with a private instance attribute `size`.
- Instantiation with optional size: `def __init__(self, size=0)`.
- `size` must be an integer; otherwise, raise a `TypeError` exception with the message "size must be an integer".
- If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0".
- Public instance method `def area(self)` that returns the current square area.
- You are not allowed to import any modules.

#### Task 4: Access and update private attribute
- Write a class `Square` that defines a square with a private instance attribute `size`.
- Property `def size(self)` to retrieve it.
- Property setter `def size(self, value)` to set it.
- `size` must be an integer; otherwise, raise a `TypeError` exception with the message "size must be an integer".
- If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0".
- Instantiation with optional size: `def __init__(self, size=0)`.
- Public instance method `def area(self)` that returns the current square area.
- You are not allowed to import any modules.

#### Task 5: Printing a square
- Write a class `Square` that defines a square with a private instance attribute `size`.
- Property `def size(self)` to retrieve it.
- Property setter `def size(self, value)` to set it.
- `size` must be an integer; otherwise, raise a `TypeError` exception with the message "size must be an integer".
- If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0".
- Instantiation with optional size: `def __init__(self, size=0)`.
- Public instance method `def area(self)` that returns the current square area.
- Public instance method `def my_print(self)` that prints the square with the character `#`.
- If `size` is equal to 0, print an empty line.
- You are not allowed to import any modules.

#### Task 6: Coordinates of a square
- Write a class `Square` that defines a square with private instance attributes `size` and `position`.
- Property `def size(self)` to retrieve `size`.
- Property setter `def size(self, value)` to set `size`.
- `size` must be an integer; otherwise, raise a `TypeError` exception with the message "size must be an integer".
- If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0".
- Property `def position(self)` to retrieve `position`.
- Property setter `def position(self, value)` to set `position`.
- `position` must be a tuple of 2 positive integers; otherwise, raise a `TypeError` exception with the message "position must be a tuple of 2 positive integers".
- Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0))`.
- Public instance method `def area(self)` that returns the current square area.
- Public instance method `def my_print(self)` that prints the square with the character `#`.
- If `size` is equal to 0, print an empty line.
- Use `position` to determine the position of the square.
- You are not allowed to import any modules.

## How to Use

1. Clone the GitHub repository: [holbertonschool-higher_level_programming](https://github.com/Joshua7792/holbertonschool-higher_level_programming)
2. Navigate to the `python-classes` directory.
3. Create and run the Python scripts as shown in the task descriptions.

For example:

```bash
./0-main.py
./1-main.py
./2-main.py
# ...