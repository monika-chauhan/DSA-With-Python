def Linear_search(array,target):
    for i in range(len(array)):
        if array[i] == target:
            return i 
    return -1 

array = [3,2,4,6,7,2,1]
target = 12
print(Linear_search(array,target))