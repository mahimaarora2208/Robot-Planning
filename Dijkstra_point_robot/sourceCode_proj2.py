import time
import matplotlib.pyplot as plt
import math
import numpy as np
import cv2

# ********** Start and Goal Coordinates (Parameters that can be changed by User) ***********

s_x = 15  # Start x coord
s_y = 15  # Start y coord
s_idx = (s_x, s_y)
g_x = 140 # Goal x coord
g_y = 140  # Goal y coord
g_idx = (g_x, g_y)

c = 5  # Clearance
c_xy = np.sqrt(c **2 / 2) # Clearance for diagonal lines
# ********** Initializing Variables ***********
pix = []
for pt in range(100000):
    pt = math.inf
    pix.append(pt)
init_mat = np.array(pix, dtype = object).reshape(400, 250)
init_mat[s_idx[0]][s_idx[1]] = 0

num_rows = init_mat.shape[0]
num_cols = init_mat.shape[1]
print('Total number of rows : ', num_cols)
print('Total number of cols : ', num_rows)

inObstacle_flag = False
map_img = np.zeros((num_cols, num_rows, 3), np.uint8)  # Creates a black image of 250 * 400
# start node
map_img[s_idx[1], s_idx[0]] = (0, 255, 0)
# goal node
map_img[g_idx[1], g_idx[0]] = (255, 255, 255) 

# ********** Obstacle Map for the Graph using Half-Plane and Semi-Algebraic Equations ***********
def obstacle_map(): 
    # obstacle equations with clearance
    # circle
    for x in range(0, num_rows):
        for y in range(0, num_cols):
            if ((x - 300) ** 2) / (40+c)**2 + ((y - 185) ** 2) / (40+c)**2 <= 1:
                init_mat[x][y] = inObstacle_flag
                map_img[y, x] = (255, 255, 0)

    # hexagon
    for x in range(0, num_rows):
        for y in range(0, num_cols):
            if x >= 165-c and x <= 235+c and y - 0.577*(x+c_xy) - (25+c_xy) <= 0 and y + 0.577*(x-c_xy) - (255.8+c_xy) <= 0 and y - 0.577*(x-c_xy) - (-55.8-c_xy) >= 0 and y + 0.577*(x+c_xy) - (175-c_xy) >= 0:
                init_mat[x][y] = inObstacle_flag
                map_img[y, x] = (255, 255, 0)

    # polygon1
    for x in range(0, num_rows):
        for y in range(0, num_cols):
            if y - 0.316*(x+c_xy) - (173.6+c_xy) <= 0 and y - 0.857*(x-c_xy) - 111.4 >= 0 and y + (0.114*x) - 189.1 >= 0:
                init_mat[x][y] = inObstacle_flag
                map_img[y, x] = (255, 255, 0)

    # polygon2
    for x in range(0, num_rows):
        for y in range(0, num_cols):
            if  y + 3.2*(x-c_xy) - (436+c_xy) <= 0 and y + 1.23*(x+c_xy) - (229.3 - c_xy) >= 0 and y + (0.114*x) - 189.1 <= 0:
                init_mat[x][y] = inObstacle_flag
                map_img[y, x] = (255, 255, 0)
     
    #lower border
    for x in range (0,num_rows):
        for y in range(0, num_cols):
            if (y <= 0 + c):
                init_mat[x][y] = inObstacle_flag
                map_img[y, x] = (255, 0, 0)

    #upper border
    for x in range (0,num_rows):
        for y in range(0, num_cols):
            if (y >= 250 - c):
                init_mat[x][y] = inObstacle_flag
                map_img[y, x] = (255, 0, 0)

    #left border
    for x in range (0,num_rows):
        for y in range(0, num_cols):
            if (x <= 0 + c):
                init_mat[x][y] = inObstacle_flag
                map_img[y, x] = (255, 0, 0)

    #right border
    for x in range (0,num_rows):
        for y in range(0, num_cols):
            if (x >= 400 - c):
                init_mat[x][y] = inObstacle_flag
                map_img[y, x] = (255, 0, 0)

   
    # obstacle equations without clearance
    # circle
    for x in range(0, num_rows):
        for y in range(0, num_cols):
            if ((x - 300) ** 2) / (40)**2 + ((y - 185) ** 2) / (40)**2 <= 1:
                init_mat[x][y] = inObstacle_flag
                map_img[y, x] = (255, 0, 255)
    # hexagon
    for x in range(0, num_rows):
        for y in range(0, num_cols):
            if x >= 165 and x <= 235 and y - (0.577*x) - 25 <= 0 and y + (0.577*x) - 255.8 <= 0 and y - (0.577*x) + 55.8 >= 0 and y + (0.577*x) - 175 >= 0:
                init_mat[x][y] = inObstacle_flag
                map_img[y, x] = (255, 0, 255)
    # polygon1
    for x in range(0, num_rows):
        for y in range(0, num_cols):
            if y - (0.316*x) - 173.6 <= 0 and y - (0.857*x) - 111.4 >= 0 and y + (0.114*x) - 189.1 >= 0:
                init_mat[x][y] = inObstacle_flag
                map_img[y, x] = (255, 0, 255)

    # polygon2
    for x in range(0, num_rows):
        for y in range(0, num_cols):
            if  y + (3.2*x) - 436 < 0 and y + (1.23*x) - 229.3 >= 0 and y + (0.114*x) - 189.1 <= 0:
                init_mat[x][y] = inObstacle_flag
                map_img[y, x] = (255, 0, 255)

    # #lower border
    # for x in range (0,num_rows):
    #     for y in range(0, num_cols):
    #         if (y <= 0):
    #             init_mat[x][y] = inObstacle_flag
    #             map_img[y, x] = (255, 0, 255)

    # #upper border
    # for x in range (0,num_rows):
    #     for y in range(0, num_cols):
    #         if (y >= 250):
    #             init_mat[x][y] = inObstacle_flag
    #             map_img[y, x] = (255, 0, 255)

    # #left border
    # for x in range (0,num_rows):
    #     for y in range(0, num_cols):
    #         if (x <= 0):
    #             init_mat[x][y] = inObstacle_flag
    #             map_img[y, x] = (255, 0, 255)

    # #right border
    # for x in range (0,num_rows):
    #     for y in range(0, num_cols):
    #         if (x >= 400):
    #             init_mat[x][y] = inObstacle_flag
    #             map_img[y, x] = (255, 0, 255)


   


    # cv2.imshow('Dijkstra Algorithm', np.flipud(map_img))
    # plt.show()
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # # Creates Hexagon
    # points = np.array([[200, 140], [235, 120],[235, 80], [200, 60], [165, 80], [165, 120]])
    # cv2.fillPoly(map_img, pts=[points], color=(0, 0, 255))
    
    # # Creates Polygon
    # points = np.array([[36,185],[115,210],[80, 180],[105,100]])
    # cv2.fillPoly(map_img, pts=[points], color=(0, 0, 255))

    # # Creates Circle
    # cv2.circle(map_img,(300,185), 40,(0, 0, 255),-1)

    # # Add boundaries to the image
    # maze = cv2.copyMakeBorder(map_img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[0, 0, 255])

    # # img takes left upper corner by default so we flip the image to begin origin from left bottom corner
    # cv2.imshow('Dijkstra Algorithm', np.flipud(maze))  
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    

