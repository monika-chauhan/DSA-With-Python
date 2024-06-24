'''Given an array of integers. Find the Inversion Count in the array.  Two array elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 

Examples:

Input: n = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
Input: n = 5, arr[] = {2, 3, 4, 5, 6}
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count.
Input: n = 3, arr[] = {10, 10, 10}
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.
'''

"""Approach: arr = [2, 4, 1, 3, 5]
merge(arr): => mid = len(arr)/2
                        [2,4,1,3,5]
                          mid = 2
                         /      |
                        /       |     while i < len(L) and j < len(R):
                  L = [2,4]    R = [1,3,5]  i,k,j=0 if L[i]<=R[j] => continue arr[k] = L[i], i += 1, k+=1 else: 2<=1[No] count += len(L)-i=>2-0=2,arr[0] = 1 j=1,k=1
                        mid=1        mid=1   else: count += len(L) - i arr[k] = R[j], j+=1, k+= 1  
                        / |          /  | if L[0]<=R[0]=> 2<=1[No] count += 2-0 = 2 arr[0] = [1,....] j=1, k=1
                       /  |         /   | if L[0]<=R[1]=> 2<=3[Yes] arr[1] = [1,2,....] i=1, k = 2  
                      /   |        /    | if L[1]<=R[1]=> 4<=3[No] count += 2-1 =2+1=3 , arr[2] = [1,2,3,...] j=2,k=3
                     /    |      /      |  if L[1]<=R[2]=> 4<=5[Yes] arr[3] = [1,2,3,4,..] i = 2, k= 4 loop break if array element remaining in R than while j <len(R): arr[k] = R[j], j+=1, k+= 1 
                    /     |     /       |   if array element remaining in L than while i <len(L): arr[k] = R[i], i+=1, k+= 1
compare(L[i],R[j]) [2]   [3]  L=[1]  R = [3,5] = [3,5] Compare L[i] <= R[j] 1<=3 and 3 <=5 contine[No inversion Count]
                                            /   |
                                         L=[3] R=[5] compare L[i] <= R[j] continue  

"""


def inversionCount(arr):
    count = merge(arr)
    return count

def merge(arr):
    count = 0 
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        
        
        count += merge(L)
        count += merge(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
                k += 1
            else:
                count += len(L) - i 
                arr[k] = R[j]
                j += 1
                k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1 
            k += 1
    return count

arr = [2,4,1,3,5]
print(inversionCount(arr))