class Point:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.value = v
    def get_adjacent(self):
        adjacent = [(self.x + 1, self.y), (self.x - 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1)]
        return [point for point in adjacent if 0<= point[0] < 100 and 0 <= point[1] < 100]
    def get_coords(self):
        return (self.x, self.y)
    def get_full(self):
        return (self.x, self.y, self.value)

def init_input():
    f = open('input.txt', 'r')
    return [[int(j) for j in i.strip()] for i in f]

def create_point_matrix(inp):
    for i, y in enumerate(inp):
        for j, x in enumerate(y):
            inp[i][j] = Point(j, i, x)
    return inp

def check_list(list, target):
    smaller = True
    for num in list:
        if num <= target:
            smaller = False
    return smaller 


def sol_one():
    list_low_points = []

    inp = init_input()
    matrix = create_point_matrix(inp)

    low_points = 0    
    
    for y in matrix:
        for point in y:
            # Get the adjacent points.
            adjacent = point.get_adjacent()

            # Check the value of the points.
            points = [matrix[x[1]][x[0]].value for x in adjacent]
            if check_list(points, point.value):
                low_points += (point.value + 1)
                list_low_points.append(point)
    return (low_points, list_low_points)

sol_one_outputs = sol_one()

print(sol_one_outputs[0])

def visit(point, visited, matrix):
    print('considering point', point)
    visited.add(point)
    p = Point(point[0], point[1], matrix[point[1]][point[0]].value)
    
    adj_list = p.get_adjacent()
    print('adjacent points: ', adj_list)
    to_visit = [Point(point[0], point[1], matrix[point[1]][point[0]].value) for point in adj_list if point not in visited]
    print('To visit: ', [(i.x, i.y) for i in to_visit])
    print('Adjacent values: ', [i.value for i in to_visit])

    while not all(i.value==9 for i in to_visit):
        for point in to_visit:
            print('value of point: ', point.value)
            if point.value != 9:
                visited.union(visit((point.x, point.y), visited, matrix))
            else:
                break
    return visited


def sol_two(low_points):
    inp = init_input()
    matrix = create_point_matrix(inp)

    basin_sizes = []

    for low in low_points[:1]:
        print('starting at:', low.x, low.y)
        d = set()
        coords = visit((low.x, low.y), d, matrix)
        basin_sizes.append(coords)
    
    basin_sizes = [len(i) for i in basin_sizes]
    final = sorted(basin_sizes)[-3:]
    #return final
    return final[0] * final[1] * final[2]

print(sol_two(sol_one_outputs[1]))

