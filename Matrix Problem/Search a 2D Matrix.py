'''You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
'''

def searchMatrix(matrix,target):
    left = 0 
    right = len(matrix[0]) - 1

    while left < len(matrix) and right >= 0:
    
        if matrix[left][right] == target:
            return True 
        elif matrix[left][right] < target:
            left += 1
        else:
            right -= 1
    return False 

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix,target))