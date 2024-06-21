'''Given a string s of length n, find all the possible non-empty subsequences of the string s in lexicographically-sorted order.

Example 1:

Input : 
s = "abc"
Output: 
a ab abc ac b bc c
Explanation : 
There are a total 7 number of subsequences possible for the given string,
and they are mentioned above in lexicographically sorted order.'''

def power_set(s):
    res = []
    n = len(s)
    for i in range(1 << n):
        temp = ''
        for j in range(n):
            if i & ( 1 << j) == 0:
                temp += s[j]
        if temp:
            res.append(temp)
    return res 

print(power_set('abc'))

