import re

def part1():
    with open("./input.txt") as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            vowels = len(re.findall(r'[aeiou]', line)) >= 3
            pair = re.search(r'([a-z])\1', line)
            denied = re.search(r'(?:ab|cd|pq|xy)', line)
            if vowels and pair and not denied:
                total += 1

        print (total)
            

def part2():
    with open("./input.txt") as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            pair = re.search(r'([a-z])([a-z])[a-z]*\1\2', line)
            split = re.search(r'([a-z])[a-z]\1', line)
            if pair and split:
                total += 1

        print (total)

part1()
part2()