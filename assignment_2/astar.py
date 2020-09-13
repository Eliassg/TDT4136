import Map

class search_Node:
    def __init__(self, position = None, best_Parent = None):
        
        self.g = 0 #cost of getting to this node
        self.h = 0 #estimated cost to goal
        self.f = self.g + self.h #estimated total cost of a solution path going through this node
        self.position = position
        self.best_Parent = best_Parent
        self.kids = []
    
    def __eq__(self, other):
        return self.position == other.position

def manhattan_distance(map_obj, position):
    """ Makes an admissible estimate cost goal """

    goal = map_obj.get_goal_pos()
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

def cost_function(map_obj,next_pos):
    return map_obj.get_cell_value(next_pos)



def attach_and_eval(map_obj,child, parent, cost):
    """Attaches a child node to a node that is now considered its best parent"""
    
    child.parent = parent
    child.g = parent.g + cost
    child.h = manhattan_distance(map_obj, child.position)

def propagate_path_improvements(map_obj, parent):
    """ Propagation of path improvements through childrend and possible
        many more descendants """

    for kid in parent.kid:
        if parent.g + 1 < kid.g:
            kid.best_parent = parent
            kid.g = parent.g + cost_function(map_obj, parent)
            kid.f = kid.g + kid.h
            propagate_path_improvements(map_obj, kid)


def best_first_search(map_obj, heuristic_func, cost_func, ):
    closed = []
    open_ = []
    #Generate initial node
    start_node = search_Node(map_obj.get_start_pos())
    goal_node = search_Node(map_obj.get_goal_pos())

    start_node.g = 0
    start_node.h = heuristic_func(map_obj, start_node.position)
    start_node.h = start_node.g + start_node.h
    open_.append(start_node)

    #Agenda loop
    while open_:
        X = open_.pop(0)
        closed.append(X)
        if X == goal_node: #returns path when goal node is found
            path = []
            current_node = X
            while current_node != None:
                path.append(current_node.position)
                X = current_node.best_Parent
            return path.reverse()

        kids = []
        directions = {
            "N": (0,1),
            "S": (0,-1),
            "W": (-1,0),
            "E": (1,0)
            }

        for direction in directions: #generating the nodes kids
            kid_pos = (X[0] + direction[0], X[1] + direction[1])
        
        if cost_function(map_obj, kid_pos) == -1:
        #if map_obj.int_map[kid_pos[0]][kid_pos[1]] == -1:
            continue
        
        new_sn = search_Node(kid_pos, X)
        kids.append(new_sn)

        for kid in kids:
            for node in open_:
                if node == kid:
                    kid = node
            for node in closed:
                if node == kid:
                    kid == node
        
            X.kids.append(kid)


        

def main():
    map_obj = Map.Map_Obj(task = 4)
    start_position = map_obj.get_start_pos()
    int_map, str_map = map_obj.get_maps()
    print(cost_function(map_obj, start_position))
    goal_node = search_Node(map_obj.get_goal_pos())
    x,y = goal_node.position
   
   
    map_obj.show_map()

    print(manhattan_distance(map_obj, start_position))
    print(map_obj.int_map[start_position[0]][start_position[1]])



if __name__ == "__main__":
    main()














