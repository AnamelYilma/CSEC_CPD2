import bisect
n, m, k = map(int, input().split())
x, s = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
spells = [(0, x)]
for i in range(m):
    spells.append((a[i], b[i]))
spells.sort()
costs, times = [], []
min_t = 10**18
for cost, time_val in spells:
    if time_val < min_t:
        min_t = time_val
        costs.append(cost)
        times.append(time_val)
ans = 10**18
for i, (ci, di) in enumerate([(0,0)] + list(zip(c, d))):
    if ci > s:
        continue
    rem = s - ci
    j = bisect.bisect_right(costs, rem) - 1
    t = times[j] if j >= 0 else x
    rem_n = max(0, n - di)
    ans = min(ans, rem_n * t)
print(ans)
