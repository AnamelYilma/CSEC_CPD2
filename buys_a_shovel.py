k, r = list(map(int, input().split()))

n =1
while True:
    total = n*k
    if total % 10 == 0 or total %10 == r:
        print(n)
        break
    n+=1

    
