C++
1)What problem do you  see here
```
operator int() const {
    return *this;
}
```

Problem with recurent call of this method, when we use it like this
int i = (new Test);

2)2 ** 64 = ?
1.8 * 10^19

3) -1 in binary format:
0xffffffff (for 32 bit system)

4) What is pure virtual call?
Happen when try to call virtual method without implmentation.

```#include <iostream>
 
class Base
{
public:
    Base() { init(); }
    ~Base() {}
 
    virtual void log() = 0;
 
private:
    void init() { log(); }    
};
 
class Derived: public Base
{
public:
    Derived() {}
    ~Derived() {}
 
    virtual void log() { std::cout << "Derived created" << std::endl; }
};
 
int main(int argc, char* argv[])
{
    Derived d;
    return 0;
}```

May happen in constructor and destructor!

5)
У вас есть исходный код приложения на языке С, которое аварийно завершается после запуска. После десяти запусков в отладчике вы обнаруживаете, что каждый раз программа падает в разных местах. Приложение однопоточное и использует только стандартную библиотеку С. Какие ошибки могут вызвать падение приложения? Как вы проверите каждую?

1 - Случайная пеменнная
2 - неинициализированная переменная
3 - кончилась память
4 - конфликт с другими приложениями

6) What are doing this code ((n & (n — 1)) == 0)?
It's figuring out if n is either 0 or an exact power of two.

7) https://tproger.ru/problems/print-the-last-k-lines-of-the-input-file-in-c-plus-plus/


8) https://tproger.ru/articles/problems/

9) What is virtual function?
Mechanism fore realisation of polimorhism in c++. We can use base class object with implementation of child classes.

10) What is a virtual destructor?
Easy
11) What different erase and remove?

12) What is volatile?

13) What is a friend function?
A function which is not a member of the class but still can access all the member of the class is called so. To make it happen we need to declare within the required class following the keyword ‘friend’.

14) Can you reqlize your class with smart pointers?

15) Who create C++?

16) What is mutable?

17)What output
#include <iostream>

int main(int argc, const char * argv[]) {
    int a[] = {1, 2, 3, 4, 5, 6};
    std::cout << (1 + 3)[a] - a[0] + (a + 1)[2];
}

18) Почему в C++ нужно использовать new вместо теплого лампового malloc()?

Потому что malloc() тупо выделяет блок памяти и возвращает этот блок программисту. А new выделяет память и вызывает конструктор объекта. Тоже самое относится к delete и free(). delete вызывает деструктор и освобождает память. free() просто освобождает память. Также есть размещающий new, который создает объект в уже выделенной вами памяти

19)Какой будет вывод в консоль и почему?
Листинг программы:
#include <iostream> 
#include <string> 
 
void print(int v) 
{ 
    std::cout << "int:" << v << std::endl; 
} 
 
void print(bool v) 
{ 
    std::cout << "bool:" << v << std::endl; 
} 
 
void print(std::string v) 
{ 
    std::cout << "std::string:" << v << std::endl; 
} 
 
int main() 
{ 
    print(1); 
    print(true); 
    print("Hello world"); 
} 

int:1 
bool:1 
bool:1 

20) . Можете ли вы написать код для переворота строки?

21) Как защитить объект от копирования?

22) В чем разница между struct и class?
class - по умолчанию приватные мемберы

23) Для чего используется вызов throw без аргументов?

24)
std::string source = "()()))()()";


bool check(const std::string &source ) {
    std::stack<char> stack = std::stack<char>();
    for (auto iter = source.begin(); iter != source.end(); iter++) {
        if (iter == '(')
        {
            stack.push(iter);
            continue;
        }
            
        if (iter == ')') {
            if (stack.empty())
                return false;
                
            stack.pop();
        }
    }    
    
    if (stack.empty())
        return true;
        
    return false;
}


//------------------------

uint64_t a = 12;
uint64_t b = 1001;

uint8_t bitsDifferent(uint64_t a, uint64_t b) {
    uint64_t c = a ^ b;
    uint8_t result = 0;
    
    for( uint8_t i = 0; i < 64; i++) {
        if (c & 1) 
            result++;
            
        c = c >> 1;
    }
            
    return result;
}


