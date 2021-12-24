
def part1():
    with open("./input.txt") as f:
        lines = f.readlines()
        line = lines[0]
        s = set()
        coordX = 0
        coordY = 0
        for c in line:
            if c == 'v':
                coordY -= 1
            elif c == '^':
                coordY += 1
            elif c == '<':
                coordX -= 1
            else:
                coordX += 1
            s.add((coordX, coordY))
        print(len(s))

def part2():
    with open("./input.txt") as f:
        lines = f.readlines()
        line = lines[0]
        s = set()
        scoordX = 0
        scoordY = 0
        rcoordX = 0
        rcoordY = 0
        santa = True
        for c in line:
            if santa:
                if c == 'v':
                    scoordY -= 1
                elif c == '^':
                    scoordY += 1
                elif c == '<':
                    scoordX -= 1
                else:
                    scoordX += 1
                s.add((scoordX, scoordY))
            else:
                if c == 'v':
                    rcoordY -= 1
                elif c == '^':
                    rcoordY += 1
                elif c == '<':
                    rcoordX -= 1
                else:
                    rcoordX += 1
                s.add((rcoordX, rcoordY))
            santa = not santa
        print(len(s))

part1()
part2()