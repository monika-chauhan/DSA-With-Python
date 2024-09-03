'''Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order without using any extra space. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.

Example 1:

Input: 
n = 4, arr1[] = [1 3 5 7] 
m = 5, arr2[] = [0 2 6 8 9]
Output: 
arr1[] = [0 1 2 3]
arr2[] = [5 6 7 8 9]
Explanation:
After merging the two 
non-decreasing arrays, we get, 
0 1 2 3 5 6 7 8 9.
'''

def merge(arr1,arr2,n,m):
    i = n - 1
    j = 0 
    while i >= 0 and j < m:
        if arr1[i] >= arr2[j]:
            arr1[i],arr2[j] = arr2[j],arr1[i]
            i -= 1
            j += 1
        else:
            break 
    arr1.sort()
    arr2.sort()
    print(arr1+arr2)

n = 4
arr1 = [1, 3, 5, 7] 
m = 5
arr2 = [0, 2, 6, 8, 9]
merge(arr1,arr2,n,m)