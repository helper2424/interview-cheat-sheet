builds/chapter2: Chapter2Test.h Chapter2Tasks.hpp Node.h
	mkdir -p builds
	cxxtestgen --error-printer -o builds/Chapter2Test.cpp Chapter2Test.h Node.h
	g++  -ggdb -std=c++11 -o builds/chapter2 builds/Chapter2Test.cpp
	chmod +x builds/chapter2

debug: builds/chapter2
	gdb ./builds/chapter2

debug_remove_duplicates_without_buffer: builds/chapter2
	gdb --args ./builds/chapter2 Chapter2Test test_remove_duplicates_without_buffer

debug_is_palindrom: builds/chapter2
	gdb --args ./builds/chapter2 Chapter2Test test_is_palindrom

debug_find_loop: builds/chapter2
	gdb --args ./builds/chapter2 Chapter2Test test_find_loop

test: ./builds/chapter2
	./builds/chapter2

clean:
	rm -rf builds