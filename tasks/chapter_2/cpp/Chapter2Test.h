#include <cxxtest/TestSuite.h>
#include "Node.h"
#include "Chapter2Tasks.hpp"
#include <initializer_list>

#include <iostream>
#include <vector>

class Chapter2Test : public CxxTest::TestSuite
{
public:
    void test_remove_duplicates( void )
    {
        auto list = new Node<int>({1});
        TS_ASSERT_EQUALS(list->removeDuplicates()->toVector(), std::vector<int>({1}));
        delete list;

        list = new Node<int>({1, 2});
        TS_ASSERT_EQUALS(list->removeDuplicates()->toVector(), std::vector<int>({1, 2}));
        delete list;

        list = new Node<int>({1, 1});
        TS_ASSERT_EQUALS(list->removeDuplicates()->toVector(), std::vector<int>({1}));
        delete list;
        
        list = new Node<int>({1, 1, 1, 1});
        TS_ASSERT_EQUALS(list->removeDuplicates()->toVector(), std::vector<int>({1}));
        delete list;

        list = new Node<int>({1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8});
        TS_ASSERT_EQUALS(list->removeDuplicates()->toVector(), std::vector<int>({1, 2, 3, 4, 5, 6, 7, 8}));
        delete list;
    }

    void test_remove_duplicates_without_buffer( void )
    {
        auto list = new Node<int>({1});
        TS_ASSERT_EQUALS(list->removeDuplicatesWithoutBuffer()->toVector(), std::vector<int>({1}));
        delete list;

        list = new Node<int>({1, 2});
        TS_ASSERT_EQUALS(list->removeDuplicatesWithoutBuffer()->toVector(), std::vector<int>({1, 2}));
        delete list;

        list = new Node<int>({1, 1});
        TS_ASSERT_EQUALS(list->removeDuplicatesWithoutBuffer()->toVector(), std::vector<int>({1}));
        delete list;


        list = new Node<int>({1, 1, 1, 1});
        TS_ASSERT_EQUALS(list->removeDuplicatesWithoutBuffer()->toVector(), std::vector<int>({1}));
        delete list;

        list = new Node<int>({1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8});
        TS_ASSERT_EQUALS(list->removeDuplicatesWithoutBuffer()->toVector(), std::vector<int>({1, 2, 3, 4, 5, 6, 7, 8}));
        delete list;
    }

    void test_self_delete(void) {
        auto list = new Node<int>({1, 2});
        list->find(1)->selfDelete();

        TS_ASSERT_EQUALS(list->toVector(), std::vector<int>({2}));
        delete list;

        list = new Node<int>({1, 2, 3, 4, 5, 6, 7});
        list->find(4)->selfDelete();

        TS_ASSERT_EQUALS(list->toVector(), std::vector<int>({1, 2, 3, 5, 6, 7}));
        delete list;
    }

    void test_sort_around_x(void) {
        auto list = new Node<int>({1, 2});
        auto new_list = list->sort_around(1);

        TS_ASSERT_EQUALS(new_list->toVector(), std::vector<int>({1, 2}));
        delete list;
        delete new_list;

        list = new Node<int>({1});
        new_list = list->sort_around(1);

        TS_ASSERT_EQUALS(new_list->toVector(), std::vector<int>({1}));
        delete list;
        delete new_list;

        list = new Node<int>({1, 2, 3, 4,5, 6, 7, 8});
        new_list = list->sort_around(1);

        TS_ASSERT_EQUALS(new_list->toVector(), std::vector<int>({1, 2, 3, 4,5, 6, 7, 8}));
        delete list;
        delete new_list;

        list = new Node<int>({4, 5, 90, 190, 1, 900, 200});
        new_list = list->sort_around(10);

        TS_ASSERT_EQUALS(new_list->toVector(), std::vector<int>({4, 5, 1, 90, 190, 900, 200}));
        delete list;
        delete new_list;

        list = new Node<int>({4, 5, 90, 190, 1, 900, 200});
        new_list = list->sort_around(1000);

        TS_ASSERT_EQUALS(new_list->toVector(), std::vector<int>({4, 5, 90, 190, 1, 900, 200}));
        delete list;
        delete new_list;
    }

    void test_find_loop(void) {
        auto list = new Node<int>({1, 2});
        list->find(2)->setNext(list->find(1));

        TS_ASSERT_EQUALS(list->find_loop()->getValue(), 1);
        list->find(2)->setNext(nullptr);
        delete list;

        list = new Node<int>({1});
        list->find(1)->setNext(list->find(1));

        TS_ASSERT_EQUALS(list->find_loop()->getValue(), 1);
        list->find(1)->setNext(nullptr);
        delete list;

        list = new Node<int>({1, 2, 3, 4, 5, 6, 7, 8, 9});
        list->find(9)->setNext(list->find(5));

        TS_ASSERT_EQUALS(list->find_loop()->getValue(), 5);
        list->find(9)->setNext(nullptr);
        delete list;

        list = new Node<int>({1, 2, 3, 4, 5, 6, 7, 8, 9});
        list->find(9)->setNext(list->find(9));

        TS_ASSERT_EQUALS(list->find_loop()->getValue(), 9);
        list->find(9)->setNext(nullptr);
        delete list;
//
        list = new Node<int>({1, 2, 3, 4, 5, 6, 7, 8, 9});
        list->find(9)->setNext(list->find(1));

        TS_ASSERT_EQUALS(list->find_loop()->getValue(), 1);
        list->find(9)->setNext(nullptr);
        delete list;

        list = new Node<int>({1, 2, 3, 4, 5, 6, 7, 8, 9});
        TS_ASSERT_EQUALS(list->find_loop(), nullptr);
        delete list;
    }

    void test_is_palindrom(void) {
        auto list = new Node<int>({1, 2});
        TS_ASSERT(!list->is_palindrom());
        delete list;

        list = new Node<int>({1});
        TS_ASSERT(list->is_palindrom());
        delete list;

        list = new Node<int>({1, 3, 1});
        TS_ASSERT(list->is_palindrom());
        delete list;

        list = new Node<int>({1, 3, 2});
        TS_ASSERT(!list->is_palindrom());
        delete list;

        list = new Node<int>({1, 2, 2, 1});
        TS_ASSERT(list->is_palindrom());
        delete list;

        list = new Node<int>({1, 2, 3, 4, 5, 4, 3, 2, 1});
        TS_ASSERT(list->is_palindrom());
        delete list;

        list = new Node<int>({1, 2, 3, 4, 5, 5, 4, 3, 2, 1});
        TS_ASSERT(list->is_palindrom());
        delete list;

        list = new Node<int>({1, 2, 3, 4, 5, 5, 4, 3, 10, 1});
        TS_ASSERT(!list->is_palindrom());
        delete list;

        list = new Node<int>({1, 1, 1, 1, 1});
        TS_ASSERT(list->is_palindrom());
        delete list;

        list = new Node<int>({1, 1, 1, 2, 1});
        TS_ASSERT(!list->is_palindrom());
        delete list;
    }
};
