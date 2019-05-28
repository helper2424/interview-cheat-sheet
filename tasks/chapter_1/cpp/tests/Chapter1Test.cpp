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
bool suite_Chapter1Test_init = false;
#include "/Users/helper2424/Documents/interview-cheat-sheet/tasks/chapter_1/cpp/tests/Chapter1Test.h"

static Chapter1Test suite_Chapter1Test;

static CxxTest::List Tests_Chapter1Test = { 0, 0 };
CxxTest::StaticSuiteDescription suiteDescription_Chapter1Test( "tests/Chapter1Test.h", 5, "Chapter1Test", suite_Chapter1Test, Tests_Chapter1Test );

static class TestDescription_suite_Chapter1Test_testCheckAllSymbolsOnlyOne : public CxxTest::RealTestDescription {
public:
 TestDescription_suite_Chapter1Test_testCheckAllSymbolsOnlyOne() : CxxTest::RealTestDescription( Tests_Chapter1Test, suiteDescription_Chapter1Test, 8, "testCheckAllSymbolsOnlyOne" ) {}
 void runTest() { suite_Chapter1Test.testCheckAllSymbolsOnlyOne(); }
} testDescription_suite_Chapter1Test_testCheckAllSymbolsOnlyOne;

static class TestDescription_suite_Chapter1Test_testReverse : public CxxTest::RealTestDescription {
public:
 TestDescription_suite_Chapter1Test_testReverse() : CxxTest::RealTestDescription( Tests_Chapter1Test, suiteDescription_Chapter1Test, 17, "testReverse" ) {}
 void runTest() { suite_Chapter1Test.testReverse(); }
} testDescription_suite_Chapter1Test_testReverse;

static class TestDescription_suite_Chapter1Test_testCheckPermutation : public CxxTest::RealTestDescription {
public:
 TestDescription_suite_Chapter1Test_testCheckPermutation() : CxxTest::RealTestDescription( Tests_Chapter1Test, suiteDescription_Chapter1Test, 31, "testCheckPermutation" ) {}
 void runTest() { suite_Chapter1Test.testCheckPermutation(); }
} testDescription_suite_Chapter1Test_testCheckPermutation;

static class TestDescription_suite_Chapter1Test_testReplaceSpaceToPercent20 : public CxxTest::RealTestDescription {
public:
 TestDescription_suite_Chapter1Test_testReplaceSpaceToPercent20() : CxxTest::RealTestDescription( Tests_Chapter1Test, suiteDescription_Chapter1Test, 43, "testReplaceSpaceToPercent20" ) {}
 void runTest() { suite_Chapter1Test.testReplaceSpaceToPercent20(); }
} testDescription_suite_Chapter1Test_testReplaceSpaceToPercent20;

static class TestDescription_suite_Chapter1Test_testCompressString : public CxxTest::RealTestDescription {
public:
 TestDescription_suite_Chapter1Test_testCompressString() : CxxTest::RealTestDescription( Tests_Chapter1Test, suiteDescription_Chapter1Test, 59, "testCompressString" ) {}
 void runTest() { suite_Chapter1Test.testCompressString(); }
} testDescription_suite_Chapter1Test_testCompressString;

#include <cxxtest/Root.cpp>
const char* CxxTest::RealWorldDescription::_worldName = "cxxtest";
