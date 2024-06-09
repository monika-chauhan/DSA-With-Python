'''Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
'''

'''Logic-> 
Iteration the array and checking if arr[i] == 1 then count += 1 amd also keep tracking max_one = max(max_one,count)
if 0 occurred then count become 0 and'''

def findMaxConsecutiveOnes(nums):
    count = 0 
    max_one = 0 
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            max_one = max(max_one,count)
        else:
            count = 0 
    return max_one 

nums = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))