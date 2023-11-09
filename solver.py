from heap import *

class Arc:
    def __init__(self, from_node, to_node, cost = 1):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost
        assert cost > 0, (f"Cost cannot be negative: {self}, cost={cost}")
        
        
class Path:
    def __init__(self, prior, new = None):
        self.prior= prior
        self.new = new
        if new is None:
            self.cost = 0
        else:
            self.cost = prior.cost + new.cost
            
    def end(self):
        if self.new is None:
            return self.prior
        else:
            return self.new.to_node

    def __repr__(self):
        """returns a string representation of a path"""
        #if self.new is None:
        #    return str(self.prior)
        #else:
        #    return f"{self.prior} --> {self.new.to_node}"
        if self.new is None:
            return str(self.prior)
        else:
            return str(self.new.to_node)

class Solver:
    def __init__(self, problem):
        self.problem = problem
        self.initialize_frontier()
        self.add_to_frontier(Path(problem.start_node()))
        pass
    
    def solve(self):
        while not self.is_frontier_empty():
            current_path = self.remove_from_frontier()
            if self.problem.is_goal(current_path.end()):
                self.solution = current_path
                return current_path

            neighbours = self.problem.neighbours(current_path.end())
            for neighbour in neighbours:
                self.add_to_frontier(Path(current_path, neighbour))
        print("no solutions found")
        return None
        
    
    def initialize_frontier(self):
        self.frontier = []
    
    def add_to_frontier(self, path):
        self.frontier.append(path)
        pass
    
    def remove_from_frontier(self):
        return self.frontier.pop()
        
    def is_frontier_empty(self):
        return self.frontier == []


class PQFrontier:
    def __init__(self):
        self.queue = Heap()
        self.length = 0
        
    def add(self, path, value):
        self.length += 1
        self.queue.add(WeighedItem(path, value))

    def pop(self):
        item = self.queue.pop()
        return item.value

    def is_empty(self):
        return self.queue.is_empty()
    

class AStarSolver(Solver):
    def __init__(self, problem):
        super().__init__(problem)
    
    def initialize_frontier(self):
        self.frontier = PQFrontier()
    
    def is_frontier_empty(self):
        return self.frontier.is_empty()
    
    def add_to_frontier(self, path):
        value = path.cost + self.problem.heuristic(path.end())
        self.frontier.add(path, value)
    

class Problem:
    def start_node(self):
        raise NotImplementedError("start_node")
    
    def is_goal(self, node):
        raise NotImplementedError("is_goal")

    def heuristic(self, node):
        return 0

    def neighbours(self, node):
        raise NotImplementedError("neighbours")
    
