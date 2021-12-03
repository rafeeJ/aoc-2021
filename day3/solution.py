f = open('input.txt', 'r')

l = [i for i in f]
x = list(l)

m = {i:0 for i in range(len(l[0])-1)}

for i in l:
    for j, k in enumerate(i.strip()):
        if int(k) == 1:
            m[j] += 1

gamma_rate = ''
epsilon_rate = ''

for i in m.values():
    if i == 0: continue
    if(i > len(l)/2):
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

print('gamma: {}'.format(gamma_rate))
print('epsilon: {}'.format(epsilon_rate))
print('{} * {} = {}\n'.format(int(gamma_rate, 2), int(epsilon_rate, 2)-1, int(epsilon_rate, 2)*int(gamma_rate, 2)))

##### Part two
from collections import Counter

print('part two:\n')

# Life support rating = ogr * csr
ogr = ''
csr = ''

bit = 0

while bit!=12:    
    # calc most occurring bit in place i
    mob = ''
    c = 0
    for i in l:
        if int(i[bit]) == 1:
            c +=1
    if c >= len(l)/2: mob = '1'
    else: mob = '0'

    print('mob is {}, {} occurrences out of {}'.format(mob, c, len(l)))

    l = [i for i in l if i[bit] == mob]
            
    print('{} readings remain'.format(len(l)))

    if len(l) == 1: 
        print('done {}'.format(int(l[0], 2)))
        break
    bit += 1

bit = 0
while bit!=12:
    lob = ''
    c = 0
    for i in x:
        if int(i[bit]) == 1:
            c +=1
    if c >= len(x)/2: lob = '0'
    else: lob = '1'  

    print('lob is {}, {} occurrences out of {}'.format(lob, c, len(x)))
  
    x = [i for i in x if i[bit] == lob]

    print('{} readings remain'.format(len(x)))

    if len(x) == 1: 
        print('done {}'.format(int(x[0],2)))
        break
    bit += 1

print('CSR*OGR={}'.format(int(x[0], 2)*int(l[0], 2)))