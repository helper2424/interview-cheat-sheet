#!/usr/bin/python

def is_loop(s1, s2):
    if len(s1) != len(s2) or len(s1) == 0:
        return False

    return s2 in s1 + s1