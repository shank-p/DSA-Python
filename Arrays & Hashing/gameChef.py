"""
    Game of Chef
    - CodeChef
"""

test_cases = int(input())
for i in range(test_cases):
    no_of_people = int(input())
    arr = list(map(int, input().split()))

    if (len(arr) == 0):
        print(0) #return 
        continue

    max_sum = current_sum = arr[0]
    for i in arr[1:]:
        if current_sum < 0:
            current_sum = 0
        current_sum += i
        max_sum = max(max_sum, current_sum)
    print(max_sum)
    