f = open('input.txt', 'r')

def split_coords(line):
    coords = line.split(' -> ')
    final_coords = (tuple([int(i) for i in coords[0].split(',')]), tuple([int(i) for i in coords[1].split(',')]))
    return final_coords

l = [split_coords(i) for i in f]

array_p_one = [i for i in l if i[0][0] == i[1][0] or i[0][1] == i[1][1]]

heat_map = [[0 for col in range(1000)] for row in range(1000)]
heat_map_two = [[0 for col in range(1000)] for row in range(1000)]

for coords in array_p_one:
    #print(coords)
    if coords[0][0] == coords[1][0]:
        # X's are the same!
        c = [coords[0][1], coords[1][1]]
        min_c = min(c)
        max_c = max(c)
        #print('max: {}, min: {}'.format(max_c, min_c))
        for i in range(min_c, max_c+1):
            #print('marking {},{}'.format(coords[0][0], i))
            heat_map[i][coords[0][0]] += 1
    if coords[0][1] == coords[1][1]:
        # Y's are the same!
        c = [coords[0][0], coords[1][0]]
        min_c = min(c)
        max_c = max(c)
        #print('max: {}, min: {}'.format(max_c, min_c))
        for i in range(min_c, max_c+1):
            #print('marking {},{}'.format(i, coords[0][1]))
            heat_map[coords[0][1]][i] += 1

def sum_heatmap(heat_map):
    c = 0 
    for i in heat_map:
        for x in i:
            if x >= 2:
                c+=1
    return c

#print(sum_heatmap(heat_map))

array_p_two = [i for i in l if i not in array_p_one]

for coords in array_p_two:
    one = coords[0]
    two = coords[1]
    if one[0] < two[0]:
    # One is on the left
        if one[1] < two[1]:
            # One is top left
            #print('top left')
            x = [i for i in range(one[0], two[0]+1)]
            y = [i for i in range(one[1], two[1]+1)]
            k = zip(x, y)
            #print(k)
            for f in k:
                heat_map[f[0]][f[1]]+=1
        else:
            # One is bottom left
            #print('bottom left')
            x = [i for i in range(one[0], two[0]+1)]
            y = [i for i in range(two[1], one[1]+1)]
            r = reversed(y)
            k = zip(x, r)
            for f in k:
                heat_map[f[0]][f[1]]+=1
    else:
    # One is on the right
        if one[1] < two[1]:
            # One is top right
            #print('top right')
            x = [i for i in range(two[0], one[0]+1)]
            y = [i for i in range(one[1], two[1]+1)]
            r = reversed(y)
            k = zip(x, r)
            #print(k)
            for f in k:
                heat_map[f[0]][f[1]]+=1

        else:
            # One is bottom right
            #print('bottom right')
            x = [i for i in range(two[0], one[0]+1)]
            y = [i for i in range(two[1], one[1]+1)]
            k = zip(x, y)
            for f in k:
                heat_map[f[0]][f[1]]+=1
        
#print(sum_heatmap(heat_map_two))


for coords in l:
    #print(coords)
    if coords[0][0] == coords[1][0]:
        # X's are the same!
        c = [coords[0][1], coords[1][1]]
        min_c = min(c)
        max_c = max(c)
        #print('max: {}, min: {}'.format(max_c, min_c))
        for i in range(min_c, max_c+1):
            #print('marking {},{}'.format(coords[0][0], i))
            heat_map_two[i][coords[0][0]] += 1
    if coords[0][1] == coords[1][1]:
        # Y's are the same!
        c = [coords[0][0], coords[1][0]]
        min_c = min(c)
        max_c = max(c)
        #print('max: {}, min: {}'.format(max_c, min_c))
        for i in range(min_c, max_c+1):
            #print('marking {},{}'.format(i, coords[0][1]))
            heat_map_two[coords[0][1]][i] += 1
    one = coords[0]
    two = coords[1]
    if one[0] < two[0]:
    # One is on the left
        if one[1] < two[1]:
            # One is top left
            print('top left')
            x = [i for i in range(one[0], two[0]+1)]
            y = [i for i in range(one[1], two[1]+1)]
            k = zip(x, y)
            #print(k)
            for f in k:
                heat_map_two[f[0]][f[1]]+=1
        else:
            # One is bottom left
            print('bottom left')
            x = [i for i in range(one[0], two[0]+1)]
            y = [i for i in range(two[1], one[1]+1)]
            r = reversed(y)
            k = zip(x, r)
            for f in k:
                heat_map_two[f[0]][f[1]]+=1
    else:
    # One is on the right
        if one[1] < two[1]:
            # One is top right
            print('top right')
            x = [i for i in range(two[0], one[0]+1)]
            y = [i for i in range(one[1], two[1]+1)]
            r = reversed(y)
            k = zip(x, r)
            #print(k)
            for f in k:
                heat_map_two[f[0]][f[1]]+=1

        else:
            # One is bottom right
            print('bottom right')
            x = [i for i in range(two[0], one[0]+1)]
            y = [i for i in range(two[1], one[1]+1)]
            k = zip(x, y)
            for f in k:
                heat_map_two[f[0]][f[1]]+=1

print(sum_heatmap(heat_map_two))
