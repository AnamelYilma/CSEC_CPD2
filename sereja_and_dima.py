n = int(input())
a = list(map(int, input().split()))
dp = [[0] * n for i in range(n)]

for i in range(n):
    dp[i][i] = a[i] 

for length in range(2, n + 1):
    for l in range(0, n - length + 1):
        r = l + length - 1
        dp[l][r] = max(a[l] - dp[l + 1][r], a[r] - dp[l][r - 1])

total = sum(a)
diff = dp[0][n - 1]               
sereja = (total + diff) // 2
dima = (total - diff) // 2

print(sereja, dima)
