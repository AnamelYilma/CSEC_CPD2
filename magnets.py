n = int(input())

group = 0
prev = None

for i in range(n):
    current = input()
    if prev != current:
        group+=1
        prev = current
print(group)
