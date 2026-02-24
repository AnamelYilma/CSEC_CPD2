n = int(input())
event = list(map(int, input().split()))

crime = 0
free_police = 0

for i in event:
    if free_police > 0 and i == -1:
        free_police-=1
    elif i>0:
        free_police+=i
    elif i == -1:
        crime+=1

print(crime)
