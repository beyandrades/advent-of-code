from aoc_tool import get_input, submit
import re

if __name__ == "__main__":
    year, day = 2024, 4
    aoc_input = get_input(year, day)
    aoc_input = aoc_input.splitlines()

    aoc_input_small = aoc_input
    sum = 0
    def make_diags():
        diags = []
        for start in range(3, len(aoc_input_small[0])):
            x, y = start, 0
            line = ""
            while x >= 0:
                line+=aoc_input_small[x][y]
                x-=1
                y+=1
            diags.append(line)
        for start in range(1, len(aoc_input_small)-3):
            x, y = len(aoc_input_small)-1, start
            line = ""
            while y < len(aoc_input_small):
                line+=aoc_input_small[x][y]
                x-=1
                y+=1
            diags.append(line)
        for start in range(len(aoc_input_small[0])-3, -1, -1):
            x, y = start, 0
            line = ""
            while x < len(aoc_input_small[0]):
                line+=aoc_input_small[x][y]
                x+=1
                y+=1
            diags.append(line)
        for start in range(1, len(aoc_input_small)-3):
            x, y = 0, start
            line = ""
            while y < len(aoc_input_small):
                line+=aoc_input_small[x][y]
                x+=1
                y+=1
            diags.append(line)
        return diags
    
    for line in aoc_input_small:
        sum+=len(re.findall('XMAS', line))
        sum+=len(re.findall('SAMX', line))
    for col in zip(*aoc_input_small):
        line = ""
        for l in col:
            line+=l
        sum+=len(re.findall('XMAS', str(line)))
        sum+=len(re.findall('SAMX', str(line)))
    diags = make_diags()
    for line in diags:
        sum+=len(re.findall('XMAS', line))
        sum+=len(re.findall('SAMX', line))  
    print(sum)
    
    



    
   
