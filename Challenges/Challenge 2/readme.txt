Bunny Prisoner Locating
=======================

Keeping track of Commander Lambda's many bunny prisoners is starting to get tricky. You've been tasked with writing a program to match bunny prisoner IDs to cell locations.

The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the prison blocks have an unusual layout. They are stacked in a triangular shape, and the bunny prisoners are given numerical IDs starting from the corner, as follows:

8|29
7|22 30
6|16 23 31
5|11 17 24 32
4| 7 12 18 25 33
3| 4  8 13 19 26 34
2| 2  5  9 14 20 27 35
1| 1  3  6 10 15 21 28 36

 1 = 1 1
 2 = 1 2
 3 = 2 1
 4 = 1 3
 5 = 2 2
 6 = 3 1
 7 = 1 4
 8 = 2 3
 9 = 3 2
10 = 4 1
11 = 1 5
12 = 2 4
13 = 3 3
14 = 4 2
15 = 5 1
16 = 1 6
17 = 2 5
18 = 3 4
19 = 4 3
20 = 5 2
21 = 6 1

96 = 5 10


Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground. 

For example, the bunny prisoner at (1, 1) has ID 1, the bunny prisoner at (3, 2) has ID 9, and the bunny prisoner at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been taking a LOT of prisoners). 

Write a function answer(x, y) which returns the prisoner ID of the bunny at location (x, y). Each value of x and y will be at least 1 and no greater than 100,000. Since the prisoner ID can be very large, return your answer as a string representation of the number.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) x = 3
    (int) y = 2
Output:
    (string) "9"

Inputs:
    (int) x = 5
    (int) y = 10
Output:
    (string) "96"

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.