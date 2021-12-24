import re

def splitInstruction(str):
    res = re.match('(\d+|\w+) -> (\w+)', str)
    if res:
        return res.group(1, 2)
    res = re.match('(\w+|\d+) (AND|OR) (\w+|\d+) -> (\w+)', str)
    if res:
        return res.group(1, 2, 3, 4)
    res = re.match('(\w+|\d+) (LSHIFT|RSHIFT) (\d+) -> (\w+)', str)
    if res:
        return res.group(1, 2, 3, 4)
    res = re.match('(NOT) (\w+|\d+) -> (\w+)', str)
    if res:
        return res.group(1, 2, 3)
    return

def splitInstructions(lines):
    vals = dict()
    instructions = list()
    for line in lines:
        instruction = splitInstruction(line)
        if len(instruction) == 2 and not re.search(r'[a-z]', instruction[0]):
            vals.update({instruction[1]: int(instruction[0])})
        else:
            instructions.append(instruction)

    return (vals, instructions)

def runInstruction(instruction, vals):
    if (len(instruction) == 2):
        cin = vals.get(instruction[0])
        cout = instruction[1]
        if cin:
            return {cout: cin}
    elif (len(instruction) == 3):
        cin = instruction[1]
        cin = int(cin) if re.match(r'\d+', cin) else vals.get(cin)
        cout = instruction[2]
        if cin is not None:
            return {cout: (~cin)+(1 << 16)}
    elif (len(instruction) == 4):
        cinL = instruction[0]
        cinL = int(cinL) if re.match(r'\d+', cinL) else vals.get(cinL)
        cinR = instruction[2]
        cinR = int(cinR) if re.match(r'\d+', cinR) else vals.get(cinR)
        cout = instruction[3]

        if cinL is None or cinR is None:
            return
        
        if instruction[1] == "AND":
            return {cout: (cinL & cinR)}
        elif instruction[1] == "OR":
            return {cout: (cinL | cinR)}
        elif instruction[1] == "LSHIFT":
            return {cout: (cinL << cinR)}
        elif instruction[1] == "RSHIFT":
            return {cout: (cinL >> cinR)}
    return

def readInstructions(vals, instructions):
    incomplete = list()
    while len(instructions) > 0:
        for instruction in instructions:
            res = runInstruction(instruction, vals)
            if res:
                vals.update(res)
            else:
                incomplete.append(instruction)
        instructions = incomplete
        incomplete = list()
    return vals


def part1():
    with open("./input.txt") as f:
        lines = f.readlines()
        vals, instructions = splitInstructions(lines)
        vals = readInstructions(vals, instructions)
        
        print(vals.get('a'))
        return vals.get('a')

def part2(wireA):
    with open("./input.txt") as f:
        lines = f.readlines()
        vals, instructions = splitInstructions(lines)
        vals.update({'b': wireA})
        vals = readInstructions(vals, instructions)
        
        print(vals.get('a'))
        return vals.get('a')

wireA = part1()
part2(wireA)