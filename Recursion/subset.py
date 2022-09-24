arr = [1, 2, 3]

substr = []
def substring(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            substr.append(arr[i:j])
substring(arr)
print(substr)

subsets = []
def subsequence(arr, i, subarr):
    if len(arr)==i:
        if subarr not in subsets:
            subsets.append(subarr)
        return
    subsequence(arr, i+1, subarr+[arr[i]]) 
    subsequence(arr, i+1, subarr)

subsequence(arr, 0, [])
print(subsets)
    
