word = input()

current = 0
total = 0

for ch in word:
    target = ord(ch)-ord('a')
    diff = abs(target - current)
    total +=min(diff, 26-diff)
    current=target

print(total) 
