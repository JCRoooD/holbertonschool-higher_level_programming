# Python Input/Output Project

This Python project consists of a set of Python scripts that perform various input and output operations, including file reading and writing, JSON manipulation, and other data processing tasks. These scripts are created to meet specific project requirements. Each script serves a unique purpose and follows the best practices for Python coding.

## Project Files

The project includes the following Python scripts:

1. **Read File (0-read_file.py):**
   - Reads and prints the content of a text file.

2. **Write to a File (1-write_file.py):**
   - Writes a given string to a text file and returns the number of characters written.

3. **Append to a File (2-append_write.py):**
   - Appends a given string to the end of a text file and returns the number of characters added.

4. **To JSON String (3-to_json_string.py):**
   - Converts an object into a JSON string representation.

5. **From JSON String to Object (4-from_json_string.py):**
   - Converts a JSON string into a Python object.

6. **Save Object to a File (5-save_to_json_file.py):**
   - Writes an object to a text file in JSON format.

7. **Create Object from a JSON File (6-load_from_json_file.py):**
   - Reads a JSON file and creates a Python object from it.

8. **Class to JSON (8-class_to_json.py):**
   - Converts an object of a custom class to a JSON-compatible dictionary.

9. **Student Class (9-student.py):**
   - Defines a `Student` class with attributes and a method to convert the object to a dictionary.

10. **Student Class with Filter (10-student.py):**
    - Extends the `Student` class to filter attributes when converting to a dictionary.

11. **Student Class with File I/O (11-student.py):**
    - Adds file I/O capabilities to the `Student` class to save and load student data.

12. **Pascal's Triangle (12-pascal_triangle.py):**
    - Generates Pascal's triangle up to a specified number of rows.

## Testing
The project includes test scripts to validate the functionality of these Python scripts. These tests can be executed as follows:
shell
Copy code
python3 -m doctest ./tests/*