
class Digit:
    def __init__(self, input):
        self.segments = input
        self.digit = ''
        if len(input) in [2, 3, 4, 7]:
            if len(input) == 2: self.digit = 1
            elif len(input) == 3: self.digit = 7
            elif len(input) == 4: self.digit = 4
            elif len(input) == 7: self.digit = 8
    def length(self):
        return len(self.segment)

class Digit_List:
    def __init__(self, input):
        self.list = input
    def get_digits_of_length(self, n):
        return [i.segments for i in self.list if len(i.segments) == n]
    def print_list(self):
        print([i.segments for i in self.list])

class Mess:
    def __init__(self, input):
        self.signals = input
        d = {}
        for i in input:
            if not d.get(i):
                d[i] = 1
            else:
                d[i] += 1
        self.occurences = d
    def unique_letters(self):
        unique = []
        for letter in self.occurences.keys():
            if self.occurences.get(letter) == 1:
                unique.append(letter)
        return unique

def parse_line(line):
    arr = line.split(' | ')
    digits = arr[0].split(' ')
    output = arr[1].strip().split(' ')
    return (digits, output)

def init_input():
    f = open('input.txt', 'r')
    return [parse_line(i) for i in f]

for_reference = {
                0: 6, 
                1: 2, # Done
                2: 5, # Done
                3: 5, # Done
                4: 4, # Done
                5: 5, # Done
                6: 6, 
                7: 3, # Done
                8: 7, # Done
                9: 6
                }

def part_one():
    part_one_input = init_input()
    c = 0
    for line in part_one_input:
        for output in line[1]:
            if len(output) in [2, 3, 4, 7]:
                c += 1
    return c

print('Solution for p1 is: {}'.format(part_one()))

def get_unique(arr, dig):
    for i in arr:
        if dig in i:
            return i

def decode_digits(line):
    decoder = {i:'' for i in range(10)}
    l = Digit_List([Digit(i) for i in line])    
    
    # Get unique lengths:
    for idx, digit in enumerate(l.list):
        if digit.digit:
            decoder[digit.digit] = ''.join(sorted(l.list[idx].segments))
    
    # Get 5
    fives = Mess(''.join(l.get_digits_of_length(5)))    
    zero_segment = ''.join([i for i in fives.unique_letters() if i in decoder.get(4)])
    
    decoder[5] = get_unique(l.get_digits_of_length(5), zero_segment)
    
    # Now that we have 5, we can work out 2 and 3.
    filtered = [i for i in l.get_digits_of_length(5) if not i == decoder.get(5)]
    fives = Mess(''.join(filtered))
    
    three_segment = ''.join([i for i in fives.unique_letters() if i in decoder.get(1)])
    five_segment = ''.join([i for i in fives.unique_letters() if i not in decoder.get(1)])
    
    decoder[3] = ''.join(sorted(get_unique(filtered, three_segment)))
    decoder[2] = ''.join(sorted(get_unique(filtered, five_segment)))
    
    two_segment = ''.join([i for i in decoder.get(1) if i != three_segment])
    
    decoder[6] = ''.join([i for i in decoder.get(8) if i != two_segment])
    decoder[9] = ''.join([i for i in decoder.get(8) if i!= five_segment])
    decoder[5] = ''.join(sorted(decoder.get(5)))

    for i in l.list:
        x = ''.join(sorted(str(i.segments)))
        if x not in decoder.values():
            decoder[0] = x
    
    return decoder    

def calc_output(digits, decoder):
    count = 0
    for idx, val in enumerate(digits):
        digits[idx] = ''.join(sorted(val))
    
    string = ''

    for digit in digits:
        for i in decoder.keys():
            if decoder.get(i) == digit:
                string += str(i)
    return int(string)

def part_two():
    input = init_input()
    count = 0
    for line in input:
        decoder = decode_digits(line[0])
        count += calc_output(line[1], decoder)
    print(count)

part_two()