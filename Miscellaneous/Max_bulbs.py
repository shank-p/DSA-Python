n = int(input())
machine = list(map(int, input().split()))

sum = 0
for i in range(len(machine)):
    temp = machine[i] * (n - i+1)
    if temp > sum :
        sum = temp
