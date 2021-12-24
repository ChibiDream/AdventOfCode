import re

def part1():
    with open("./input.txt") as f:
        lines = f.readlines()

        codeTotal = 0
        charTotal = 0
        for line in lines:
            codeLen = len(line)

            noescapes = re.sub(r'(?:\\"|\\\\|\\x[0-9a-f]{2})', 'c', line)
            noquotes = re.sub(r'"', '', noescapes)
            charLen = len(noquotes)

            codeTotal += codeLen
            charTotal += charLen

        print(codeTotal - charTotal)


def part2():
    with open("./input.txt") as f:
        lines = f.readlines()

        codeTotal = 0
        expandTotal = 0
        for line in lines:
            codeLen = len(line)

            addbackescapes = re.sub(r'\\', '\\\\\\\\', line)
            addquoteescapes = re.sub(r'"', '\\"', addbackescapes)
            addspecialescapes = re.sub(r'\\x[0-9a-f]{2}', '\\\\xff', addquoteescapes)
            expandLen = len('"' + addspecialescapes + '"')

            codeTotal += codeLen
            expandTotal += expandLen
        print(expandTotal - codeTotal)

part1()
part2()