__
void deep_recursion()
{
    int i[1000000];
    deep_recursion();
}

int main(int argc, char **argv)
{
    deep_recursion();
    return 0;
}

int main(int argc, char **argv)
{
    long unsigned int i = 100000000;
    while(true)
        (*(int*)i++) = 1;
    return 0;
}

int main(int argc, char **argv)
{
    while(true)
        int *i = new int[400000000];
    return 0;
}

unsigned int fib(unsigned int i)
{
    if (i == 0 || i == 1)
        return i;

    return fib(i - 1) + fib(i - 2);
}

If we doesn't have any memory limits we can create Map with the next structure. Key is an item pointer(address) and value is boolean flag. Next, we go through the linked list and if Map has key with current linked list item then there is loop. In other way we add linked list item to Map and go forward.
If we have memory limitations we can use classical algorithm with two pointers F and S. We go through linked list and move pointer F to 1 step and pointer S to 2 steps. If F and S see to same item then there is loop.

std::string reverse(std::string str, unsigned int position = 1)
{
    if (str.size() == 0)
        return str;

    if (position >= str.length())
        return std::string(1, str[0]);

    return str[str.length() - position] + reverse(str, position + 1);
}

25) Reverse string

void reverse(std::string & str)
{
    if (!str.size())
    return;

    for (auto i = 0; i < str.size() / 2 - 1; i++)
    {
        auto last_pos = str.size() - 1 - i;
        str[i] = str[i] ^ str[last_pos];
        str[last_pos] = str[i] ^ str[last_pos];
        str[i] = str[i] ^ str[last_pos];
    }
}

26) Write quick sort

void quick_sort(std::vector<int> source) 
{

}

27) Write heap sort


28) https://www.toptal.com/algorithms/interview-questions


29)----------
What will be the output when the following code is executed? Explain.

```
#include <stdio.h>
#define SQUARE(a) (a)*(a)

int main() {
    printf("%d\n", SQUARE(4));
    int x = 3;
    printf("%d\n", SQUARE(++x));
}
```

16
25 OR 20, depend on calculator

30) Why is it usually a bad idea to use gets()? Suggest a workaround.

The function gets() reads characters from the stdin and stores them at the provided input buffer. However, gets() will keep reading until it encounters a newline character. Unless the buffer is large enough, or the length of the line being read is known ahead of time, gets() can potentially overflow the input buffer and start overwriting memory it is not supposed to, wreaking havoc or opening security vulnerabilities.

One way to work around this issue is to use fgets(). It allows you to put a limit on the maximum number of characters to read:

fgets(b, 124, stdin);

31) What is the difference between structs and unions?

In struct data saved in different memoty locations. In union values stored in one memory location.

If you change some field of union it will change other fields values. So in struct all fields are independent

32)What is a void pointer? Can you dereference a void pointer without knowing its type?

void pointer is a pointer to some data and you dont' know type of this data. You can't dereference pointer without knowing data type.

33) What is being declared in the following statement?
char (*x) (char*);

pointer x to function, which receive pointer to character and return char

34) What is the difference between #include "..." and #include <...>?

<> - compiler search for source/header file just in system (or declared through flags for compiler) directories
"" - search in system directories + search in current dorectory (pwd for compiler)

35) What are dangling pointers? How are dangling pointers different from memory leaks?

Dangling pointers are those that point to memory locations which have already been freed. For example:

int *a = malloc(sizeof(int));
free(a);
// a is now a dangling pointer
Memory leaks are quite the opposite of dangling pointers. Memory leaks happen when memory locations are not freed, but there is no way to refer to them (i.e., no pointers are pointing to them).

int *a = malloc(sizeof(int));
a = 0;
// now a no longer points to the memory that we just allocated, causing a memory leak
Unlike higher-level languages with garbage collectors, it is critical to always keep track of allocated memory when programming in C.

36) This code snippet converts a floating point number to an integer using casting:

float f = 1.0;

