#  Python - Classes and Objects

In this learning experience, I learnt the following:
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What is a method
- What is the special __init__ method and how to use it etc.


## Tasks :page_with_curl:

**Task-0**: The [0-square.py](./0-square.py) file contains an empty class `Square` that defines a square

**Task-1**: The [1-square.py](./1-square.py) file contains a class Square that defines a square by: (based on [0-square.py](./0-square.py))
- Private instance attribute: `size`
- Instantiation with `size` (no type/value verification)

**Task-2**: The [2-square.py](./2-square.py) file contains a class Square that defines a square by: (based on [1-square.py](./1-square.py))
- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
- `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
- if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`

**Task-3**: The [3-safe_print_division.py](./3-safe_print_division.py) contains a function that divides 2 integers and prints the result.

**Task-4**: The [4-list_division.py](./4-list_division.py) contain a function that divides element by element 2 lists.

**Task-5**: The [5-raise_exception.py](./5-raise_exception.py) file contains a function that raises a type exception.

**Task-6**: The [6-raise_exception_msg.py](./6-raise_exception_msg.py) file contains a function that raises a name exception with a message.

**Task-7**: The [100-safe_print_integer_err.py](./100-safe_print_integer_err.py) file contains a function that prints an integer.

**Task-8**: The [101-safe_function.py](./101-safe_function.py) file contains a function that executes a function safely.

**Task-9**: The [102-magic_calculation.py](./102-magic_calculation.py) file contains a Python function that does exactly the same as the following Python bytecode:
```sh
 3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        >>   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE
```
