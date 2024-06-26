'''Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
'''

'''Approach:
start   end    nums[end]   curr_sum+=nums[end]    curr_sum-= nums[start]    length=(end-start+1)   min_length=min(min_length,legth)
0       0       2           2                        2                         0                       0
        1       3           5                        5                         0                       0
1       2       1           6                        6                         0                       0
2       3       2           8/6                     8-nums[0]=6                0                       0
3       4       4           10/7                   (10-3=7==target)         (4-2+1)=3                  3              
4       5       3           10                     10-1=9
                                                  (9-2=7==target)          (5-4+1)=2                   2 = output    
'''

def minSubArrayLen(nums,target):
    start = end = 0 
    min_length = float('inf')
    length = 0
    curr_sum = 0
    while end < len(nums):
        curr_sum += nums[end]
    
        while curr_sum >= target:
            length = end - start + 1
            min_length = min(min_length,length)
            curr_sum -= nums[start]
            start += 1
        end += 1
    
    return 0 if min_length == float('inf') else min_length 

nums = [2,3,1,2,4,3]
target = 7 
print(minSubArrayLen(nums,target))