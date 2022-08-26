"""
    Search an element in an infinite sorted array
    - GFG
"""

nums = list(map(int, input().split()))
target = int(input())

start = 0
end = 1
range = 1
while (target > nums[end]):
    range += range
    start = end + 1
    end = start + range

def binarySearch(start, end, target):
    pass
