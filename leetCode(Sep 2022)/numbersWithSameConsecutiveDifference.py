"""
    967. Numbers With Same Consecutive Differences
    -leetCode
"""

n = int(input())
k = int(input())

arr = []

a = 9
while (a>=k and a>0):
    string1 = str(a)
    for i in range(n-1):
        prev = int(string1[-1])
        if prev-k >= 0:
            string1 += str(prev-k)
        else:
            string1 += str(prev+k)
    print(string1)
    arr.append(int(string1))
    string4 = str(a)
    for i in range(n-1):
        prev = int(string4[-1])
        if prev+k <= 9:
            string4 += str(prev+k)
        else:
            string4 += str(prev-k)
    print(string4)
    if int(string4) not in arr:
        arr.append(int(string4))
    rev = string1[::-1]
    if rev[0] != '0' and int(rev) not in arr:
        arr.append(int(rev))

    b = a - k
    whole_times = n//2
    half_times = n %2

    string2 = (str(a) + str(b))*whole_times + str(a)*half_times
    if int(string2) not in arr:
        arr.append(int(string2))
    if b > 0:
        string3 =  (str(b) + str(a))*whole_times + str(b)*half_times
        if int(string3) not in arr:
            arr.append(int(string3))
    a -= 1

print(arr)
