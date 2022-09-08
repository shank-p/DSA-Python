"""
    frequency arr
"""

nums = [1, 2, 2, 5, 6, 7, 7, 7, 4, 4, 3]

def try1(nums):
    temp1 = []
    temp2 = []
    arr = []
    for i in nums:
        if i not in temp1:
            temp1.append(i)
            temp2.append(nums.count(i))

    while len(temp1) > 0:
        maxi = max(temp2)
        for i in range(len(temp1)):
            if temp2[i] == maxi:
                for j in range(maxi):
                    arr.append(temp1[i])
                temp1.pop(i)
                temp2.pop(i)
                break
    print(arr)


