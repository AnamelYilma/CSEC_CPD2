s = str(input())
li = list(s)
upper = []
lower = []

for i in li:
    if i.isupper():
        upper.append(i)
    else:
        lower.append(i)

if len(upper) > len(lower):
    print(s.upper())
else:
    print(s.lower())
