# dijkstra-2d-array
### Implementation of a modified version of Dijkstra's Algorithm for Algorithms assignment, in which instead of finding the shortest path, the longest path is found.

All code is written from scratch with only the basics of dijkstra's algorithm being described in class. This is because the assignment was submitted and checked via a plagiarism detector.

### Objective:

Given a 2D integer array of *m* rows and *n* columns,

Traverse the array clockwise exactly *n - 1* times (no backwards moving), ensuring that the starting and ending point of the traversal is either the top *or* the bottom row of the 2D Array.

Movement upwards when at the first row will put the next point in the traversal back to the bottom (and vice versa).

Return the path of the traversal that has the highest cumulative sum.

### Example:

given:

1 1 4 8 8 6 2 2 8 2 1 5  
2 8 1 8 2 2 2 4 5 9 9 1  
8 3 2 5 2 2 5 8 9 8 4 4  
1 4 1 9 8 9 5 6 1 6 4 7  
7 2 6 8 4 1 1 7 1 2 5 3  
6 2 2 6 1 6 2 2 7 8 7 7  
8 5 5 8 9 8 7 8 8 3 2 5

the optimal path would be starting at a specific **8** on the top row, and gives us a max sum of **89** for the entire 2D array:

72 80 88 **8** 16 23 27 34 **48** 50 58 **71**  
73 81 81 x 10 18 25 31 39 **57** **66** 67  
78 76 83 x xx 12 23 33 40 47 61 70  
71 82 77 xx x xx 17 30 35 41 53 68  
75 73 87 x xx xx 24 34 35 49 61 61  
69 81 86 x xx 23 27 34 47 56 58 65  
**79** **84** **89** x **17** **25** **32** **40** 48 51 53 63 
