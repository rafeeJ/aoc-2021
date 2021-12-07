f = open('input.txt', 'r')

l = [i for i in f]
fish = [int(i) for i in l[0].split(',')]

def create_d(fish):
    d = {i:0 for i in range(9)}
    for i in fish:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
    return d

def sum_d(d):
    c=0
    for i in d.values():
        c += i
    return c

def sol():
    d = create_d(fish)
    print(d)
    for day in range(1, 257):
        print('After day: {}'.format(day))
        to_create = 0
        for k in d.keys():
            if k == 0: to_create = d.get(0)
            else: d[k-1] = d[k]
        d[8] = to_create
        if d.get(6):
            d[6] += to_create
        else:
            d[6] = to_create
        print(d)
    print(sum_d(d))
    
sol()