from os import major


f = open('input.txt', 'r')

l = [i for i in f]
moves = [int(i) for i in l[0].split(',')]

def sol():
    d = {i:0 for i in range(max(moves)+1)}
    for i in moves:
        d[i] +=1
    
    min_fuel = 10000000000
    for i in d.keys():
        
        # What is the fuel for everyone to come here?
        fuel = 0
        for j in d.keys():
            if i == j: 
                continue
            elif fuel > min_fuel:
                break
            else: 
                fuel += abs(i - j) * d.get(j)
        
        if fuel < min_fuel: min_fuel = fuel
    print(min_fuel)

def sol_two():
    d = {i:0 for i in range(max(moves)+1)}
    for i in moves:
        d[i] +=1
    
    min_fuel = 10000000000
    for i in d.keys():
        
        # What is the fuel for everyone to come here?
        fuel = 0
        for j in d.keys():
            if i == j: 
                continue
            elif fuel > min_fuel:
                break
            else: 
                s = sum(range(1, abs(i - j)+1))
                fuel += s * d.get(j)
        
        if fuel < min_fuel: min_fuel = fuel
    print(min_fuel)

# sol()
sol_two()