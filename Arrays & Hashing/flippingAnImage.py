"""
  832. Flipping an Image
  -leetCode
"""
image = [[1,1,0],[1,0,1],[0,0,0]]


for i in image:
    for j in range(len(i)//2):
        temp = i[j] ^ 1
        i[j] = i[-j-1] ^ 1
        i[-j-1] = temp
print(image)
