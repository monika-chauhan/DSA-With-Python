'''Given a matrix of size r*c. Traverse the matrix in spiral form.

Example 1:

Input:
r = 4, c = 4
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12},
           {13, 14, 15,16}}
Output: 
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
'''

def spirallyTraverse(matrix,r,c):
    left = top = 0 
    right = c - 1
    bottom = r - 1 
    res = []
    while left <= right and top <= bottom:
        for x in range(left,right+1):
            res.append(matrix[top][x])
        top += 1

        for y in range(top,bottom+1):
            res.append(matrix[y][right])
        right -= 1

        if top <= bottom:
            for x in range(right,left-1,-1):
                res.append(matrix[bottom][x])
        bottom -= 1
        if left <= right:
            for y in range(bottom,top-1,-1):
                res.append(matrix[y][left])
        left += 1
    return res 


r = 3 
c = 4 
matrix = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]
print(spirallyTraverse(matrix,r,c))