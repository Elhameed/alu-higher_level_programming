#  Python - Data Structures: Lists, Tuples

In this learning experience, I have learned how to work with lists and strings, use common list methods, use lists as stacks and queues, use list comprehensions to create new lists, and work with tuples. Additionally, I have learned about sequences, tuple packing and unpacking, and the del statement for deleting objects or elements from a data structure.

## __Pycache__ :file_folder:

The [__pycache__](./__pycache__) directory is a directory created by Python3 to store compiled bytecode files, which are generated to improve the performance of Python code execution.

## Function Prototypes 🛠️

Prototypes for functions written in this project:

| File                                     | Prototype                                               |
| ---------------------------------------- | ------------------------------------------------------- |
| `0-print_list_integer.py`                | `def print_list_integer(my_list=[]):`                   |
| `1-element_at.py`                        | `def element_at(my_list, idx):`                         |
| `2-replace_in_list.py`                   | `def replace_in_list(my_list, idx, element):`           |
| `3-print_reversed_list_integer.py`       | `def print_reversed_list_integer(my_list=[]):`          |
| `4-new_in_list.py`                       | `def new_in_list(my_list, idx, element):`               |
| `5-no_c.py`                              | `def no_c(my_string):`                                  |
| `6-print_matrix_integer.py`              | `def print_matrix_integer(matrix=[[]]):`                |
| `7-add_tuple.py`                         | `def add_tuple(tuple_a=(), tuple_b=()):`                |
| `8-multiple_returns.py`                  | `def multiple_returns(sentence):`                       |
| `9-max_integer.py`                       | `def max_integer(my_list=[]):`                          |
| `10-divisible_by_2.py`                   | `def divisible_by_2(my_list=[]):`                       |
| `11-delete_at.py`                        | `def delete_at(my_list=[], idx=0):`                     |

## Tasks :page_with_curl:

**Task-0**: The [0-add.py](./0-add.py) file contains a program that imports the function `def add(a, b):` from the file [add_0.py](./add_0.py) and prints the result of the addition `1 + 2 = 3`

**Task-1**: The [1-calculation.py](./1-calculation.py) file contains a program that imports functions from the file [calculator_1.py](./calculator_1.py), does some Maths, and prints the result.

**Task-2**: The [2-args.py](./2-args.py) file contains a program that prints the number of and the list of its arguments.

**Task-3**: The [3-infinite_add.py](./3-infinite_add.py) contains a program that prints the result of the addition of all arguments

**Task-4**: The [4-hidden_discovery.py](./4-hidden_discovery.py) contain a program that prints all the names defined by the compiled module `hidden_4.pyc`

**Task-5**: The [5-variable_load.py](./5-variable_load.py) file contains a program that imports the variable `a from the file [variable_load_5.py](./variable_load_5.py) and prints its value.

**Task-6**: The [100-my_calculator.py](./100-my_calculator.py) file contains a program that imports all functions from the file [calculator_1.py](./calculator_1.py) and handles basic operations.

**Task-7**: The [101-easy_print.py](./101-easy_print.py) file contains a program that prints `#pythoniscool`, followed by a new line, in the standard output without using `print` or `eval` or `open` or `import sys` in the file.

**Task-8**: The [102-magic_calculation.py](./102-magic_calculation.py) file contains a Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:
```sh
 3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
```

**Task-9**: The [103-fast_alphabet.py](./103-fast_alphabet.py) file contains a program that prints the alphabet in uppercase, followed by a new line.
