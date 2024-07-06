'''Given an integer array of N elements. You need to find the maximum sum of two elements such that sum is closest to zero.

Example 1:

Input:
N = 3
arr[] = {-8 -66 -60}
Output: -68
Explanation: Sum of two elements closest to 
zero is -68 using numbers -60 and -8.
'''

def closestToZero(nums,n):
    i = 0 
    j = n - 1
    diff = nums[i] + nums[j]
    sum = nums[i] + nums[j] 
    while i < j:
        if nums[i] + nums[j] == 0:
            return 0 
        if abs(nums[i]+nums[j]) < abs(diff):
            diff = nums[i]+nums[j]
            sum = nums[i] + nums[j] 
        elif abs(nums[i]+nums[j]) == abs(diff):
            sum = max(sum,nums[i]+nums[j])
        if nums[i] + nums[j] > 0:
            j -= 1
        else:
            i += 1
    return sum 

nums = [-8,-66,-60]
n = len(nums)
print(closestToZero(nums, n))
        
