def reportchecker(r):
    lastdiff=0
    for x in range(len(r)-1):
        diff = int(r[x])-int(r[x+1])
        if abs(diff) > 3 or abs(diff) < 1:
            return False
        elif diff*lastdiff < 0:
            return False
        lastdiff=diff
    return True

def testall(report):
    report = report.split(' ')
    for x in range(len(report)):
        nolevel=report[:x] + report[x+1 :]
        if reportchecker(nolevel):
            return True
    return False

if __name__ == "__main__":
    from aoc_tool import get_input, submit
    from collections import defaultdict
    year, day = 2024, 2
    aoc_input = get_input(year, day)
    reports=aoc_input.splitlines()
    count = 0
    for r in reports:
        if testall(r):
            count+=1
    print(count)

    submit(count, year, day, 2)