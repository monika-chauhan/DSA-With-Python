'''Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
'''

'''Logic :-> we have to create the temp array and store the nums[i] value at nums[i] index in count so that We fill the value 
and then check if count having 0 value at some index and we store those index value in result array '''

def findDisappearedNumbers(nums):
    n = len(nums)
    count = [0] * (n+1)
    for i in range(n):
        count[nums[i]] = nums[i] 
    res = []
    for i in range(1, len(count)):
        if count[i] == 0:
            res.append(i)
    return res 

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))