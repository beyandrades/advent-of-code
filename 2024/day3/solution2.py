from aoc_tool import get_input, submit
import re

if __name__ == "__main__":
    year, day = 2024, 3
    aoc_input = get_input(year, day)
    aoc_input = aoc_input
    #print(aoc_input)
    
    sum = 0
    tokens = re.findall("mul\([0-9]{1,3},[0-9]{1,3}?\)|do\(\)|don't\(\)", aoc_input)

    print("tokens: ", tokens)
    stop = False
    for t in tokens:
        if t == "don't()":
            stop = True
        elif t == "do()":
            stop = False
        if not stop:
            t= t[4:-1]
            try:
                x, y = t.split(',')
            except:
                continue
            try:
                sum+=int(x)*int(y)
            except:
                continue
    
    print(sum)