int i1 = (int) f;
int i2 = * (int *) &f;

printf("%d\n, i1);
printf("%d\n, i2);
The following output is produced:

1
1065353216
Can you explain why results differ?

The first casting operation properly converts from a floating point number to an integer, as specified by the C standard. The second conversion, however, is first casting a float pointer to an integer pointer which is then dereferenced to get the final result. This way the compiler is effectively treating raw bits from a float (typically stored in IEEE floating point format) as if they were bits of an integer. Besides getting a wrong result you are potentially doing a “bad read” operation, in cases where sizeof(int) is greater than sizeof(float) (e.g. on some 64-bit architectures).

Although this particular code is unlikely, it demonstrates one of the risks involved in typecasting when only a pointer to the variable to be cast is available. In practice, the pointer must be dereferenced before it is cast

37)What is the output of the following program if run on a 32-bit operating system?

#include
int  main()
{
    int a=-2;
    printf("%x",a>>3);
}

----

In a 32 bit operating system, integers are stored as 4 bytes.

Since a is negative, it will be stored in 2’s complement. When an integer is negative and we want to right shift by “n” bits, we need to prepend ones (not zeros!) to the left hand side. The answer would therefore be 0xFFFF (%x prints out value in hex).

38) What will the line of code below print out and why?

cout << 25u - 50;

---
4294967271

39) C++ supports multiple inheritance. What is the “diamond problem” that can occur with multiple inheritance? Give an example.

Diamong problem -when we have one parent class, two children class and one class, which is children of this two children classes. ANd all this classes will have one method which will overloaded. And we have undefined way to detect what this method should be for last class.

diamond because inheritance diagram looks like diamond.

  a
 / \
b   c
 \ /
  d

40) What is the error in the code below and how should it be corrected?

  my_struct_t *bar;
  /* ... do stuff, including setting bar to point to a defined my_struct_t object ... */
  memset(bar, 0, sizeof(bar));


  we should use `sizeof(*bar)`, bacause `sizeof(bar)` is a size if pointer

41)What will i and j equal after the code below is executed? Explain your answer.

```
int i = 5;
int j = i++;
```

i == 6
j == 5

42) Assuming buf is a valid pointer, what is the problem in the code below? What would be an alternate way of implementing this that would avoid the problem?

```
size_t sz = buf->size();
while ( --sz >= 0 )
{
    /* do something */
}
```

While will be infinity loop, because size_t is a uint64_t which can't be less then 0

43)Consider the two code snippets below for printing a vector. Is there any advantage of one vs. the other? Explain.

Option 1:

```
vector vec;
/* ... .. ... */
for (auto itr = vec.begin(); itr != vec.end(); itr++) {
    itr->print();
}
```

Option 2:

```
vector vec;
/* ... .. ... */
for (auto itr = vec.begin(); itr != vec.end(); ++itr) {
    itr->print();
}
```

It has identical behavior. Option with post increment will work less efiicienlty, because post increment create variable duplicate.

44)Implement a template function IsDerivedFrom() that takes class C and class P as template parameters. It should return true when class C is derived from class P and false otherwise.

#include <type_traits>

template <class C, class P> bool isDereviedFrom() {
    return std::is_base_of<C, P>::value;
};


45) Implement a template boolean IsSameClass() that takes class A and B as template parameters. It should compare class A and B and return false when they are different classes and true if they are the same class.

....

46) Is it possible to have a recursive inline function?

Compiler will not create inline function in this case.

47) What is the output of the following code:

```
#include <iostream>

class A {
public:
    A() {}
    ~A() {
        throw 42;
    }
};

int main(int argc, const char * argv[]) {
    try {
        A a;
        throw 32;
    } catch(int a) {
        std::cout << a;
    }
}
```

Will crashed with exception. because when A desctroyed it will generate unhandled exception.

48) You are given library class Something as follows:

class Something {
public:
    Something() {
        topSecretValue = 42;
    }
    bool somePublicBool;
    int somePublicInt;
    std::string somePublicString;
private:
    int topSecretValue;
};
Implement a method to get topSecretValue for any given Something* object. The method should be cross-platform compatible and not depend on sizeof (int, bool, string).


