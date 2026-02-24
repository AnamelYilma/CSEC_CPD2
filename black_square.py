i = list(map(int, input().split()))
s = input()
total = 0

for sc in s:
    if sc == "1":
        total+=i[0]
    elif sc == "2":
        total +=i[1]
    elif sc == "3":
        total +=i[2]
    else:
        total+=i[3]
        
print(total)
