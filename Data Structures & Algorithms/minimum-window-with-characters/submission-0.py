class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not s or not t:
            return ""

        t_freq = {}
        for c in t:
            t_freq[c] = t_freq.get(c, 0) +1

        l, r = 0, 0
        req = len(t_freq)
        formed = 0
        min_win = float('inf')
        min_left, min_right = 0, 0
        s_freq = {}

        while r < len(s):
            char = s[r]
            s_freq[char] = s_freq.get(char, 0) + 1

            if char in t_freq and t_freq[char] == s_freq[char]:
                formed += 1

            while l <= r and formed == req:
                char = s[l]
                if (r-l +1) < min_win:
                    min_win = r-l +1
                    min_left, min_right = l, r

                s_freq[char] -= 1 
                if char in t_freq and s_freq[char] < t_freq[char]:
                    formed -= 1

                l += 1
            r += 1
        
        return "" if min_win == float('inf') else s[min_left:min_right +1]
