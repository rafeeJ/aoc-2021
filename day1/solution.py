f = open('input.txt', 'r')

l = [int(i) for i in f]

solution_one_count = 0

for idx, val in enumerate(l):
    if(idx == 0):
        continue
    if(val > l[idx-1]):
        print('{} is bigger than {}'.format(val, l[idx-1]))
        solution_one_count += 1

print(solution_one_count)

# Part 2
def sum_of_window(arr):
    if len(arr) < 3: 
        return 0
    else: 
        return sum(arr)

windows = {idx:sum_of_window(l[idx: idx+3]) for idx, val in enumerate(l)}

solution_two_count = 0

for i in range(len(windows)):
    if i == 0: continue
    if windows[i] > windows[i-1]:
        print("{} is bigger than {}".format(windows[i], windows[i-1]))
        solution_two_count += 1

print(solution_two_count)