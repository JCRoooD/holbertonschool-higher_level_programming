![GIF](https://media.giphy.com/media/ugyC0Q2BoCbYs/giphy.gif)

## Almost a circle

## Requirements

### Python Scripts
- Use Python 3.8.5.
- Files should end with a new line.
- The first line of all your files should be `#!/usr/bin/python3`.
- A `README.md` file is mandatory.
- Code should adhere to PEP 8 style guidelines.
- All files must be executable.
- Document your modules, classes, and functions with docstrings.

### Python Unit Tests
- Use the `unittest` module.
- Organize test files within a `tests` folder.
- Test files should have names starting with "test_".
- Tests should be discoverable using `python3 -m unittest discover tests`.

## Tasks

### Task 0: If It's Not Tested, It Doesn't Work
All files, classes, and methods must be unit tested and adhere to PEP 8.

### Task 1: Base Class
Create a `Base` class in the `models` package. It should have an `__init__` method that manages the `id` attribute.

### Task 2: First Rectangle
Create a `Rectangle` class that inherits from the `Base` class. It should have attributes for width, height, x, y, and an `__init__` method.

### Task 3: Validate Attributes
Update the `Rectangle` class to validate attributes (width, height, x, y) in the constructor.

### Task 4: Area First
Add a method to the `Rectangle` class to calculate the area of a rectangle.

### Task 5: Display #0
Add a method to the `Rectangle` class to display the rectangle using "#" characters.

### Task 6: __str__
Override the `__str__` method in the `Rectangle` class to provide a string representation.

### Task 7: Display #1
Improve the `display` method to include x and y positioning.

### Task 8: Update #0
Add an `update` method to the `Rectangle` class to assign attributes using no-keyword arguments.

### Task 9: Update #1
Update the `update` method to accept keyworded arguments (key-value pairs).

### Task 10: Square Class
Create a `Square` class that inherits from the `Rectangle` class. The size attribute will be both width and height.

### Task 11: Square Size
Add a getter and setter for the `size` attribute in the `Square` class.

### Task 12: Square Update
Add an `update` method to the `Square` class that assigns attributes using arguments or key-value pairs.

### Task 13: Rectangle Instance to Dictionary
Add a `to_dictionary` method to the `Rectangle` class to return a dictionary representation.

### Task 14: Square Instance to Dictionary
Add a `to_dictionary` method to the `Square` class to return a dictionary representation.

### Task 15: Dictionary to JSON String
Add a `to_json_string` method to the `Base` class that converts a list of dictionaries to a JSON string.

### Task 16: JSON String to File
Add a `save_to_file` class method to the `Base` class that saves a list of instances to a JSON file.

### Task 17: JSON String to Dictionary
Add a `from_json_string` method to the `Base` class that converts a JSON string to a list of dictionaries.

### Task 18: Dictionary to Instance
Add a `create` method to the `Base` class that returns an instance with all attributes already set.

### Task 19: File to Instances
Add a `load_from_file` class method to the `Base` class that returns a list of instances from a JSON file.