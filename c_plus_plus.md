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

26) 