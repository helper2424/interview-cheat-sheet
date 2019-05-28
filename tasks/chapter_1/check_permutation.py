#!/usr/bin/python

# Check that one string is permutaton of another
def is_permutation(string1, string2):
    length = len(string1)
    if length != len(string2):
        return False

    if length == 0:
        return True

    symbols = [0] * 256
    for i in range(length):
        symbols[ord(string1[i])] +=1
        symbols[ord(string2[i])] -= 1

    for i in range(256):
        if not symbols[i] == 0:
            return False

    return True