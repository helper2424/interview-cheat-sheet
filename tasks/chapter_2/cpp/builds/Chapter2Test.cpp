/* Generated file, do not edit */

#ifndef CXXTEST_RUNNING
#define CXXTEST_RUNNING
#endif

#define _CXXTEST_HAVE_STD
#include <cxxtest/TestListener.h>
#include <cxxtest/TestTracker.h>
#include <cxxtest/TestRunner.h>
#include <cxxtest/RealDescriptions.h>
#include <cxxtest/TestMain.h>
#include <cxxtest/ErrorPrinter.h>

int main( int argc, char *argv[] ) {
 int status;
    CxxTest::ErrorPrinter tmp;
    CxxTest::RealWorldDescription::_worldName = "cxxtest";
    status = CxxTest::Main< CxxTest::ErrorPrinter >( tmp, argc, argv );
    return status;
}
bool suite_Chapter2Test_init = false;
#include "/Users/helper2424/Documents/interview-cheat-sheet/tasks/chapter_2/cpp/Chapter2Test.h"

static Chapter2Test suite_Chapter2Test;

static CxxTest::List Tests_Chapter2Test = { 0, 0 };
CxxTest::StaticSuiteDescription suiteDescription_Chapter2Test( "Chapter2Test.h", 9, "Chapter2Test", suite_Chapter2Test, Tests_Chapter2Test );

static class TestDescription_suite_Chapter2Test_test_remove_duplicates : public CxxTest::RealTestDescription {
public:
 TestDescription_suite_Chapter2Test_test_remove_duplicates() : CxxTest::RealTestDescription( Tests_Chapter2Test, suiteDescription_Chapter2Test, 12, "test_remove_duplicates" ) {}
 void runTest() { suite_Chapter2Test.test_remove_duplicates(); }
} testDescription_suite_Chapter2Test_test_remove_duplicates;

static class TestDescription_suite_Chapter2Test_test_remove_duplicates_without_buffer : public CxxTest::RealTestDescription {
public:
 TestDescription_suite_Chapter2Test_test_remove_duplicates_without_buffer() : CxxTest::RealTestDescription( Tests_Chapter2Test, suiteDescription_Chapter2Test, 35, "test_remove_duplicates_without_buffer" ) {}
 void runTest() { suite_Chapter2Test.test_remove_duplicates_without_buffer(); }
} testDescription_suite_Chapter2Test_test_remove_duplicates_without_buffer;

static class TestDescription_suite_Chapter2Test_test_self_delete : public CxxTest::RealTestDescription {
public:
 TestDescription_suite_Chapter2Test_test_self_delete() : CxxTest::RealTestDescription( Tests_Chapter2Test, suiteDescription_Chapter2Test, 59, "test_self_delete" ) {}
 void runTest() { suite_Chapter2Test.test_self_delete(); }
} testDescription_suite_Chapter2Test_test_self_delete;

static class TestDescription_suite_Chapter2Test_test_sort_around_x : public CxxTest::RealTestDescription {
public:
 TestDescription_suite_Chapter2Test_test_sort_around_x() : CxxTest::RealTestDescription( Tests_Chapter2Test, suiteDescription_Chapter2Test, 73, "test_sort_around_x" ) {}
 void runTest() { suite_Chapter2Test.test_sort_around_x(); }
} testDescription_suite_Chapter2Test_test_sort_around_x;

static class TestDescription_suite_Chapter2Test_test_find_loop : public CxxTest::RealTestDescription {
public:
 TestDescription_suite_Chapter2Test_test_find_loop() : CxxTest::RealTestDescription( Tests_Chapter2Test, suiteDescription_Chapter2Test, 110, "test_find_loop" ) {}
 void runTest() { suite_Chapter2Test.test_find_loop(); }
} testDescription_suite_Chapter2Test_test_find_loop;

static class TestDescription_suite_Chapter2Test_test_is_palindrom : public CxxTest::RealTestDescription {
public:
 TestDescription_suite_Chapter2Test_test_is_palindrom() : CxxTest::RealTestDescription( Tests_Chapter2Test, suiteDescription_Chapter2Test, 151, "test_is_palindrom" ) {}
 void runTest() { suite_Chapter2Test.test_is_palindrom(); }
} testDescription_suite_Chapter2Test_test_is_palindrom;

#include <cxxtest/Root.cpp>
const char* CxxTest::RealWorldDescription::_worldName = "cxxtest";
