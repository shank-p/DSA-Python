"""
    Angry Professor
    - Hackerrank
"""

def angryProfessor(arrivals, k):
    if len(arrivals) < k:
        return 'YES'
    count = 0
    for i in arrivals:
        if i > 0:
            count += 1
    if len(arrivals)-count >= k:
        return 'NO'
    return 'YES'

# number of. tets cases
T = int(input())
for _ in range(T):
    # students(n)   # threshold(k)
    n, k = map(int, input().split())
    arrivals = list(map(int, input().split()))
    result = angryProfessor(arrivals, k)
    print(result)
