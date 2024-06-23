'''Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.


Example 1:

Input:
N = 4, K = 6
arr[] = {1, 5, 7, 1}
Output: 2
Explanation: 
arr[0] + arr[1] = 1 + 5 = 6 
and arr[1] + arr[3] = 5 + 1 = 6.

Example 2:

Input:
N = 4, K = 2
arr[] = {1, 1, 1, 1}
Output: 6
Explanation: 
Each 1 will produce sum 2 with any 1.

'''

def countPair(arr,k):
    d = {}
    count = 0 
    for i,num in enumerate(arr):
        if k - num in d:
            count += d[k-num]
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    return count 

arr = [1,5,7,1]
array = [1,1,1,1]
print(countPair(arr,6))
print(countPair(array,2))