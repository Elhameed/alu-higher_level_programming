#  Python - Input/Output

In this learning experience, I have learned about the following:
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement
- What is `JSON`
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Function Prototypes 🛠️

Prototypes for functions written in this project:

| File                          | Prototype                                      |
| ----------------------------- | -----------------------------------------------|
| `0-read_file.py`                 | `def read_file(filename=""):`                             |
| `1-write_file.py`                | `def write_file(filename="", text=""):`                      |
| `2-append_write.py`          | `def append_write(filename="", text=""):`             |
| `3-to_json_string.py`       | `def to_json_string(my_obj):`          |
| `4-from_json_string.py`          | `def from_json_string(my_str):`             |
| `5-save_to_json_file.py`          | `def save_to_json_file(my_obj, filename):`                              |
| `6-load_from_json_file.py`          | `def load_from_json_file(filename):`    |
| `8-class_to_json.py`          | `def class_to_json(obj):`    |
| `12-pascal_triangle.py`          | `def pascal_triangle(n):`    |
| `100-append_after.py`          | `def append_after(filename="", search_string="", new_string=""):`    |

## Tasks :page_with_curl:

**Task-0**: The [0-read_file.py](./0-read_file.py) file contains a function that reads a text file (`UTF8`) and prints it to stdout

**Task-1**: The [1-write_file.py](./1-write_file.py) file contains a function that writes a string to a text file (`UTF8`) and returns the number of characters written:

**Task-2**: The [2-append_write.py](./2-append_write.py) file contains a function that appends a string at the end of a text file (UTF8) and returns the number of characters added

**Task-3**: The [3-to_json_string.py](./3-to_json_string.py) contains a function that returns the JSON representation of an object (string)

**Task-4**: The [4-from_json_string.py](./4-from_json_string.py) contain a function that returns an object (Python data structure) represented by a JSON string

**Task-5**: The [5-save_to_json_file.py](./5-save_to_json_file.py) file contains a function that writes an Object to a text file, using a JSON representation

**Task-6**: The [6-load_from_json_file.py](./6-load_from_json_file.py) file contains a function that creates an Object from a “JSON file”:

**Task-7**: The [7-add_item.py](./7-add_item.py) file contains a script that adds all arguments to a Python list, and then save them to a file.

**Task-8**: The [8-class_to_json.py](./8-class_to_json.py) file contains a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object
