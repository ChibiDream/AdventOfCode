import re

def splitInstruction(line):
    return re.match(r'(toggle|turn off|turn on) (\d+),(\d+) through (\d+),(\d+)', line).group(1, 2, 3, 4, 5)

def part1():
    with open("./input.txt") as f:
        lines = f.readlines()

        lights = [ [ False for col in range(1000) ] 
                    for row in range(1000) ]

        for line in lines:
            ins, x1, y1, x2, y2 = splitInstruction(line)
            for i in range(int(x1), int(x2) + 1):
                for j in range(int(y1), int(y2) + 1):
                    if (ins == "toggle"):
                        lights[i][j] = not lights[i][j]
                    elif (ins == "turn off"):
                        lights[i][j] = False
                    elif (ins == "turn on"):
                        lights[i][j] = True
        print(sum(sum(lights, [])))


def part2():
    with open("./input.txt") as f:
        lines = f.readlines()

        lights = [ [ 0 for col in range(1000) ] 
                    for row in range(1000) ]

        for line in lines:
            ins, x1, y1, x2, y2 = splitInstruction(line)
            for i in range(int(x1), int(x2) + 1):
                for j in range(int(y1), int(y2) + 1):
                    if (ins == "toggle"):
                        lights[i][j] += 2
                    elif (ins == "turn off"):
                        if (lights[i][j] > 0):
                            lights[i][j] -= 1
                    elif (ins == "turn on"):
                        lights[i][j] += 1
        print(sum(sum(lights, [])))

part1()
part2()