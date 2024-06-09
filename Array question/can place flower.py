'''You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
'''

'''Logic :-> We are updating the original array itself counting the place flower by 1 
we will be checking the two side of the current index that is
if index == 0 or flower[index - 1] and 
index == len(flowersbed) - 1 - or flower[index + 1]
if both conditon True then We can place the flower 
index  | nums[index] | checking condition
0        1              if flower[index] == 0 [No]
1        0              if flower[index] == 0 [Yes] then check if (index == 0 or flower[index-1] == 0) == False and  (index == len(flower) - 1 or flower[index+1] == 0) == True then False and True=> False 
3        0              if flower[index] == 0 [Yes] then check if (index == 0 or flower[index-1] == 0) == True and  (index == len(flower) - 1 or flower[index+1] == 0) == True then flower[index] = 1, count+= 1 
4        0              if flower[index] == 0 [Yes] then check if (index == 0 or flower[index-1] == 0) == False and  (index == len(flower) - 1 or flower[index+1] == 0) == True  
5        1              if flower[index] == 0 [Yes] then check if (index == 0 or flower[index-1] == 0) == True and  (index == len(flower) - 1 or flower[index+1] == 0) == False  
count >= n [1 >= 1] {Yes}
'''

def canPlaceFlowers(flowerbed,n):
    lenF = len(flowerbed)
    count = 0 
    for i in range(lenF):
        if flowerbed[i] == 0:
            empty_left = (i == 0) or (flowerbed[i-1] == 0)
            empty_right = (i == lenF -1) or (flowerbed[i+1] == 0)

            if empty_left and empty_right:
                flowerbed[i] = 1 
                count += 1
    return count >= n 

nums = [1,0,0,0,1]
print(canPlaceFlowers(nums, 1))
print(canPlaceFlowers(nums, 2))
