'''Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

 

Example 1:

Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2
Example 2:

Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive. 
Example 3:

Input: nums = [1,-2,-3]
Output: 5
'''
'''Login
sum += nums[i] 
ans = min(ans,sum) 
index | nums[i] | sum | ans 
0       -3        -3    -3 
1        2        -1    -3
2       -3        -4    -4
3        4         0    -4   
4        2         2    -4
adding 1 beacuse if should be greater than one 
if sum >= 0 then retrun -ans + 1
if sum < 0 then we will return a value such that it never goes below 1. This will be equal to -S + 1 (because adding -S gives us minimum value we need to start from to ensure running sum always stays atleast 0. Adding 1 makes it never go below 1)
return -ans + 1
'''

def minStartValue(nums):
    sum, ans = 0, 0
    for el in nums:
        sum += el 
        ans = min(ans,sum)
    return -ans+1 

nums = [-3,2,-3, 4, 2]
print(minStartValue(nums))