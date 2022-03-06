Note : Please download the zip and extract it OR copy github url and run < git clone https://github.com/mahimaarora2208/Robot-Planning.git > in the terminal.

Use VSC for running the code.

<h3>Project Description</h3>

* This project is the implementation of Dijkstra algorithm for a point robot. It consists of an obstacle maze on which a point robot navigates to reach 
  the Goal position.
* Dijkstra's Algorithm is an algorithm used to find shortest path between two nodes in a graph. It is a cost-based search method which follows optimised 
  cost to locate the goal position.
* The maze is designed in openCV with origin starting at left-bottom corner.
* Maze consists of three obstacles each with a 5mm clearance. 

<h3> Code Description</h3>

* Running Code
1. Open the sourceCode_proj2.py file and enter your initial coordinates(x and y) in "s_x" and "s_y"  and goal coordinate in variable "g_x" and "g_y".
2. example :  

Start position: (10,15)
Goal position: (140,150)

s_x = 10
s_y = 15

g_x = 140
g_y = 150

* Once you run the code, two windows should pop up. "Map" shows the animation for finding the goal node and the "Dijkstra Algorithm" shows the backtrack path from start to goal node. 


* Test Cases
The following test cases were tested and stored in the folder "testCases"

Start           Goal             TimeTaken
------------------------------------------------
(15,15)        (140,150)    


