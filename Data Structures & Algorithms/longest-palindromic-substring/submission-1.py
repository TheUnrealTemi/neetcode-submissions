class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def palindrom(s, l, r):
            result = ""
            resLen = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l+1) > resLen:
                    result = s[l:r+1]
                    resLen = r - l +1
                l -= 1
                r += 1
            return result

        for i in range(len(s)):
            odd = palindrom(s, i, i)
            even = palindrom(s, i, i+1)

            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        
        return res