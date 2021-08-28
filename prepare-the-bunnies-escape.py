from Queue import deque
wall = 1
passable = 0

class Node:
    def __init__(self, x, y, saldo):
        self.x = x
        self.y = y
        self.saldo = saldo

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.saldo == other.saldo

    def __hash__(self):
        return self.x ^ self.y

    def get_neighbors(self, map, width, height):
        neighbors = []
        if self.y < height - 1:
            if map[self.y + 1][self.x] == passable:
                neighbors.append(Node(self.x, self.y + 1, self.saldo))
            elif self.saldo > 0:
                neighbors.append(Node(self.x, self.y + 1, self.saldo - 1))
        if self.y > 0:
            if map[self.y - 1][self.x] == passable:
                neighbors.append(Node(self.x, self.y - 1, self.saldo))
            elif self.saldo > 0:
                neighbors.append(Node(self.x, self.y - 1, self.saldo - 1))
        
        if self.x < width - 1:
            if map[self.y][self.x + 1] == passable:
                neighbors.append(Node(self.x + 1, self.y, self.saldo))
            elif self.saldo > 0:
                neighbors.append(Node(self.x + 1, self.y, self.saldo - 1))
        
        if self.x > 0:
            if map[self.y][self.x - 1] == passable:
                neighbors.append(Node(self.x - 1, self.y, self.saldo))
            elif self.saldo > 0:
                neighbors.append(Node(self.x - 1, self.y, self.saldo - 1))
        return neighbors

# BFS modified.
# The solution will do a breadth first search, modified
# to break at most one wall
def solution(map):
    height = len(map)
    width = len(map[0])
    start = Node(0, 0, 1)
    
    frontier = deque([start])
    distmap = {start: 1}
    
    while frontier:
        current = frontier.popleft()
        if current.x == width - 1 and current.y == height - 1:
            return distmap[current]
        
        for next in current.get_neighbors(map, width, height):
            if not (next in distmap.keys()):
                distmap[next] = distmap[current] + 1
                frontier.append(next)
                
    

print solution([[0, 1, 1, 0],
                [0, 0, 0, 1], 
                [1, 1, 0, 0], 
                [1, 1, 1, 0]])

print solution([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

print solution([[0, 0, 0, 0, 0, 0], 
                [1, 1, 1, 1, 1, 0], 
                [0, 0, 0, 0, 0, 0], 
                [0, 1, 1, 1, 1, 1], 
                [0, 1, 1, 1, 1, 1], 
                [0, 0, 0, 0, 0, 0]])

print solution([[0, 1, 0, 0], 
                [0, 0, 0, 0], 
                [0, 0, 1, 1], 
                [0, 1, 1, 0], 
                [0, 1, 1, 0]])