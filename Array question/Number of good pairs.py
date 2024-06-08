'''Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0'''

'''Logic -> create a mapp to store the occurrence of number 
1) mapp = {1:} if not in mapp
2) 1 is in mapp then count += mapp[1] = > 1 and mapp[1] = 2
3) 1 is in mapp then count += mapp[1] => 1 + 2 = 3and mapp[1] = 3
4) 1 is in mapp then count += map[1] => 3 + 3 = 6 and mapp[1] = 4'''



def goodPairs(nums):
    mapp = {}
    count = 0 
    for i in nums:
        if i in mapp:
            count  += mapp[i]
            mapp[i] += 1
        else:
            mapp[i] = 1
    return count 

nums = [1,1,1,1]
print(goodPairs(nums))