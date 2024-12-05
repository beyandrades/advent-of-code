from aoc_tool import get_input, submit
import re

if __name__ == "__main__":
    year, day = 2024, 3
    aoc_input = get_input(year, day)
    aoc_input = aoc_input
    #print(aoc_input)
    
    sum = 0
    tokens = re.findall("mul\([0-9]{1,3},[0-9]{1,3}?\)", aoc_input)
    print("tokens: ", tokens)
    #tokens = ['mul(738^--^)', 'mul(60,730)', 'mul(958,89)', 'mul(371,786)', 'mul(151,757)', 'mul(644,833)', 'mul(480,246)', 'mul(305,497)', 'mul(233,355)', 'mul(412,498^how())']
    for t in tokens:
        t= t[4:-1]
        try:
            x, y = t.split(',')
        except:
            #print("broke", t)
            continue
        try:
            sum+=int(x)*int(y)
        except:
            #print("broke", t)
            continue
    
    print(sum)