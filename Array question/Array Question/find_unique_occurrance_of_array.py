def findUniqueOccuranceElement(array):
    hashMap = {}
    for i in array:
        if i not in hashMap:hashMap[i] = 1 
        else:hashMap[i] += 1 
    res = []
    for key in hashMap.keys():
        res.append(hashMap[key])
    return len(set(res)) == len(res)

array = [2,2,3,1,1]
print(findUniqueOccuranceElement(array))