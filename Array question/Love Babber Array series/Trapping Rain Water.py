'''Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 
 

Example 1:

Input:
N = 6
arr[] = {3,0,0,2,0,4}
Output:
10

Input:
N = 4
arr[] = {7,4,0,9}
Output:
10
Explanation:
Water trapped by above 
block of height 4 is 3 units and above 
block of height 0 is 7 units. So, the 
total unit of water trapped is 10 units.
'''

'''Approach:
left = 0 
right = n - 1
lmax = max(lmax,arr[left])
rmax = max(rmax,arr[right])
result += max(0,lmax-arr[left]) else  max(0,rmax-arr[right])
left    arr[left]   right    arr[right]     lmax=0     rmax=0           result 
0       7             3          9      max(0,7)=7    max(0,9)=9    if rmax<=lmax: result+=max(0,0-7)=0       
1       4             2          0      max(7,4)=7    max(9,0)=9    if rmax<=lmax: result+=max(0,7-4)=0+3
2       0             1          4      max(7,0)=7    max(9,4)=9    if rmax<=lmax: result+=max(0,7-0)=0+3+7  
3       9             0          7      max(7,9)=9    max(9,7)=9    if rmax<=lmax: result+=max(0,9-9)=0+3+7+0=10 
ans = 10 
'''

def TrapingRainWater(height):
    left = 0 
    right = len(height) - 1

    result = lmax = rmax = 0 
    while left <= right:
        if rmax <= lmax:
            result += max(0,rmax-height[right])
            rmax = max(rmax,height[right])
            right -= 1
        else:
            result += max(0,lmax-height[left])
            lmax = max(lmax,height[left])
            left += 1
    return result 

height = [7,4,0,9]
print(TrapingRainWater(height))


