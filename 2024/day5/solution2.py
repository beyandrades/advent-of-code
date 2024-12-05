from aoc_tool import get_input, submit
import re
from collections import defaultdict

if __name__ == "__main__":
    year, day = 2024, 5
    aoc_input = get_input(year, day)
    aoc_input = aoc_input.splitlines()

    #file = 'day 5/input.txt'
    #f=open(file,"r")
    #aoc_input=f.read().splitlines()
    rules = defaultdict(list)
    afterrules = defaultdict(list)
    updates = []
    found = False
    for x in aoc_input: 
        if x == '':
            found = True
        elif found:
            updates.append(x)
        else:
            before, after = x.split('|')
            afterrules[after].append(before)
            rules[before].append(after)

    sum = 0
    wrongs = []
    for u in updates:
        flag = False
        u = u.split(',')
        for x in range(len(u)-1, -1, -1):
            befores = rules[u[x]]
            if len(set(befores) & set(u[:x])) > 0:
                wrongs.append(u)
                break

    for update in wrongs:
        for u in update:
            afters = afterrules[u]
            if len(set(afters) & set(update)) == len(update)//2:
                sum+=int(u)
            

    print(sum)


    