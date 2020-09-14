import Map
import astar as a

def main():
    """ Displays maps and solutions for task 5 """
    task = 5

    map_obj = Map.Map_Obj(task = task)
    start_position = map_obj.get_start_pos()
    goal_position = map_obj.get_goal_pos()
    int_map, str_map = map_obj.get_maps()

    map_obj.show_map() # Show map with start and goal

    path = a.best_first_search(map_obj, a.moving_manhattan, a.cost_function, True)

    print("Starting position: ", start_position)
    print("Goal position: ", goal_position)

    try:
        a.draw_path(map_obj, path)
        print("Drawing path...")
    except TypeError:
        print("Path does not exist :( ")

    map_obj.show_map() # Show map with path 

if __name__ == "__main__":
    main()
