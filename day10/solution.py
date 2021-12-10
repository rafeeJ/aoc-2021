from collections import Counter

def init_input():
    f = open('input.txt', 'r')
    return [i for i in f]

open_chars = ['[', '{', '(', '<']
closed_chars = [']', '}', ')', '>']
mapping = dict(zip(open_chars, closed_chars))

vals = {')': 3, ']': 57, '}': 1197, '>': 25137}

def check_syntax(code):
    processed = []
    valid = ''
    for char in code:
        if char in open_chars:
            processed.append(char)
        elif char == mapping[processed[-1]]:
            processed.pop()
        else:
            valid = char
            break
    return valid

def sol_one():
    inp = init_input()
    arr = []
    for idx, code in enumerate(inp):
        x = check_syntax(code)
        if x:
            arr.append((idx, x))
    arr_occ = [i[1] for i in arr if i[1] != '\n']
    d = Counter(arr_occ)
    c = 0
    for i in d.keys():
        c += vals[i] * d[i]
    return c, [i[0] for i in arr if i[1] != '\n']

sol_one_out = sol_one()

print(sol_one_out[0])

vals_inc = {')': 1, ']': 2, '}': 3, '>': 4}

def check_incomplete(code):
    processed = []
    for char in code:
        if char in open_chars:
            processed.append(char)
        elif char == mapping[processed[-1]]:
            processed.pop()
        elif char == '\n':
            break
        else:
            continue
    return [mapping[i] for i in reversed(processed)]

def sol_two(inv):
    inp = [v for i,v in enumerate(init_input()) if i not in inv]
    scores = []
    for code in inp:
        seq = check_incomplete(code)
        c = 0
        for char in seq:
            c = c * 5
            c += vals_inc[char]
        scores.append(c)
    return sorted(scores)[int((len(scores)/2))]
    
print(sol_two(sol_one_out[1]))