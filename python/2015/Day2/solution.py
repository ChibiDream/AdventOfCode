import re

def getDimensions(str):
    arr = [int(n) for n in re.findall(r'\d+', str)]
    arr.sort(reverse=True)
    return arr

def part1():
    with open("./input.txt") as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            l, w, h = getDimensions(line)
            total += 2 * l * w + 2 * l * h + 2 * w * h + w * h
        print(total)

def part2():
    with open("./input.txt") as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            l, w, h = getDimensions(line)
            total += 2 * w + 2 * h + l * w * h
        print(total)

part1()
part2()