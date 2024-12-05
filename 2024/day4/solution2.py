from aoc_tool import get_input, submit
import re

if __name__ == "__main__":
    year, day = 2024, 4
    aoc_input = get_input(year, day)
    aoc_input = aoc_input.splitlines()

    aoc_input_small = aoc_input
    sum = 0
    for x in range(1, len(aoc_input_small)-1):
        for y in range(1, len(aoc_input_small[0])-1):
            if aoc_input_small[x][y] == "A":
                    ld = aoc_input_small[x-1][y-1] + aoc_input_small[x][y] + aoc_input_small[x+1][y+1]
                    rd = aoc_input_small[x+1][y-1] + aoc_input_small[x][y] + aoc_input_small[x-1][y+1]
                    if (ld == "SAM" or ld == "MAS") and (rd == "SAM" or rd == "MAS"):
                        sum+=1




    print(sum)
    
    



    
   
