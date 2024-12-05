from collections import defaultdict
file = 'input.txt'
f=open(file,"r")
reports=f.read().splitlines()
count = 0
for r in reports:
    flag = False
    lastdiff=0
    r = r.split(' ')
    for x in range(len(r)-1):
        diff = int(r[x])-int(r[x+1])
        if abs(diff) > 3 or abs(diff) < 1:
            flag = True
            break
        elif diff*lastdiff < 0:
            flag = True
            break
        lastdiff=diff

    if not flag:
        count+=1
print(count)

def testall(report):
    for x in range(len(report)):
        nolevel = []
        nolevel.append(report[:x])
        nolevel.append(report[x+1:])
        if reportchecker(nolevel):
            return True