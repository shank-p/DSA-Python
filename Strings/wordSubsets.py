"""
    916. Word Subsets
    - leetCode
"""

words1 = input().split()
words2 = input().split()

res = []
for i in words1:
    valid = True
    for j in words2:
        b = list(j)
        a = list(i)
        print('a', a)
        print('b', b)
        for k in b:
            if (k not in a):
                valid = False
                break
            a.remove(k)
            print('pop:', k)
        if (not valid):
            break
    if (valid):
        res.append(i)
    print('res', res)
    print()


print (res)
            
       

