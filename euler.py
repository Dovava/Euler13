num = open("num.txt")
lines = num.readlines()
for l in range(0,len(lines)):
    lines[l] = int(lines[l])
linesum = sum(lines)
answer = str(linesum)[0:10]
print(answer)