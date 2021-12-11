class Octopus:
    def __init__(self, x, y, energy):
        self.x = x
        self.y = y
        self.energy = energy

    def get_energy(self):
        return self.energy

    def set_energy(self, energy):
        self.energy = energy
        return self.energy

    def increase_energy(self, energy):
        return self.set_energy(self.get_energy() + energy)

    def get_adjacent(self):
        adj = []
        for i in range(self.x - 1, self.x + 2):
            for j in range(self.y - 1, self.y + 2):
                adj.append((i, j))
        return [k for k in adj if -1 < k[0] < 10 and -1 < k[1] < 10 and k != (self.x, self.y)]


class Field:
    def __init__(self, matrix):
        self.layout = [[Octopus(x, y, v) for x, v in enumerate(val)]
                                for y, val in enumerate(matrix)]

    def get_layout(self):
        return self.layout

    def inc_field(self, val):
        for y in self.layout:
            for octopus in y:
                octopus.increase_energy(val)

    def value_field(self):
        return [[octopus.get_energy() for octopus in y] for y in self.get_layout()]

    def get_flashing(self):
        flash = []
        for y in self.get_layout():
            for oct in y:
                if oct.get_energy() > 9:
                    flash.append(oct)
        return flash

    def get_octopus(self, x, y):
        return self.get_layout()[y][x]

    def get_flashed(self):
        flashed = []
        for y in self.get_layout():
            for oct in y:
                if oct.get_energy() == 0:
                    flashed.append(oct)
        return flashed
    
    def flash_neighbours(self, octopus):
        adj = [self.get_octopus(o[0], o[1]) for o in octopus.get_adjacent()]
        for o in adj:
            o.increase_energy(1)

def init_input():
    f = open('input.txt', 'r')
    return [[int(y) for y in i if y != '\n'] for i in f]

def step(field):
    # Increase the energy.
    field.inc_field(1)
    print('After we increase everyone: ', field.value_field())
    
    flashed = []
    while True:
        # Then, any octopus that has energy of 9 < FLASHES.
        to_flash = [o for o in field.get_flashing() if o not in flashed]
        if to_flash:
            print('There are {} flashy mfs here \n'.format(len(to_flash)))
            # For each octopus with energy > 9
            for octopus in to_flash:
                print('Flashing octopus at {}'.format((octopus.x, octopus.y)))
                octopus.set_energy(0)
                flashed.append(octopus)
                field.flash_neighbours(octopus)
            print(field.value_field())
        else:
            break

    # Set flashed octopi to energy 0
    for i in flashed:
        i.set_energy(0)
    print(field.value_field())
    print('Done with step! \n')

    return field


def sol_one():
    c = 0
    f = Field(init_input())

    print('Starting: {}'.format(f.value_field()))

    c = 0
    for i in range(1, 101):
        print('After step: {}'.format(i))
        f = step(f)
        c += len(f.get_flashed())
    return c

def sol_two():
    c = 0
    f = Field(init_input())

    print('Starting: {}'.format(f.value_field()))

    c=0
    while True:
        f = step(f)
        x = len(f.get_flashed())
        c += 1 
        if x == 100:
            break
    return c

print(sol_one())
print(sol_two())
