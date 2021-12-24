
def part1():
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        floor = 0
        for c in lines[0]:
            if (c == "("):
                floor += 1
            else:
                floor -= 1
        print(floor)

def part2():
    with open("input.txt", 'r') as f:
        lines = f.readlines()
        floor = 0
        index = 0
        for c in lines[0]:
            if (c == "("):
                floor += 1
            else:
                floor -= 1
            index += 1
            if floor < 0:
                print(index)
                return

part1()
part2()