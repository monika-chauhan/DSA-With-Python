'''Given an array of integers. Find if there is a subarray (of size at-least one) with 0 sum. You just need to return true/false depending upon whether there is a subarray present with 0-sum or not. Printing will be taken care by the driver code.

Example 1:

Input:
n = 5
arr = {4,2,-3,1,6}
Output: 
Yes
Explanation: 
2, -3, 1 is the subarray with sum 0.
'''

'''Approach: arr = [4,2,-3,1,6]
i       arr[i]      sum+=arr[i]         sum_map={sum:0}         subarray
0        4              4                  {4:1}                [4] 
1        2              6                 {4:1,6:1}             [4,2]
2       -3              3               {4:1,6:1,7:1}           [4,2,-3] 
3        1              4             4 in {4:1,6:1,7:1,8:1}        [4,2,-3,1] Return True
4        6              10        
'''

def subarraySum0(arr):
    sum_map = {}
    curr_sum = 0 
    for i in range(len(arr)):
        curr_sum+=arr[i]
        print(curr_sum)
        if curr_sum == 0 or curr_sum in sum_map:
            return True 
        sum_map[curr_sum] = 1
    return False

arr = [4,2,-3,1,6]
print(subarraySum0(arr))