from maze_creator import *
from solver import *
from sys import *
setrecursionlimit(100000000)

class mazeProblem(Problem):
    def __init__(self, node):
        self.start = node
        self.explored = {}
    
    def start_node(self):
        return self.start
    
    def is_goal(self, node):
        return node.is_goal
    
    def heuristic(self, node):
        heuristic = -1 * sum(node.pos)
        return heuristic
    
    def neighbours(self, node):
        neighbours = []
        for neighbour in node.connections:
            if neighbour in self.explored:
                continue
            else:
                neighbours.append(Arc(node, neighbour))
                self.explored[neighbour] = True
        return neighbours


def create_maze():
    grid = create_grid(24, 90)
    iterative_deepening_controller(grid)
    #dfs_create_maze(grid)
    print(grid.show_maze())
    return grid
    

def solve_maze(grid):
    problem = mazeProblem(grid)
    solver = AStarSolver(problem)
    solution = solver.solve()
    while type(solution.prior) == Path:
        solution.end().important = True
        solution = solution.prior
    print(grid.show_maze())
    print(problem.explored)
    

    
    
if __name__ == "__main__":
    grid = create_maze()
    solve_maze(grid)
    
