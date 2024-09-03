'''Given 2 sorted integer arrays Ar1 and Ar2 of size N each. Merge the given arrays and find the sum of the two middle elements of the merged array.

Example 1:

Input:
N = 5
Ar1[] = {1, 2, 4, 6, 10}
Ar2[] = {4, 5, 6, 9, 12}
Output: 11
Explanation: The merged array looks like {1,2,4,4,5,6,6,9,10,12}. Sum of middle elements is 11 (5 + 6).
'''

'''Approach:
count   i   j   a1[i]   a2[j]   condition                       m1=m2  m2=a1[i]/a2[j]
0       0   0     1      4    if a1[i] <= a2[j](1 <=4) i+= 1     -1       1              
1       1   0     2      4    if 2<=4: i+= 1                      1       4  
2       2   0     4      4    if 4<=4: i+= 1                      4       4
3       3   0     6      4    if 6<=4:[No] j += 1                 4       6
4       3   1     6      5    if 6<=5:[No] j+= 1                  6       5
                              if i == n: break                   (6   +     5) = 11 answer

'''
def findMidSum(a1,a2,n):
    m1 = m2 = - 1
    i = j = 0
    for count in range(n+1):
        if i == n:
            m1 = m2 
            m2 = a1[i]
            break 
        elif j == n:
            m1 = m2 
            m2 = a2[j]
            break 
        if a1[i] <= a2[j]:
            m1 = m2 
            m2 = a1[i]
            i += 1
        else:
            m1 = m2 
            m2 = a2[j]
            j += 1
    return m1+m2
N = 5
Ar1 = [1, 2, 4, 6, 10]
Ar2 = [4, 5, 6, 9, 12]
print(findMidSum(Ar1,Ar2,N))