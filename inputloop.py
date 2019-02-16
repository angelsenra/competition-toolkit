#!python3
# -*- coding: utf-8 -*-


def until(c="#"):
    out = []
    inp = input()
    while inp != c:
        out.append(inp)
        inp = input()
    return out


def ntimes(plus=0):
    out = []
    for i in range(int(input()) + plus):
        out.append(input())
    return out
