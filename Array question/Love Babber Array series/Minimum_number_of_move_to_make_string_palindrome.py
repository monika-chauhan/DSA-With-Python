'''You are given a string s consisting only of lowercase English letters.

In one move, you can select any two adjacent characters of s and swap them.

Return the minimum number of moves needed to make s a palindrome.

Note that the input will be generated such that s can always be converted to a palindrome.

 

Example 1:

Input: s = "aabb"
Output: 2
Explanation:
We can obtain two palindromes from s, "abba" and "baab". 
- We can obtain "abba" from s in 2 moves: "aabb" -> "abab" -> "abba".
- We can obtain "baab" from s in 2 moves: "aabb" -> "abab" -> "baab".
Thus, the minimum number of moves needed to make s a palindrome is 2.
'''

def minMovesToMakePalindrome(s):
    s = list(s)
    res = 0 
    while s:
        i = s.index(s[-1])
        if i == len(s) -1:
            res += i / 2
        else:
            res += i 
            s.pop(i)
        s.pop()
    return res 

s = 'aabb'
print(minMovesToMakePalindrome(s))