"""
    Apple and Orange
    - Hackerrank
"""

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0
    for i in apples:
        if i+a>=s and i+a<=t:
            apple_count += 1
    for i in oranges:
        if b+i>=s and b+i<=t:
            orange_count += 1
    
    print(apple_count)
    print(orange_count)


#input in multiple lines
house_coord = input().strip().split()
s = int(house_coord[0])
t = int(house_coord[1])

tree_coord = input().strip().split()
a = int(tree_coord[0])
b = int(tree_coord[1])

no_of_fruits = input().strip().split()
m = int(no_of_fruits[0])
n = int(no_of_fruits[1])

apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)



