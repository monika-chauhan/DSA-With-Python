'''Given an array arr of n positive integers and a number k. One can apply a swap operation on the array any number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . Find the minimum number of swaps required to bring all the numbers less than or equal to k together, i.e. make them a contiguous subarray.

Example 1:

Input : 
arr[ ] = {2, 1, 5, 6, 3} 
K = 3
Output : 
1
Explanation:
To bring elements 2, 1, 3 together,
swap index 2 with 4 (0-based indexing),
i.e. element arr[2] = 5 with arr[4] = 3
such that final array will be- 
arr[] = {2, 1, 3, 6, 5}
'''

def minSwap(arr,n,k):
    good_number = 0 
    for i in arr:
        if i <= k:
            good_number += 1
    bad_number = 0 
    for i in range(good_number):
        if arr[i] > k:
            bad_number += 1

    i = 0 
    j = good_number
    ans = bad_number
    while i < n and j < n:
        if arr[i] > k:
            bad_number -= 1
        if arr[j] > k:
            bad_number += 1
        ans = min(ans,bad_number)
        i += 1
        j += 1
    return ans 

arr = [2, 1, 5, 6, 3]
n = len(arr) 
k = 3 
print(minSwap(arr,n,k))