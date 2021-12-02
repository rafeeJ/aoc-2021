f = open('input.txt', 'r')

#l = [(i.split(' ')[0], int(i.split(' ')[1])) for i in f]
l = [i for i in f]

hor = 0
dep = 0
for i in l:
    n = int(i.split(' ')[1])
    if 'forward' in i:
        hor += n
    elif 'up' in i:
        dep -= n
    elif 'down' in i:
        dep += n

print('solution 1: {} * {} = {}'.format(hor, dep, hor*dep))

# solution dos
hor = 0
dep = 0
aim = 0
for i in l:
    n = int(i.split(' ')[1])
    if 'up' in i:
        aim -= n
    elif 'down' in i:
        aim += n
    elif 'forward' in i:
        hor += n
        dep = dep + (aim * n)

print('solution 2: {} * {} = {}'.format(hor, dep, hor*dep))
