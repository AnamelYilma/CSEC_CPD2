s = input().strip()
t = input().strip()

pos = 0
for ch in t:
    if ch == s[pos]:
        pos += 1
        if pos == len(s):
            break

print(pos + 1)
