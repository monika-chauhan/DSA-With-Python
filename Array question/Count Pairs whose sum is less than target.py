'''Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
 

Example 1:

Input: nums = [-1,1,2,3,1], target = 2
Output: 3
Explanation: There are 3 pairs of indices that satisfy the conditions in the statement:
- (0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target
- (0, 2) since 0 < 2 and nums[0] + nums[2] = 1 < target 
- (0, 4) since 0 < 4 and nums[0] + nums[4] = 0 < target
Note that (0, 3) is not counted since nums[0] + nums[3] is not strictly less than the target.
'''

'''Logic :-> 
First Sort the array 
Using two pointers left = 0 and right = len(nums) - 1
check with first and last elements to add and comapre with target 
1. If nums[left] + nums[right] < target: count += right - left; left += 1 
2. else: right -= 1
nums = [-1,1,2,3,1]
sort => [-1,1,1,2,3]
l = 0 r = len(nums) - 1 = 4
l  |   r  =  sum 
0      4  =  -1+3 = 2 < 2 [NO]-> r -= 1
0      3  =  -1+2 = 1 < 2 [Yes] -> count += r - l=> 3 - 0 = 3 l += 1
1      3  =  1+2  = 3 < 2 [No] -> r -= 1=> 2 
1      2  =  1 + 1 = 2 < 2 [No] -> r -= 1=> 1 
1      1  =  1+1 = 2< 2 [No] r -= 1 -> 0 
break return count => 3  
'''

def countPairs(nums,target):
    count = 0
    nums.sort() 
    left = 0 
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] < target:
            count += right - left 
            left += 1
        else:
            right -= 1
    return count  

nums = [-1,1,2,3,1]
target = 2 
print(countPairs(nums, target))