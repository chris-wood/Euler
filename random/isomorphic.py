class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        chars1 = {}
        for c in s:
            if c not in chars1:
                chars1[c] = 1
            else:
                chars1[c] = chars1[c] + 1

        chars2 = {}
        for c in t:
            if c not in chars2:
                chars2[c] = 1
            else:
                chars2[c] = chars2[c] + 1

        for i in range(len(s)):
            if chars1[s[i]] != chars2[t[i]]:
                return False
        return True

        if sorted(chars1.values()) == sorted(chars2.values()):
            return True # keys don't matter -- all that matters is the count
        return False

s = Solution()
print s.isIsomorphic("aba", "baa")
