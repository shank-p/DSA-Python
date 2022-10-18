"""
    Flatland_Space_Station
    - HR
"""

n, m = map(int, input().split())
c = list(map(int, input().split()))

def flatlandSpaceStations(n, c):
  c.sort()
  maxd = max(c[0], n-1 - c[-1])
  for i in range(len(c)-1):
    maxd = max((c[i+1]-c[i])//2, maxd)
  return maxd
print(flatlandSpaceStations(n, c))