import random
from tkinter import *

class Cell:
    def __init__(self, pos):
        self.pos = pos
        self.left = None
        self.right = None
        self.below = None
        self.above = None
        self.visited = False
        self.connections = []
        self.unvisited = []
        self.important = False
        self.is_goal = False
        

    def show(self):
        output = ""
        curr_below = self
        while curr_below != None:
            curr_right = curr_below
            while curr_right != None:
                output += str(curr_right.pos)
                curr_right = curr_right.right
            output += "\n"
            curr_below = curr_below.below
        return output
    
    def show_maze_with_pos(self):
        output = "-"
        curr_below = self
        curr_right = curr_below
        while curr_right != None:
            output += "---------"
            curr_right = curr_right.right
        output += "\n"
            
        while curr_below != None:
            curr_right = curr_below
            output += "|"
            while curr_right != None:
                output += str(curr_right.pos)
                if curr_right.right in curr_right.connections:
                    
                    output += "   "  # display a connection between cells
                else:
                    output += " | "  # display a wall between cells
                curr_right = curr_right.right
            output += "\n"
            curr_right = curr_below
            while curr_right != None:
                #output += str(curr_right.pos)
                if curr_right.below in curr_right.connections:
                    output += "         "  # display a connection between cells
                else:
                    output += "---------"  # display a wall between cells
                curr_right = curr_right.right
            output += "\n"
            curr_below = curr_below.below
        return output
    
    
    def show_maze(self):
        output = "X"
        curr_below = self
        curr_right = curr_below
        while curr_right != None:
            output += "---X"
            curr_right = curr_right.right
        output += "\n"
            
        while curr_below != None:
            curr_right = curr_below
            output += "|"
            while curr_right != None:
                if curr_right.is_goal:
                    if curr_right.right in curr_right.connections:
                        output += " G  "  # display a connection between cells
                    else:
                        output += " G |"  # display a wall between cells
                    curr_right = curr_right.right
                elif curr_right.important:
                    if curr_right.right in curr_right.connections:
                        output += " I  "  # display a connection between cells
                    else:
                        output += " I |"  # display a wall between cells
                    curr_right = curr_right.right
                else:
                    if curr_right.right in curr_right.connections:
                        output += "    "  # display a connection between cells
                    else:
                        output += "   |"  # display a wall between cells
                    curr_right = curr_right.right
            output += "\nX"
            curr_right = curr_below
            while curr_right != None:
                #output += str(curr_right.pos)
                if curr_right.below in curr_right.connections:
                    output += "   X"  # display a connection between cells
                else:
                    output += "---X"  # display a wall between cells
                curr_right = curr_right.right
            output += "\n"
            curr_below = curr_below.below
        return output
    
    
    def has_unvisited(self):
        result = False
        self.unvisited = []
        if self.left != None and self.left.visited != True:
            self.unvisited.append(self.left)
            result = True
        if self.right != None and self.right.visited != True:
            self.unvisited.append(self.right)
            result = True
        if self.above != None and self.above.visited != True:
            self.unvisited.append(self.above)
            result = True
        if self.below != None and self.below.visited != True:
            self.unvisited.append(self.below)
            result = True
        return result
    
    def __str__(self):
        return str(self.pos)
    
    def __repr__(self):
        return str(self.pos)


def dfs_create_maze(grid_point):
    grid_point.visited = True
    while grid_point.has_unvisited():
        new_unvisited = grid_point.unvisited[random.randint(0, len(grid_point.unvisited) - 1)]
        grid_point.connections.append(new_unvisited)
        new_unvisited.connections.append(grid_point)
        dfs_create_maze(new_unvisited)
        
def random_iterative_deepening_controller(grid_point):
    nodes = dl_create_maze(grid_point, random.randint(1, 5))
    #print(nodes)
    while nodes != []:
        new_nodes = []
        for node in nodes:
            new_nodes = new_nodes + dl_create_maze(node, random.randint(1, 10))
        nodes = new_nodes
        #print(nodes)
        

def iterative_deepening_controller(grid_point):
    depth = 5
    nodes = dl_create_maze(grid_point, depth)
    #print(nodes)
    while nodes != []:
        new_nodes = []
        for node in nodes:
            new_nodes = new_nodes + dl_create_maze(node, depth)
        nodes = new_nodes
        #print(nodes)
    
    
def dl_create_maze(grid_point, depth):
    grid_point.visited = True
    if depth <= 0:
        grid_point.important = True
        return [grid_point]
    next_values = []
    while grid_point.has_unvisited():
        new_unvisited = grid_point.unvisited[random.randint(0, len(grid_point.unvisited) - 1)]
        grid_point.connections.append(new_unvisited)
        new_unvisited.connections.append(grid_point)
        next_values = next_values + dl_create_maze(new_unvisited, depth - 1)
    #print(next_values)
    return next_values




def create_grid(x, y):
    # create an n by n grid of cells
    grid = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(Cell((i, j)))
        grid.append(row)


    # link the cells together
    for i in range(x):
        for j in range(y):
            if i > 0:
                grid[i][j].above = grid[i-1][j]
                grid[i-1][j].below = grid[i][j]
            if j < y-1:
                grid[i][j].right = grid[i][j+1]
                grid[i][j+1].left = grid[i][j]
    grid[x - 1][y - 1].is_goal = True
    return grid[0][0]


def create_tk_frame():
    root = Tk()
    root.title("Maze")
    root.geometry("500x600")
    canvas = Canvas(root, width=500, height=600)
    canvas.pack()
    return root, canvas
    
    

def create_maze_tk(canvas, maze):
    curr = maze
    width = 20
    height = 20
    col = 0
    while curr != None:
        canvas.create_line(10 + 20 * col, 10, 10 + 20 * (col + 1), 10, fill = "black")
        curr = curr.right
        col += 1
    


def main():
    grid = create_grid(20, 20)
    #print(type(grid))
    #random_iterative_deepening_controller(grid)
    #iterative_deepening_controller(grid)
    dfs_create_maze(grid)
    print(grid.show_maze())

if __name__ == "__main__": 
    main()
    


