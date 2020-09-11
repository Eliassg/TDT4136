import Map


def best_first_search(start):
    closed = []
    open = []
    #Generate initial node
    start_node = search_Node(None, start)
    

class search_Node:
    def __init__(self, position = None, best_Parent = None):
        
        self.g = 0 #cost of getting to this node
        self.h = 0 #estimated cost to goal
        self.f = self.g + self.h #estimated total cost of a solution path going through this node
        self.position = position
        self.best_Parent = best_Parent
        self.kids = []


