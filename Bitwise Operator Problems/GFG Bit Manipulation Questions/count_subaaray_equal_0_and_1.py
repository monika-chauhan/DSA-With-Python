'''Count subarrays with equal number of 1’s and 0’s using Map:'''

def Countsubbary1and0(arr):
    mp = dict()
    sum = 0 
    count = 0 
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1 
        sum += arr[i]
    
        if sum == 0:
            count += 1
        
        if sum in mp.keys():
            count += mp[sum]
        
        mp[sum] = mp.get(sum,0)+1
    return count 

print(Countsubbary1and0([1,0,0,1,0,1,1]))
        