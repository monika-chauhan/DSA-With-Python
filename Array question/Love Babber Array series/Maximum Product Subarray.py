'''Given an array arr[] that contains n integers (may be positive, negative or zero). Find the product of the maximum product subarray.

Examples

Input: arr[] = {6, -3, -10, 0, 2}, n = 5
Output: 180
Explanation:  The subarray [6, -3, -10] gives max product as 180.
'''

'''Approach:
i   arr[i]      pre *= arr[i]        suf *= arr[n-i-1]        max_product=max(max_product,max(pre,suf))
0    6              6                       2                    max('-inf',max(6,2) = 6   
1   -3             -18               if arr[i]==0: suff=1        max(6,max(-18,1)) = 6 
2   -10            180                      -10                  max(6,max(180,-10)) = 180
3    0      if arr[i]==0: pref=1             30                  max(180,max(1,30)) = 180 
4    2              2                       180                  max(180,max(2,180)) = 180
'''

def max_product_of_subarray(arr,n):
    max_product = float('-inf')
    pre = suf = 1 
    for i in range(n):
        pre *= arr[i]
        max_product = max(max_product, pre)
        if arr[i] == 0:
            pre = 1 
    for i in range(n-1,-1,-1):  
        suf *= arr[n-i-1]
        max_product = max(max_product,suf)
        if arr[n-i-1] == 0:
            suf = 1
      
    return max_product

arr = [6, -3, -10, 0, 2]
n = 5
print(max_product_of_subarray(arr,n))
