f = open('input.txt', 'r')

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Line:
    def __init__(self, one, two):
        self.one = one
        self.two = two
    
    def max_y(self):
        if self.one.y > self.two.y:
            return self.one.y
        else:
            return self.two.y
    
    def min_y(self):
        if self.one.y > self.two.y:
            return self.two.y
        else:
            return self.one.y
    
    def max_x(self):
        if self.one.x > self.two.x:
            return self.one.x
        else:
            return self.two.x
    
    def min_x(self):
        if self.one.x > self.two.x:
            return self.two.x
        else:
            return self.one.x

def split_coords(line):
    coords = line.split(' -> ')
    left = Point([int(i) for i in coords[0].split(',')][0], [int(i) for i in coords[0].split(',')][1])
    right = Point([int(i) for i in coords[1].split(',')][0], [int(i) for i in coords[1].split(',')][1])
    return Line(left, right)

def sum_heatmap(heat_map):
    c = 0 
    for i in heat_map:
        for x in i:
            if x >= 2:
                c+=1
    return c

lines = [split_coords(i) for i in f]

hor_ver = [line for line in lines if line.one.x == line.two.x or line.one.y == line.two.y]

heat_map = [[0 for col in range(1000)] for row in range(1000)]

for line in hor_ver:
    if line.one.x == line.two.x:
        x = line.one.x
        for y in range(line.min_y(), line.max_y() + 1):
            heat_map[x][y] += 1

    elif line.one.y == line.two.y:
        y = line.one.y
        for x in range(line.min_x(), line.max_x() + 1):
            heat_map[x][y] += 1

print(sum_heatmap(heat_map))

diags = [i for i in lines if i not in hor_ver]

for line in diags:
    if line.one.x < line.two.x:
        x = [x for x in range(line.one.x, line.two.x+1)]
        y = []
        if line.one.y < line.two.y:
            y = [y for y in range(line.one.y, line.two.y+1)]
        else:
            y = reversed([y for y in range(line.two.y, line.one.y+1)])
        coords = zip(x, y)
        for coord in coords:
            heat_map[coord[0]][coord[1]] += 1
    else:
        x = [x for x in range(line.two.x, line.one.x+1)]
        y = []
        if line.one.y < line.two.y:
            y = reversed([y for y in range(line.one.y, line.two.y+1)])
        else:
            y = [y for y in range(line.two.y, line.one.y+1)]
        coords = zip(x, y)
        for coord in coords:
            heat_map[coord[0]][coord[1]] += 1

print(sum_heatmap(heat_map))