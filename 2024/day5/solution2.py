from aoc_tool import get_input, submit
import re
from collections import defaultdict


def getRulesUpdates(aoc_input):
    rules, updates = aoc_input.split('\n\n')
    rules_dict, afterrules = defaultdict(list), defaultdict(list)
    for r in rules.splitlines(): 
        rules_dict[r.split('|')[0]].append(r.split('|')[1])
        afterrules[r.split('|')[1]].append(r.split('|')[0])
    return rules_dict, afterrules, updates.splitlines()

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

    rules, afterrules, updates = getRulesUpdates(aoc_input)
    wrongs = getWrongUpdates(updates)
    sum = 0
    for update in wrongs:
        for u in update:
            afters = afterrules[u]
            if len(set(afters) & set(update)) == len(update)//2:
                sum+=int(u)
    print(sum)


    

    