# ********** Actions to move around the Graph ***********
def ActionMoveUp(r, c, mat):
    try:
        if not mat[r - 1, c]:
            return None
    except:
        pass
    if r <= 0:
        return None
    else:
        cost = init_mat[r][c] + 1
        r = r - 1
    return (r, c), cost

def ActionMoveUpRight(r, c, mat):
    try:
        if not mat[r - 1, c + 1]:
            return None
    except:
        pass
    if c >= 400 or r <= 0:
        return None
    else:
        cost = init_mat[r][c] + 1.4
        r = r - 1
        c = c + 1   
    return (r, c), cost

def ActionMoveRight(r, c, mat):
    try:
        if not mat[r, c + 1]:
            return None
    except:
        pass
    if c >= 300:
        return None
    else:
        cost = init_mat[r][c] + 1
        c = c + 1
    return (r, c), cost

def ActionMoveDownRight(r, c, mat):
    try:
        if not mat[r + 1, c + 1]:
            return None
    except:
        pass
    if c >= 400 or r >= 250:
        return None
    else:
        cost = init_mat[r][c] + 1.4
        r = r + 1
        c = c + 1
    return (r, c), cost

def ActionMoveDown(r, c, mat):
    try:
        if not mat[r + 1, c]:
            return None
    except:
        pass
    if r >= 250:
        return None
    else:
        cost = init_mat[r][c] + 1
        r = r + 1
    return (r, c), cost

def ActionMoveDownLeft(r, c, mat):
    try:
        if not mat[r + 1, c - 1]:
            return None
    except:
        pass
    if c <= 0 or r >= 250:
        return None
    else:
        cost = init_mat[r][c] + 1.4
        r = r + 1
        c = c - 1 
    return (r, c), cost

def ActionMoveLeft(r, c, mat):
    try:
        if not mat[r, c - 1]:
            return None
    except:
        pass
    if c <= 0:
        return None
    else:
        cost = init_mat[r][c] + 1
        c = c - 1
    return (r, c), cost

