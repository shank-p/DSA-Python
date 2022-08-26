"""
    42. Trapping Rain Water
    - leetCode
"""

height = list(map(int, input().split(',')))

left, right = 0, len(height)-1
maxLeft, maxRight = height[left], height[right]

res = 0
while (left < right):
    if maxLeft <= maxRight:
        left += 1
        maxLeft = max(maxLeft, height[left])
        res += maxLeft - height[left]
    
    else:
        right -= 1
        maxRight = max(maxRight, height[right])
        res += maxRight - height[right]
    
print(res)