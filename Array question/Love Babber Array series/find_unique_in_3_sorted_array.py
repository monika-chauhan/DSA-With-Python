'''Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?

Example 1:

Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function commonElements() which take the 3 arrays A[], B[], C[] and their respective sizes n1, n2 and n3 as inputs and returns an array containing the common element present in all the 3 arrays in sorted order. 
If there are no such elements return an empty array. In this case the output will be printed as -1.

 

Expected Time Complexity: O(n1 + n2 + n3)
Expected Auxiliary Space: O(n1 + n2 + n3)

'''

def commonElements(A,B,C,n1,n2,n3):
    res = []
    i = j = k = 0 
    last = -123456789
    while i < n1 and j < n2 and k < n3:
        if A[i] == B[j] == C[k]:
            if last != A[i]:
                res.append(A[i])
                last = A[i]
            i += 1
            j += 1
            k += 1
        elif min(A[i],B[j],C[k]) == A[i]:
            i += 1
        elif min(A[i],B[j],C[k]) == B[j]:
            j += 1
        else:
            k += 1
    return res 
n1 = 6
A = [1, 5, 10, 20, 40, 80]
n2 = 5
B = [6, 7, 20, 80, 100]
n3 = 8
C = [3, 4, 15, 20, 30, 70, 80, 120]
print(commonElements(A,B,C,n1,n2,n3))