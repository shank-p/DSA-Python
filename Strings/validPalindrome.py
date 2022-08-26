"""
    125. Valid Palindrome
    - LeetCode
"""

s = input()

s = s.lower()
arr = []

for i in s:
    if i.isalnum():
        arr.append(i)
print(''.join(arr))
for i in range(len(arr)//2):
    if arr[i] != arr[-(i+1)]:
        print(-1)
        break

"""
"""

i = 0
j = len(s) - 1

while(i <= j):
    print(s[i:j+1])
    print('i', s[i], i)
    print('j', s[j], j)
    print()
    if s[i].isalnum() != True:
        i += 1
        continue
    if s[j].isalnum() != True:
        j -= 1
        continue
    if (s[i] != s[j]):
        print(-1)
        break
    i += 1
    j -= 1
