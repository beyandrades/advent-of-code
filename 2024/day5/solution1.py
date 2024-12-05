from aoc_tool import get_input, submit
import re
from collections import defaultdict

def getRulesUpdates(aoc_input):
    rules = defaultdict(list)
    updates = []
    found = False
    for x in aoc_input: 
        if x == '':
            found = True
        elif found:
            updates.append(x)
        else:
            rules[x.split('|')[0]].append(x.split('|')[1])
    return rules, updates


if __name__ == "__main__":
    year, day = 2024, 5
    aoc_input = get_input(year, day)
    aoc_input = aoc_input.splitlines()

    rules, updates = getRulesUpdates(aoc_input)
    sum = 0
    for u in updates:
        flag = False
        u = u.split(',')
        for x in range(len(u)-1, -1, -1):
            afters = rules[u[x]]
            if len(set(afters) & set(u[:x])) > 0:
                flag = True
                break
        if not flag:
            sum+=int(u[len(u)//2])

    print(sum)


    

    


    