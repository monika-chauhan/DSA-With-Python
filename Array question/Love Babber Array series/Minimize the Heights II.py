'''Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.
Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output:
5
Explanation:
The array can be modified as 
{1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}. 
The difference between 
the largest and the smallest is 8-3 = 5.
Example 2:
'''

'''Approach:
i      h[i]       small         large          ans/min(ans,maxi-mini)   mini/min(small,h[i+1]-k)   maxi/max(large,h[i]+k) 
0       1       (1+k)=(1+2)= 3 (10-k)=(10-2)=8  large-small=8-3=5                                   
1       5                                       min(5,8-3)=5             min(3,5-2)=3             max(8,1+2)=8     
1       8                                       min(5,10-3)=5            min(3,8-2)=3             max(8,8+2)=10
2       10                                      min(5,8-3)=5             min(3,10-2)=3            max(8,10-2)=8

'''

def get_min_diff(heights,n, k):
    heights.sort()
    small = heights[0] + k
    large = heights[n-1] - k
    ans = large - small 

    for i in range(n-1):
        mini = min(small,heights[i+1] - k)
        maxi = max(large,heights[i] + k)
        if mini < 0:
            continue
        ans = min(ans,maxi - mini)
    return ans 

height = [1, 5, 8, 10]
k = 2
n = len(height)
print(get_min_diff(height,n,k)) 