--- 

#include <iostream>

class Something {
public:
    Something() {
        topSecretValue = 42;
    }
    bool somePublicBool;
    int somePublicInt;
    std::string somePublicString;
private:
    int topSecretValue;
};

class SomethingClone {
public:
   SomethingClone() {
        topSecretValue = 42;
    }
    bool somePublicBool;
    int somePublicInt;
    std::string somePublicString;
    int topSecretValue;
};

int main(void) {
        Something a;
        SomethingClone * b = reinterpret_cast<SomethingClone *>(&a);
        std::cout << b->topSecretValue;
}

49) Implement a void function F that takes pointers to two arrays of integers (A and B) and a size N as parameters. It then populates B where B[i] is the product of all A[j] where j != i.

For example: if A = {2, 1, 5, 9}, then B would be {45, 90, 18, 10}
#include <algorithm>
#include <iostream>
using namespace std;
void f(int *a, int *b, size_t n) {
    int common_product = 1;
    int zeros = 0;
    for(size_t i = 0; i < n; i++){
        if (a[i] == 0) {
            zeros += 1;

            if (zeros < 2)
                continue;
        }
        common_product *= a[i];
    }

    if (zeros >= 2) {
        fill(b, b+n, 0);
        return;
    }

    for (size_t i = 0; i < n; i++) {
        if (zeros == 1) {
            if (a[i] == 0) 
                b[i] = common_product;
            else
                b[i] = 0;
            continue;
    }
        
        b[i] = common_product / a[i];
    }
}

#define N 4

int main(int argc, char ** argv) {
    
  int n = N;  
  int  B[N];

  int A[N] = {2, 1, 5, 9};
  f(A,B,n);

  for(size_t i = 0; i < n; i++)
    std::cout << A[i] << ",";

  std::cout << std::endl;

    for(size_t i = 0; i < n; i++)
        std::cout << B[i] << ",";
  
  std::cout << std::endl;
  
  return 0;
}

but I see the problem with integer overloading

50) When you should use virtual inheritance?

While it’s ideal to avoid virtual inheritance altogether (you should know how your class is going to be used) having a solid understanding of how virtual inheritance works is still important:

So when you have a class (class A) which inherits from 2 parents (B and C), both of which share a parent (class D), as demonstrated below:

#include <iostream>

class D {
public:
    void foo() {
        std::cout << "Foooooo" << std::endl;
    }
};


class C:  public D {
};

class B:  public D {
};

class A: public B, public C {
};

int main(int argc, const char * argv[]) {
    A a;
    a.foo();
}
If you don’t use virtual inheritance in this case, you will get two copies of D in class A: one from B and one from C. To fix this you need to change the declarations of classes C and B to be virtual, as follows:

class C:  virtual public D {
};

class B:  virtual public D {
};

Used to solve diamond problem.

51) Is there a difference between class and struct?

By default class have private members, struct have public members.

52) What is the output of the following code:

```
#include <iostream>

int main(int argc, const char * argv[]) {
    int a[] = {1, 2, 3, 4, 5, 6};
    std::cout << (1 + 3)[a] - a[0] + (a + 1)[2];
}
```

8

53) What is the output of the following code:

```
#include 

class Base {
    virtual void method() {std::cout << "from Base" << std::endl;}
public:
    virtual ~Base() {method();}
    void baseMethod() {method();}
};

class A : public Base {
    void method() {std::cout << "from A" << std::endl;}
public:
    ~A() {method();}
};

int main(void) {
    Base* base = new A;
    base->baseMethod();
    delete base;
    return 0;
}
```

from A
from A
from Base <- thi swill called on the stage of Base destroying, where A#method doesn't exist

54) Explain the volatile and mutable keywords

The volatile keyword informs the compiler that a variable will be used by multiple threads. Variables that are declared as volatile will not be cached by the compiler to ensure the most up-to-date value is held.

The mutable keyword can be used for class member variables. Mutable variables are allowed to change from within const member functions of the class.

