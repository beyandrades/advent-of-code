from aoc_tool import get_input, submit
import re
from collections import defaultdict


def getRulesUpdates(aoc_input):
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
    return rules, afterrules, updates

def getWrongUpdates(updates):
    wrongs = []
    for u in updates:
        u = u.split(',')
        for x in range(len(u)-1, -1, -1):
            befores = rules[u[x]]
            if len(set(befores) & set(u[:x])) > 0:
                wrongs.append(u)
                break
    return wrongs

if __name__ == "__main__":
    year, day = 2024, 5
    aoc_input = get_input(year, day)
    aoc_input = aoc_input.splitlines()

    rules, afterrules, updates = getRulesUpdates(aoc_input)
    wrongs = getWrongUpdates(updates)
    sum = 0
    for update in wrongs:
        for u in update:
            afters = afterrules[u]
            if len(set(afters) & set(update)) == len(update)//2:
                sum+=int(u)
    print(sum)


    

    