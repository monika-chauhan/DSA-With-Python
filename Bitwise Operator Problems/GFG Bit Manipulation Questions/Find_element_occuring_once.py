'''Find element occuring once when all other are present thrice'''
def findElementOnce(arr,N):
    ones = 0 
    twos = 0 
    for i in range(N):
        twos = twos ^ (ones & arr[i])
        ones = ones ^ arr[i] 
        common_mask = ~(ones & twos)
        ones = ones & common_mask
        twos = twos & common_mask
    return ones 

arr = [1, 10, 1, 1]
N = len(arr)
print(findElementOnce(arr,N))