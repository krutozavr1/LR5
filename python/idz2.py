#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    first = float(input("First number: "))
    second = float(input("Second number: "))
    third = float(input("Third number: "))

    if 0 <= first <= 1:
        print(first, " is in range!")
    if 0 <= second <= 1:
        print(second, " is in range!")
    if 0 <= third <= 1:
        print(third, " is in range!")
