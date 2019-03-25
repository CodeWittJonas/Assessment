cmake_minimum_required(VERSION 3.13)
project(InformatikII C)

set(CMAKE_C_STANDARD 99)

add_executable(Week1 Week1/main.c)
add_executable(InformatikII Week1/hello.c)
add_executable(DrawTriangle Week2/task2.c)
add_executable(BoxFractal Week2/task3b__skeleton.c)
add_executable(gcdlcm Week2/task1.c)
add_executable(whatdoesitdo Week3/task1.c)
add_executable(hanoi Week4/task4.c)
add_executable(heapsort Week5/task1.c)