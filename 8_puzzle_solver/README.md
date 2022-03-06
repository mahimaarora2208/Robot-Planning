Note : Please download the zip and extract it. Use VSC for running the code.
<h4>Project Description

This is an 8 puzzle solver program which uses BFS Planning Algorithm to solve it self. BFS or Breadth First Search algorithm is an algorithm used for searching a tree data structure for a node that satisfies a given condition, in this case the goal node.


<h4> Code Description <h4>
- Queue Class
1. The queue class implements pop() and append() functions of List. 
2. It appends on the end of the list and pops the first element entered making it a First-In First Out behaviour.

- Running Code
1. Open the sourceCode_proj1.py file and enter your initial and final states in variables "input_init" and "input_final".
2. example : If you want to enter the following matrix:

1 5 2
4 0 3
7 8 6

we enter like --> [[1,4,7],[5,0,8],[7,8,6]]
Note : the code takes care of the transpose so enter column wise values

3. Some of the formatting in the files is different from what mentioned in the sample files, so I wanted to mention it here.
-  Nodes.txt : file contains all the nodes in column-wise format but each node element is in same row sepearted by a comma and enclosed in array(). 

e.g. [array([1, 4, 7, 5, 0, 8, 2, 3, 6]), array([1, 4, 7, 0, 5, 8, 2, 3, 6]), array([1, 4, 7, 5, 8, 0, 2, 3, 6]), array([1, 0, 7, 5, 4, 8, 2, 3, 6])


- NodesInfo.txt : File contains the mapping of each child node to parent node in one row. They are all seperated by a comma as well.

e.g. {1: 0, 2: 1, 3: 1, 4: 1, and so on. Here "key is child" and "value is parent".

- NodesPath.txt : file starts from the goal node and backtracks to the start node. However, it stops one node right before the exact start node since we are aware of the initial node. 

e.g.
[1 4 7 2 5 8 3 6 0]
[1 4 7 2 5 8 3 0 6]
[1 4 7 2 5 8 0 3 6]
[1 4 7 0 5 8 2 3 6]

4. Initial_State1 folder shows results for :
Test case 1
Initial state - [1,4,7],[5,0,8],[2,3,6]
5. Initial_state2 folder shows results for :
Test case 2
Initial state -  [4,7,0],[1,2,8],[3,5,6]

Goal states for both the cases are same.
Goal states is [1,4,7 ],[2,5,8],[3,6,0]

