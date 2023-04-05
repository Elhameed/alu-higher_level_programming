#  Python - Inheritance

In this learning experience, I have learned about the following:
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions

## __Pycache__ :file_folder:

The [__pycache__](./__pycache__) directory is a directory created by Python3 to store compiled bytecode files, which are generated to improve the performance of Python code execution.

## Test :file_folder:

The [test](./test/) directory is a directory that contains automated tests for the shell scripts of each problem in this repository.

## Tasks :page_with_curl:

**Task-0**: The [0-lookup.py](./0-lookup.py) file contains a function that returns the list of available attributes and methods of an object:

**Task-1**: The [1-my_list.py](./1-my_list.py) file contains a class `MyList` that inherits from `list`

**Task-2**: The [2-is_same_class.py](./2-is_same_class.py) file contains a function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`.

**Task-3**: The [3-is_kind_of_class.py](./3-is_kind_of_class.py) contains a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.

**Task-4**: The [4-inherits_from.py](./4-inherits_from.py) contain a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.

**Task-5**: The [5-base_geometry.py](./5-base_geometry.py) file contains an empty class `BaseGeometry`.

**Task-6**: The [6-base_geometry.py](./6-base_geometry.py) file contains a class `BaseGeometry` that raises an `Exception` with the message `area() is not implemented`

**Task-7**: The [7-base_geometry.py](./7-base_geometry.py) file contains a class `BaseGeometry` (based on `6-base_geometry.py`).

**Task-8**: The [8-rectangle.py](./8-rectangle.py) file contains  a class `Rectangle` that inherits from BaseGeometry (`7-base_geometry.py`).

**Task-9**: The [9-rectangle.py](./9-rectangle.py) file contains a class `Rectangle` that inherits from BaseGeometry (`7-base_geometry.py`). (task based on `8-rectangle.py`)

**Task-10**: The [10-square.py](./10-square.py) file contains a class `Square` that inherits from Rectangle (`9-rectangle.py`)

**Task-11**: The [11-square.py](./11-square.py) file contains a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).

**Task-12**: The [100-my_int.py](./100-my_int.py) file contains a class `MyInt` that inherits from `int`

**Task-13**: The [101-add_attribute.py](./101-add_attribute.py) file contains a function that adds a new attribute to an object if it’s possible
