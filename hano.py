#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def move(n, a, b, c):

    if n == 0:
        return None
    move(n - 1, a, c, b)
    print(a, '->', c)
    move(n - 1, b, a, c)
    return



