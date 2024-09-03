def majority_element(nums):
    n = len(nums)
    d = {}
    for i in nums:
        d[i] = d.get(i,0)+1
    res = []
    for key in d.keys():
        if d[key] >= n//3:
            res.append(key)
    return res 
arr = [1,2]
print(majority_element(arr))