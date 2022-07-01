# 0x03-Python Data Structures
Higher level programming day 4

## Tasks
### 1. Print a list of integers
- Write a function that prints all integers of a list.
  - Conditions
    1. Format: one integer per line
    2. You are not allowed to import any module
    3. You are not allowed to cast integer to string
    4. You have to use `str.format()` to print integers

### 2. Secure access to an element in a list
- Write a function that retrieves an element from a list like in C.
  - Conditions:
    1. Prototype: `def element_at(my_list, idx):`
    2. if idx is negative, the function should return `None`
    3. if idx is out of range(> of number of element in `my_list`), the function should return `None`
    4. You are not allowed to import any module
    5. You are not allowed to use `try/except`

### 3. Replace element
- Write a function that replaces an element of a list at a specific position(like in C).
  - Conditions:
    1. Prototype: `def replace_in_list(my_list, idx, element):`
    2. if idx is negative, the function should not modify anything and returns the original list
    3. if idx is out of range(> of number of element in my_list), the function should not modify anything, and returns the original list
    4. You are not allowed to import any module
    5. You are not allowed to use `try/except`

### 4. Print a list of integers... in reverse!
- Write a function that prints all integers of a list, in reverse order.
  - Conditions:
    1. Prototype: `def print_reversed_list_integer(my_list=[])`
    2. Format: one integer per line
    3. You are not allowed to import any module
    4. You have to use `str.format()` to print integers

### 5. Replace in a copy
- Write a function that replaces an element in a list at a specific position without modifying the original list(like in C)
  - Conditions:
    1. Prototype: `def new_in_list(my_list, idx, element):`
    2. if idx is negative, the function should return a copy of the original list
    3. if idx is out of range(> of number of element in my_list), the function should return a copy of the original list
    4. You are not allowed to import any module
    5. You are not allowed to use `try/except`
