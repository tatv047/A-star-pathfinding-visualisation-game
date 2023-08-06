# A-star-pathfinding-visualisation-game
This is an implementation of the A* pathfinding algorithm using the Pygame library in Python. 
The A* algorithm is used to find the shortest path between a start and end point on a grid.

# Let's break down the code step-by-step:

1. First, the necessary libraries are imported: `pygame`, `math`, and `PriorityQueue` from the `queue` module.

2. The width of the game window (`WIDTH`) and the Pygame window (`WIN`) are defined.

3. Various color constants are defined for drawing the grid and nodes.

4. The `Node` class is defined. Each instance of this class represents a cell in the grid. The class has various methods and attributes such as `get_pos()`, `is_closed()`, `is_open()`, `is_barrier()`, `is_start()`, etc., which are used to define the properties of a node and perform various operations on them.

5. The `heuristic` function is defined. This function calculates the heuristic value between two points using the Manhattan distance formula.

6. The `reconstruct_path` function is defined. This function is used to trace back the shortest path from the end node to the start node using the `came_from` dictionary.

7. The `algorithm` function is defined. This function implements the A* algorithm. It takes the `draw` function, `grid` (2D list of `Node` objects), `start` node, and `end` node as inputs. It calculates the shortest path using the A* algorithm and calls the `draw` function to update the visualization at each step.

8. The `make_grid` function is defined. This function creates a 2D list of `Node` objects based on the number of rows and the width of the grid.

9. The `draw_grid` function is defined. This function is used to draw the grid lines on the game window.

10. The `draw` function is defined. This function is used to draw the updated grid and grid lines on the game window.

11. The `get_clicked_pos` function is defined. This function takes the mouse position (`pos`), number of rows, and grid width as inputs and returns the row and column corresponding to the clicked position.

12. The `main` function is defined. This function is the entry point of the program. It initializes the grid, start, and end nodes. It handles user events such as mouse clicks and keyboard input. It also calls the `algorithm` function when the spacebar is pressed to find the shortest path.

13. Finally, the `main` function is called with the game window and width as input arguments to start the program.

You can create barriers, set the start and end points, and visualize the A* algorithm finding the shortest path on the grid using the Pygame library. 
