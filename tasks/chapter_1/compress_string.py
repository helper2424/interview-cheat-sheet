#!/usr/bin/python

# Compress string by algorithm aabbcc -> a2b2c2, if original shorter than result - return result
def compress_string(string):
    current_symbol = None
    counter = 0

    result = []
    length = len(string)
    for i in range(length):
        if string[i] == current_symbol:
            counter += 1
        else:
            if counter != 0:
                result.append(current_symbol)
                result.append(str(counter))
            current_symbol = string[i]
            counter = 1

        if i == length - 1:
            result.append(current_symbol)
            result.append(str(counter))

    result = ''.join(result)

    if len(result) >= length:
        return string

    return result