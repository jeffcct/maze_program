class WeighedItem:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
    def __lt__(self, other):
        if isinstance(other, int):
            return self.weight < other
        if not isinstance(other, WeighedItem):
            raise TypeError("Can't compare WeighedItem with non-Weighed_Items")
        return self.weight < other.weight
    
    def __gt__(self, other):
        if isinstance(other, int):
            return self.weight > other
        if not isinstance(other, WeighedItem):
            raise TypeError("Can't compare WeighedItem with non-Weighed_Items")
        return self.weight > other.weight
    
    def __str__(self):
        return str(self.value) + " " + str(self.weight)
    
    def __repr__(self):
        return str(self.value) + " " + str(self.weight)

class Heap:
    def __init__(self):
        self.vals = [0]
        self.length = 0
    
    def add(self, val, weight = None):
        if not isinstance(val, WeighedItem):
            if weight == None:
                print("didn't add item as it was the wrong type")
                return -1
            val = WeighedItem(val, weight)
        self.length += 1
        self.vals.append(val)
        self.percolate_up(self.length)
        
    def is_empty(self):
        return self.length == 0
    
    def print_weights(self):
        print("[", end = "")
        for val in self.vals[1:]:
            print(val.weight, end = ", ")
        print("]")
            
        
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Tried popping from an empty heap")
        out = self.vals[1]
        if self.length == 0:
            return self.vals.pop()
        self.vals[1] = self.vals[self.length]
        self.length -= 1
        self.vals.pop()
        self.percolate_down(1)
        return out
        
        
    def percolate_up(self, position):
        if position == 1:
            return
        parent = position // 2
        if self.vals[position] < self.vals[parent]:
            self.vals[position], self.vals[parent] = self.vals[parent], self.vals[position]
            self.percolate_up(parent)
    
    def percolate_down(self, position):
        child1 = position * 2
        child2 = position * 2 + 1
        if child1 >= self.length:
            return
        
        if child2 >= self.length and self.vals[child1] > self.vals[position]:
            self.vals[child1], self.vals[position] = self.vals[position], self.vals[child1]
            return
            
        if self.vals[child1] < self.vals[child2]:
            min_child = child1
        else:
            min_child = child2
            
        if self.vals[position] > self.vals[min_child]:
            self.vals[min_child], self.vals[position] = self.vals[position], self.vals[min_child]
            self.percolate_down(min_child)

        
