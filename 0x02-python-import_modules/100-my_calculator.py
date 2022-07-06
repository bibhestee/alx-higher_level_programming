#!/usr/bin/python3
from sys import exit, argv
from calculator_1 import add, sub, mul, div


def cal():
    ch = ['', '', '', '']
    length = len(argv)
    if length < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        for i in range(0, 4):
            ch[i] = argv[i]
        a = int(ch[1])
        sign = ch[2]
        b = int(ch[3])
        if sign == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif sign == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif sign == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif sign == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == "__main__":
    cal()
