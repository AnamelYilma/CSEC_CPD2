Y,W = map(int, input().split())

m = max(Y,W)
fav = 7-m
deno = 6

a,b = fav,deno

while b!=0:
    a, b = b, a%b
gcd = a

print(f"{fav//gcd}/{deno//gcd}")
