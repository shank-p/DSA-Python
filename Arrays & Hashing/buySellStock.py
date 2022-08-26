"""
    121. Best Time to Buy and Sell Stock
    - leetcode
"""
prices = list(map(int, input().split(',')))


temp = []
for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        temp.append(prices[j] - prices[i])

print(temp)

#working