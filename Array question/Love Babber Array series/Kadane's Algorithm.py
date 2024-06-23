'''Given an array arr[] of n integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

Examples:

Input: arr[] = {1,2,3,-2,5}, n = 5
Output: 9
Explanation: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.

approach:
i   arr[i]  curr_sum(curr_sum + arr[i])    max_sum
0   1               1                        1
1   2               3                        3
2   3               6                        6
3  -2               4                        6
4   5               9                        9

subarray = [1,2,3,-2,5]

'''

def maxSumSubarray(arr,n):
    curr_sum = 0 
    max_sum = float('-inf')
    for i in range(n):
        curr_sum += arr[i]

        if curr_sum > max_sum:
            max_sum = max(max_sum,curr_sum)

        if curr_sum < 0:
            curr_sum = 0 
    return max_sum

array = [1, 2, 3, -2, 5]
n = len(array)
print(maxSumSubarray(array,n))