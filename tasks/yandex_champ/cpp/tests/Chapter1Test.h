#include <cxxtest/TestSuite.h>
#include "../chapter1Tasks.hpp"
#include <string>
#include <iostream>

class Chapter1Test : public CxxTest::TestSuite
{
public:
  void testCheckAllSymbolsOnlyOne( void )
  {
      TS_ASSERT(checkAllSymbolsOnlyOne(""));
      TS_ASSERT(checkAllSymbolsOnlyOne("1"));
      TS_ASSERT(!checkAllSymbolsOnlyOne("11"));
      TS_ASSERT(!checkAllSymbolsOnlyOne("abcdegh!!"));
      TS_ASSERT(!checkAllSymbolsOnlyOne("wefiuwefuih wef ewiu hfewf "));
  }

  void testReverse( void )
  {
      std::string str = "";
      TS_ASSERT_EQUALS(reverse(str), "");
      str = "1";
      TS_ASSERT_EQUALS(reverse(str), "1");
      str = "123";
      TS_ASSERT_EQUALS(reverse(str), "321");
      str = "1234";
      TS_ASSERT_EQUALS(reverse(str), "4321");
      str = "11 22 33";
      TS_ASSERT_EQUALS(reverse(str), "33 22 11");
  }

  void testCheckPermutation()
  {
      TS_ASSERT(checkPermutation("", ""));
      TS_ASSERT(checkPermutation("1", "1"));
      TS_ASSERT(checkPermutation("12", "21"));
      TS_ASSERT(checkPermutation("112233", "123123"));
      TS_ASSERT(checkPermutation("test r234", "res tt432"));
      TS_ASSERT(!checkPermutation("123", "1234"));
      TS_ASSERT(!checkPermutation("123", "133"));
      TS_ASSERT(!checkPermutation("321", "333"));
  }

  void testReplaceSpaceToPercent20( void )
  {
      char str[15] = "";
      TS_ASSERT_EQUALS(replaceSpaceToPercent20(str, 0), "");
      strcpy(str, "1");
      TS_ASSERT_EQUALS(replaceSpaceToPercent20(str, 1), "1");
      strcpy(str,"123");
      TS_ASSERT_EQUALS(replaceSpaceToPercent20(str, 3), "123");
      strcpy(str,"1  2");
      TS_ASSERT_EQUALS(replaceSpaceToPercent20(str, 4), "1%20%202");
      strcpy(str," hello w");
      TS_ASSERT_EQUALS(replaceSpaceToPercent20(str, 8), "%20hello%20w");
  }

  void testCompressString( void )
  {
//      TS_ASSERT_EQUALS(compressString(""), "");
//      TS_ASSERT_EQUALS(compressString("a"), "a");
//      TS_ASSERT_EQUALS(compressString("aa"), "aa");
//      TS_ASSERT_EQUALS(compressString("aaq"), "aaq");
//      TS_ASSERT_EQUALS(compressString("abc"), "abc");
        std::cout << "WTF@";
     // TS_ASSERT_EQUALS(compressString("aaabbbc"), "a3b3c1");
//      TS_ASSERT_EQUALS(compressString("111"), "13");
//      TS_ASSERT_EQUALS(compressString("aaaaaaaaaab"), "a10b1");
  }
};