def ActionMoveUpLeft(r, c, mat):
    try:
        if mat[r - 1, c - 1]:
            return None
    except:
        pass
    if r <= 0 or c <= 0:
        return None
    else:
        cost = init_mat[r][c] + 1.4
        r = r - 1
        c = c - 1
    return (r, c), cost

# ********** To get neighboring node info (action in clockwise direction {up, upRight, right...etc}) ***********

def neighbor_info(r, c):
    idx = []  # Stores the coordinate of the point (r,c) in matrix
    cost_neighbor = [] # Stores the cost of the neighbor
  
    action_up = ActionMoveUp(r, c, init_mat)
    if action_up is not None:
        cost_neighbor.append(action_up[1])
        idx.append(action_up[0])
    
    action_upRight = ActionMoveUpRight(r, c, init_mat)
    if action_upRight is not None:
        cost_neighbor.append(action_upRight[1])
        idx.append(action_upRight[0])
    
    action_right = ActionMoveRight(r, c, init_mat)
    if action_right is not None:
        cost_neighbor.append(action_right[1])
        idx.append(action_right[0])    

    action_downRight = ActionMoveDownRight(r, c, init_mat)
    if action_downRight is not None:
        cost_neighbor.append(action_downRight[1])
        idx.append(action_downRight[0]) 

    action_down = ActionMoveDown(r, c, init_mat)
    if action_down is not None:
        cost_neighbor.append(action_down[1])
        idx.append(action_down[0]) 
    
    action_downLeft = ActionMoveDownLeft(r, c,init_mat)
    if action_downLeft is not None:
        cost_neighbor.append(action_downLeft[1])
        idx.append(action_downLeft[0])    

    action_left = ActionMoveLeft(r, c, init_mat)
    if action_left is not None:
        cost_neighbor.append(action_left[1])
        idx.append(action_left[0])  
    
    action_upLeft = ActionMoveUpLeft(r, c,init_mat)
    if action_upLeft is not None:
        cost_neighbor.append(action_upLeft[1])
        idx.append(action_upLeft[0])
           
    return cost_neighbor, idx


# ********** Visualization for Dijkstra ************  
def visualization(visited,img_map, parent_map, node):
    path_list = []
    path_list.append(node)
    parent = parent_map[node]
    
    while parent is not None:
        path_list.append(parent)
        parent = parent_map[parent]

    for ele in visited:
        x = ele[0]
        y = ele[1]
        map_img[y, x] = (0, 204, 153)  # shows visited nodes in green
        # print(map_img[y,x],x,y)
        cv2.imshow('map',np.flipud(map_img))
        if cv2.waitKey(1) == 27:
            break

    for idx in path_list:
        map_img[idx[1], idx[0]] = (102, 0, 102)

    cv2.imshow('Dijkstra Algorithm', np.flipud(map_img))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ********** Main function begins (Code start point) ***********
def main():
    print("Search Algorithm Started : \n")
    obstacle_map() # Shows the obstacle map

    # Checks if Initial and Final Nodes are not in the Obstacle
    
    if not init_mat[s_idx[0]][s_idx[1]]:
        print("Initial node in the obstacle")
    else:
        print("initial node not in obstacle")

    if not init_mat[g_idx[0]][g_idx[1]]:
        print("goal node in the obstacle")
    else:
        print("goal node not in obstacle")

    # algorithm related initalisation
    nodeCost = 0
    idx_q = [] 
    open_q = []
    visited_list = []
    visited = set()
    child_parent_map = {}
    child_parent_map[s_idx] = None
    idx_q.append(s_idx)
    open_q.append(nodeCost)
    stop_flag = False

    while len(idx_q) != 0 and not stop_flag:
        node = idx_q[0]
        visited.add(node)
        visited_list.append(node)

        idx_q.pop(0)
        open_q.pop(0)
        pair = neighbor_info(node[0],node[1])
        cost_neghbr = pair[0]
        index = pair[1]
        # print(index)
        # print(cost_neghbr)
        
        # Checks if goal node is reached
        if node == g_idx:
            print('\n ******** GOAL IS REACHED ******** \n')
            visualization(visited_list,map_img, child_parent_map, node)
            stop_flag = True
        
        for i in range(len(index)):
            if index[i] not in visited:           
                old_cost = init_mat[index[i][0]][index[i][1]]
                if cost_neghbr[i] < old_cost:
                    init_mat[index[i][0]][index[i][1]] = cost_neghbr[i]
                    if old_cost != math.inf:
                        node_idx = idx_q.index((index[i][0], index[i][1]))
                        idx_q.pop(node_idx)
                        open_q.pop(node_idx)
                        
                    idx_q.append(index[i])
                    open_q.append(init_mat[index[i][0]][index[i][1]])
                    child_parent_map[index[i]] = node



if __name__ == '__main__':
    main()