55)How many times will this loop execute? Explain your answer.

```
unsigned char half_limit = 150;

for (unsigned char i = 0; i < 2 * half_limit; ++i)
{
    // do something;
}
```

infinity loop, because i unsigned char and max uchar < 300

56)How can you make sure a C++ function can be called as e.g. void foo(int, int) but not as any other type like void foo(long, long)?

Implement foo(int, int)… ~~~cpp

void foo(int a, int b) { // whatever } ~~~

…and delete all others through a template:

`template <typename T1, typename T2> void foo(T1 a, T2 b) = delete;`

57) What is the problem with the following code?

```
class A
{
public:
A() {}
~A(){}
};

class B: public A
{
public:
B():A(){}
~B(){}
}

int main(void)
{
  A* a = new B();
  delete a;
}
```

class A should have virtual destructor, because delete a; will not clean memory for B;

58) What wil happen if we avoid `return` statement in `main`;

Implicitly `return 0`;

59)Is you allowed to have a static const member function? Explain your answer.

A const member function is one which isn’t allowed to modify the members of the object for which it is called. A static member function is one which can’t be called for a specific object.

Thus, the const modifier for a static member function is meaningless, because there is no object associated with the call.

A more detailed explanation of this reason comes from the C programming language. In C, there were no classes and member functions, so all functions were global. A member function call is translated to a global function call. Consider a member function like this:

void foo(int i);
A call like this:

obj.foo(10);
…is translated to this:

foo(&obj, 10);
This means that the member function foo has a hidden first argument of type T*:

void foo(T* const this, int i);
If a member function is const, this is of type const T* const this:

void foo(const T* const this, int i);
Static member functions don’t have such a hidden argument, so there is no this pointer to be const or not.

60) What is a storage class?

https://www.tutorialspoint.com/cplusplus/cpp_storage_classes.htm !

61) What will be the output of the following program?

```
#include <iostream>

struct A
{
    int data[2];

    A(int x, int y) : data{x, y} {}
    virtual void f() {}
};

int main(int argc, char **argv)
{
    A a(22, 33);

    int *arr = (int *) &a;
    std::cout << arr[2] << std::endl;

    return 0;
}
```

In the main function the instance of struct A is treated as an array of integer values. On 32-bit architectures the output will be 33, and on 64-bit architectures it will be 22. This is because there is virtual method f() in the struct which makes compiler insert a vptr pointer that points to vtable (a table of pointers to virtual functions of class or struct). On 32-bit architectures the vptr takes 4 bytes of the struct instance and the rest is the data array, so arr[2] represents access to second element of the data array, which holds value 33. On 64-bit architectures the vptr takes 8 bytes so arr[2] represents access to the first element of the data array, which holds 22.

This question is testing knowledge of virtual functions internals, and knowledge of C++11-specific syntax as well, because the constructor of A uses the extended initializer list of the C++11 standard.

Compiled with:

g++ question_vptr.cpp -m32 -std=c++11
g++ question_vptr.cpp -std=c++11

62) What is lvalue and rvalue?

lvalue - locator value, it should an adrress, rvalue - is a opposite. So originally lvalue should on the left side of assignment. Currentl it's more complex bacause have cv-specified lvalues (const volatile) and immutalbe lavalues
https://habr.com/ru/post/348198/

63)
(переписываю то, что у меня на шпорах к собеседованиям было, на каждый пункт один-два листа): auto, decltype; forward; explicit; noexcept; mutable; {deque, stack, queque, unordered_map} — выучил зачем-то все методы этих классов отсюда; перегруженные функции/перегрузка операторов; шаблонные классы/функции; всё о «виртуальности» в ООП (функции, классы, чисто виртуальные функции и пр); всё о конструкторах (конструктор копирования, делегирующий коструктор, перемещающий и пр); отключение копирования в классе; move() семантика, ссылки (lvalue, rvalue, xvalue, glvalue, prvalue); std::forward; исключения в деструкторе/конструкторе; где уместен try\catch; сопоставление хэш таблиц и map; static; defaul; override; mutable; reinterpret_cast; constexpr; volatile