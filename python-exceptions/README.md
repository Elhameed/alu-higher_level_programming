#  Python - Exceptions

In this learning experience, I learnt the following:
- What’s the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What’s the purpose of catching exceptions
- How to raise a builtin exception
- When do we need to implement a clean-up action after an exception

## Function Prototypes 🛠️

Prototypes for functions written in this project:

| File                                     | Prototype                                               |
| ---------------------------------------- | ------------------------------------------------------- |
| `0-safe_print_list.py`                   | `def safe_print_list(my_list=[], x=0):`                 |
| `1-safe_print_integer.py`                | `def safe_print_integer(value):`                        |
| `2-safe_print_list_integers.py`          | `def safe_print_list_integers(my_list=[], x=0):`        |
| `3-safe_print_division.py`               | `def safe_print_division(a, b):`                        |
| `4-list_division.py`                     | `def list_division(my_list_1, my_list_2, list_length):` |
| `5-raise_exception.py`                   | `def raise_exception():`                                |
| `6-raise_exception_msg.py`               | `def raise_exception_msg(message=""):`                  |
| `100-safe_print_integer_err.py`          | `def safe_print_integer_err(value):`                    |
| `101-safe_function.py`                   | `def safe_function(fct, *args):`                        |
| `102-magic_calculation.py`               | `def magic_calculation(a, b):`                          |


## Tasks :page_with_curl:

**Task-0**: The [0-safe_print_list.py](./0-safe_print_list.py) file contains a function that prints `x` elements of a list.

**Task-1**: The [1-safe_print_integer.py](./1-safe_print_integer.py) file contains a function that prints an integer with `"{:d}".format()`.

**Task-2**: The [2-safe_print_list_integers.py](./2-safe_print_list_integers.py) file contains a function that prints the first `x` elements of a list and only integers.

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
