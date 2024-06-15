num = []
with open("num.txt") as file:
    for line in file:
        num.append(int(line.rstrip()))

sortednum = sorted(num)
print(sortednum[-1])