def ValueEqualToIndex(arr):
    ans = [] 
    for i in range(len(arr)):
        if arr[i] == i + 1:
            ans.append(arr[i])
    return ans 

arr = [4,2,6,4,5]
print(ValueEqualToIndex(arr))