class Solution(object):
    def scoreOfString(self, s):
        o = 0
        for i in range(len(s) - 1):
            o += abs(ord(s[i]) - ord(s[i + 1]))
        return o