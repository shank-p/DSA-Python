arr = [2 ,10 ,3 ,5 ,4 ,1 ,9 ,5 ,4]
n = 9
beauty = n

for i in range(len(arr)):
    d = {}
    d[arr[i]] = 1
    for j in range(i + 1, len(arr)):
        if arr[j] not in d:
            d[arr[j]] = 1
        else:
            d[arr[j]] = 0
            # temp.add(arr[j])
        beauty += sum([i for i in d.values()]) #len(temp) - count
print (beauty)