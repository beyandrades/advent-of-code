from collections import defaultdict
file = 'input.txt'
f=open(file,"r")
lines=f.read().splitlines()
row1 = []
row2  = defaultdict(int)

for x in lines:
    a, b = x.split('   ')
    row1.append(int(a))
    row2[int(b)]+=1
sum = 0
for a in row1:
    sum+=row2[a]*a
print(sum)
f.close()