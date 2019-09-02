# SWE 5648. 원자 소멸 시뮬레이션
import sys
sys.stdin = open("swe_5648.txt", "r")


dix = [0, 0, -1, 1]
diy = [1, -1, 0, 0]
class Atom_colide:
    def __init__(self, x, y, location, size):
        self.x = x
        self.y = y
        self.prex = x + dix[location]
        self.prey = y + diy[location]
        self.location = location
        self.size = size

    def move(self):
        global result
        x, y, prex, prey, location, size = self.x, self.y, self.prex, self.prey, self.location, self.size
        new_x, new_y, new_prex, new_prey, new_location, new_size = x + dix[location], y + diy[location], prex + dix[location], prey + diy[location], location, size

        if -1000 <= new_x <= 1000 and -1000 <= new_y <= 1000:
            if (prex, prey) in atoms and (atoms[(prex, prey)].prex, atoms[(prex, prey)].prey) == (x, y):
                result += size
                return

            if (new_x, new_y) not in atom_temp and (new_x, new_y) not in temp:
                atom_temp[(new_x, new_y)] = Atom_colide(new_x, new_y, new_location, new_size)

            elif (new_x, new_y) in atom_temp:
                result += (new_size + atom_temp[(new_x, new_y)].size)
                temp.append((new_x, new_y))
                del atom_temp[(new_x, new_y)]
                return

            elif (new_x, new_y) in temp:
                result += new_size
                return

for t in range(1, int(input())+1):
    N = int(input())
    arr = [ list(map(int, input().split())) for _ in range(N) ]

    atoms = {}
    atom_temp = {}
    temp = []
    result = 0

    for __ in range(len(arr)):
        x, y, location, size = arr[__][0], arr[__][1], arr[__][2], arr[__][3]
        atoms[(x, y)] = Atom_colide(x, y, location, size)

    while True:
        for key, value in atoms.items():
            value.move()
        else:
            if len(atom_temp) == 0:
                break
            else:
                atoms = atom_temp
                atom_temp = {}
                temp = []

    print("#{} {}".format(t, result))
