ic = int(input())
period = int(input())
keys = list(map(int, input().split()))

unique_keys = list(set(keys))
deg_divisibility = []
for i in range(len(unique_keys)):
    maxi = 0
    for j in range(0, len(unique_keys)):
        if (unique_keys[i] % unique_keys[j]==0):
            maxi+=1
    deg_divisibility.append(maxi)

strength_of_encryption = max(deg_divisibility) * (10**5)
hacker_pow = ic*period

print(deg_divisibility)
if (hacker_pow >= strength_of_encryption):
    print(0)
else:
    print(1)
print(strength_of_encryption)