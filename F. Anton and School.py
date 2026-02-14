import sys
input = sys.stdin.read
data = input().split()

index = 0
n = int(data[index])
index += 1

b = [int(data[index + i]) for i in range(n)]
index += n
c = [int(data[index + i]) for i in range(n)]

sum_b = sum(b)
sum_c = sum(c)

if (sum_b + sum_c) % (2 * n) != 0:
    print(-1)
    sys.exit()

S = (sum_b + sum_c) // (2 * n)

a = []
ok = True

for i in range(n):
    num = b[i] + c[i] - S
    if num % n != 0 or num < 0:
        ok = False
        break
    ai = num // n
    a.append(ai)

if not ok:
    print(-1)
else:
    for i in range(n):
        if b[i] + c[i] != n * a[i] + S:
            ok = False
            break
    if ok:
        print(' '.join(map(str, a)))
    else:
        print(-1)
