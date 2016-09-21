cmake_minimum_required (VERSION 2.8)
project (MyHello)

include (${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup ()

add_executable (mytest test.cpp)
add_executable (mtest mtest.c)
target_link_libraries (mytest ${CONAN_LIBS})
target_link_libraries (mtest ${CONAN_LIBS})
