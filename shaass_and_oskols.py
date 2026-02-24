n = int(input())
a = list(map(int, input().split())) 

m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    idx = x - 1
    if idx > 0:
        a[idx - 1] += y - 1
    if idx < n - 1:
        a[idx + 1] += a[idx] - y
    a[idx] = 0
for val in a:
    print(val)
