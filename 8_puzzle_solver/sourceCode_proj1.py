from inspect import stack
from pprint import pprint
import numpy as np

# *************************** INPUT INITIAL AND FINAL STATES HERE ***********************************
'''
e.g.
Test case 1
Initial state - [1,4,7],[5,0,8],[2,3,6]
Test case 2
Initial state -  [4,7,0],[1,2,8],[3,5,6]
'''
# input_init = [[1,4,7],[5,0,8],[2,3,6]]
input_init = [[4,7,0],[1,2,8],[3,5,6]]
input_final = [[1,4,7],[2,5,8],[3,6,0]]

# ***************************************************************************************************
'''
Queue = [A,B,C,D,E] appends at the end
pops the 0th index 
'''
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item): 
        self.items.append(item)
    
    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None    

    def size(self):
        return len(self.items) 

# transpose the input
initial_state = np.transpose(input_init)
final_state = np.transpose(input_final)
print("Initial State: ")
print(initial_state,'\n')
print("Goal State: ")
print(final_state,'\n')

# function to return index of the blank tile
def blank_tile_idx(state_mat):
    row, col = np.where(state_mat == 0)
    row = int(row)
    col = int(col)
    return row,col

# functions for moving the blank tile (Actions : Left, Right, Up, Down)
def ActionMoveLeft(state_mat):
    row, col = blank_tile_idx(state_mat)
    # left most column
    if col == 0: 
        return None
    else:
        tempMtx = np.copy(state_mat)
        temp = tempMtx[row, col-1]
        tempMtx[row,col] = temp
        tempMtx[row,col-1] = 0
        
        return tempMtx
                
def ActionMoveRight(state_mat):
    row, col = blank_tile_idx(state_mat)
    if col == 2:
        return None
    else:
        tempMtx = np.copy(state_mat)
        temp = tempMtx[row,col+1]
        tempMtx[row,col] = temp
        tempMtx[row,col+1] = 0
        
        return tempMtx
    
def ActionMoveUp(state_mat):
    row, col = blank_tile_idx(state_mat)
    if row == 0:        
        return None
    else:
        tempMtx = np.copy(state_mat)
        temp = tempMtx[row-1,col]
        tempMtx[row,col] = temp
        tempMtx[row-1, col] = 0
        
        return tempMtx
    
def ActionMoveDown(state_mat):
    row, col = blank_tile_idx(state_mat)
    if row == 2:
        return None
    else:
        tempMtx = np.copy(state_mat)
        temp = tempMtx[row + 1,col]
        tempMtx[row,col] = temp
        tempMtx[row + 1,col] = 0
        
        return tempMtx
        
# Check if the matrix equal
def is_equal(mat1,mat2):
    for i in range(3):
        for j in range(3):
            if mat1[i][j] != mat2[i][j]:
                return False
    return True

# function to get child list   
def find_child(node):

    list_childNodes = []
    # append to the list of childnodes only if it is not None
    action_up = ActionMoveUp(node)
    if action_up is not None:      # will return none only if method does not return anything
        list_childNodes.append(action_up)        
    
    action_down = ActionMoveDown(node)
    if action_down is not None:
        list_childNodes.append(action_down)
    
    action_left = ActionMoveLeft(node)
    if action_left is not None:
        list_childNodes.append(action_left)        
   
    action_right = ActionMoveRight(node) 
    if action_right is not None:
        list_childNodes.append(action_right)
    
    return list_childNodes
    
def main():
     # initializing variables and queue obj
    counter = 0
    goalNodeFound = False
    q = Queue()
    idx_q = Queue()
    visited = []
    parent = []
    child_parent_map = {1 : 0} 
    idx_state_map = { 1 : initial_state}
    idx_q.enqueue(1) # index queue for nodes
    q.enqueue(initial_state)
    
    print("Solution : ", "\n")
    if is_equal(initial_state,final_state):
        print("Initial State is already equal to Final State.....! Goal Reached :)")
    else:    
        while (q.size() != 0) and not goalNodeFound:
            counter += 1
            node = q.dequeue()
            
            print(node,'\n')

            node_index = idx_q.dequeue()
            visited.append(node)
            list_child = find_child(node)
            child_idx_top = np.max(list(child_parent_map.keys()))
            
            # Add relation between parent and child idx
            for i, state in enumerate(list_child):
                new_latest = child_idx_top + i + 1
                child_parent_map[new_latest] = node_index
                
                idx_state_map[new_latest] = state

            child_counter = 0
            for child in list_child:        
                child_counter += 1
                if is_equal(child, final_state) == True:
                    goalNodeFound = True
                    sol_idx = child_idx_top + child_counter
                    print('Puzzle is Solved.....!')
                    break
                else:
                    not_found = True
                    for visited_mat in visited:
                        if is_equal(visited_mat,child):
                            not_found = False
                        
                if not_found: 
                    idx_q.enqueue(child_idx_top + child_counter)
                    q.enqueue(child)

        # cc = visited[0].flatten('F')
        # print(cc)

    # using 'w' as a parameter in open() as we want to overwrite after every run
    with open("Nodes.txt","w") as f:
            flat_list = [item.flatten('F') for item in visited]
            f.write(str(flat_list))
 

    print("\n","States Explored : ", counter)    

    # backtracking index
    path_child = []
    path_parent = []
    parent = child_parent_map[sol_idx]
    child_index = sol_idx
    while parent != 0:
        
        path_child.append(child_index)
        path_parent.append(parent)
        child_index = parent
        parent = child_parent_map[child_index]
        
    print("child path:",path_child)
    print("parent path:",path_parent)

    with open("NodesPath.txt","w") as f1:
        for idx in path_child:
            temp = idx_state_map.get(idx)
            flat_mat = temp.flatten('F')
            f1.write(str(flat_mat) + '\n')
            

    with open("nodesInfo.txt", "w") as f:
        f.write(str(child_parent_map))
        
if __name__ == '__main__':
    main()     
          


    
    

    
    
       
          

 




