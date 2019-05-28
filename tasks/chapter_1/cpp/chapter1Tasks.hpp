/**
Build suite test
alias build="cxxtestgen --error-printer -o tests/Chapter1Test.cpp tests/Chapter1Test.h && g++  -ggdb -o tests/builds/chapter1 tests/Chapter1Test.cpp && chmod +x tests/builds/chapter1"
build
*/

/**
Check that all symbols enter the string only one time

How to test
build && tests/builds/chapter1 Chapter1Test testCheckAllSymbolsOnlyOne
*/

bool checkAllSymbolsOnlyOne(const char* string) {
    unsigned int symbols[256];

    for(int i = 0; i < 256; i++)
        symbols[i] = 0;

    for(int i = 0; string[i] != '\0'; i++) {
        symbols[string[i]] +=1;

        if (symbols[string[i]] > 1)
            return false;
    }

    return true;
}

#include <stdio.h>
/**
Reverse method for strings

How to test
build && tests/builds/chapter1 Chapter1Test testReverse
*/

void swap(std::string& string, std::size_t i, std::size_t j) {
    string[i] -= string[j];
    string[j] += string[i];
    string[i] = string[j] - string[i];
}

std::string reverse(std::string string) {
    std::size_t length = string.size();

    for(int i = 0; i < length / 2; i++) {
        swap(string, i, length - 1 - i);
    }

    return string;
}

/**
Check that one string is permutation of another

How to test
build && tests/builds/chapter1 Chapter1Test testCheckPermutation
*/

bool checkPermutation(const std::string& string1, const std::string& string2) {
    if (string1.size() != string2.size())
        return false;

    int mask[256];

    for (short int i = 0; i< 256; i++)
        mask[i] = 0;

    for(int i = 0; i < string1.size(); i++) {
        mask[string1[i]] += 1;
        mask[string2[i]] -= 1;
    }

    for(int i = 0; i < 256; i++)
       if (mask[i])
        return false;

    return true;
}

/**
Replace spaces to %20

How to test
build && tests/builds/chapter1 Chapter1Test testReplaceSpaceToPercent20
*/

char* replaceSpaceToPercent20(char* string, int length) {
    unsigned int spaces = 0;

    for (int i = 0; i<length; i++)
        if (string[i] == ' ')
            spaces++;

    int length_diff = 2*spaces;
    string[length + length_diff] = '\0';
    int right_pointer = length + length_diff - 1;

    for (int i = length -1; i >= 0; i--, right_pointer--) {
        if (string[i] == ' ') {
            string[right_pointer] = '0';
            string[right_pointer - 1] = '2';
            string[right_pointer - 2] = '%';
            right_pointer -= 2;
        } else {
            string[right_pointer] = string[i];
        }
    }

    return string;
}

/**
Compress the string

How to test
build && tests/builds/chapter1 Chapter1Test testCompressString

How to debug
build && gdb ./tests/builds/chapter1
set args Chapter1Test testCompressString
break chapter1Tasks.hpp:170
run
*/

#include <sstream>

unsigned int symbolsLength(unsigned int number) {
    unsigned int counter = 0;
    for(;number > 0; number = number / 10) {
        counter++;
    }

    return counter;
}

unsigned int newLength(const char* string) {
    int size = 0;
    char last = string[0];
    int count = 1;

    for( int i =1; i < strlen(string); i++) {
        if (last == string[i]) {
            count++;
        } else {
            size+= 1 + symbolsLength(count);
            last = string[i];
            count = 1;
        }
    }

    return size + 1 + symbolsLength(count);
}

unsigned int copyToString(std::string& string, const char* copied, unsigned int currentCursor) {
    unsigned int cursor = 0;
    while(copied[cursor] != '\0')
        string[currentCursor++] = copied[cursor++];

    return currentCursor;
}

unsigned int copyToString(std::string& string, char copied, unsigned int currentCursor) {
    string[currentCursor++] = copied;
    return currentCursor;
}

std::string itoa(unsigned int a) {
    std::stringstream result;
    result << a;
    return result.str();
}

std::string compressString(const char* string) {
    if (strlen(string) == 0)
        return string;

    unsigned int _newLength = newLength(string);

    if (_newLength >= strlen(string))
        return string;

    std::string result = std::string(_newLength, ' ');

    char last = string[0];
    int count = 1;
    unsigned int writeCursor = 0;

    for( int i =1; i < strlen(string); i++) {
        if (last == string[i]) {
            count++;
        } else {
            writeCursor = copyToString(result, last, writeCursor);
            writeCursor = copyToString(result, itoa(count).c_str(), writeCursor);
            last = string[i];
            count = 1;
        }
    }

    writeCursor = copyToString(result, last, writeCursor);
    writeCursor = copyToString(result, itoa(count).c_str(), writeCursor);

    return result;
}
