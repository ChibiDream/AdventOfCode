import hashlib

def part1():
    with open("./input.txt") as f:
        lines = f.readlines()
        input = lines[0]
        inc = 0
        hres = ""
        while (hres[0:5] != "00000"):
            inc += 1
            hstr = "" + input + str(inc)
            hres = hashlib.md5(hstr.encode()).hexdigest()
        print(inc)

def part2():
    with open("./input.txt") as f:
        lines = f.readlines()
        input = lines[0]
        inc = 346386
        hres = ""
        while (hres[0:6] != "000000"):
            inc += 1
            hstr = "" + input + str(inc)
            hres = hashlib.md5(hstr.encode()).hexdigest()
        print(inc)

part1()
part2()