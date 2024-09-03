'''Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m, where both arrays may contain duplicate elements. The task is to determine whether array a2 is a subset of array a1. It's important to note that both arrays can be sorted or unsorted. Additionally, each occurrence of a duplicate element within an array is considered as a separate element of the set.

Example 1:

Input:
a1[] = {11, 7, 1, 13, 21, 3, 7, 3}
a2[] = {11, 3, 7, 1, 7}
Output:
Yes
Explanation:
a2[] is a subset of a1[]
'''

def isSubset(a1,a2,n,m):
    d2 = {}
    for i in a2:
        d2[i] = d2.get(i,0) + 1 
    
    for i in range(n):
        if a1[i] in d2:
            d2[a1[i]] -= 1
            if d2[a1[i]] == 0:
                del d2[a1[i]]
    
    if d2 == {}:
        return 'Yes'
    else:
        return 'No'

a1 = [1, 2, 3, 4, 4, 5, 6]
a2 = [1, 2, 4]
n = len(a1) 
m = len(a2)
print(isSubset(a1,a2,n,m))