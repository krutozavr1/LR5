#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    day_cnt = 1
    new_words = 5
    words_cnt = 0

    while day_cnt <= 10:
        words_cnt += new_words
        new_words += 2
        day_cnt += 1

    print(words_cnt)
