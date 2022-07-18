#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
        print("Inside result: ")
    except ZeroDivisionError:
        pass
    finally:
        print()
        return div
