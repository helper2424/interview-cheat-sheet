#!/usr/bin/python

# Check that all symbols enter the string only one time
def check_count_symbols_equal_one(input):
    symbols = {}
    for i in range(len(input)):
        character = input[i]
        if symbols.get(character, None):
            return False

        symbols[character] = True

    return True

# Check that all symbols enter the string only one time
def check_count_symbols_equal_one2(input):
    symbols = [False] * 256
    for i in range(len(input)):
        character = ord(input[i])
        if symbols[character]:
            return False

        symbols[character] = True

    return True