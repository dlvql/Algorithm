class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        for k in range(len(s) - 1):
            nxt = s[k + 1]
            v = s[k]
            if v == 'I':
                if nxt == 'V' or nxt == 'X':
                    ans -= 1
                else :
                    ans += 1
            elif v == 'V':
                ans += 5
            elif v == 'X':
                if nxt == 'L' or nxt == 'C' :
                    ans -= 10
                else:
                    ans += 10
            elif v == 'L':
                ans += 50
            elif v == 'C':
                if nxt == 'D' or nxt == 'M':
                    ans -= 100
                else:
                    ans += 100
            elif v == 'D':
                ans += 500
            else:
                ans += 1000
        ans += 1 if s[-1] == 'I' else (5 if s[-1] == 'V' else (10 if s[-1] == 'X' else (50 if s[-1] == 'L' else (100 if s[-1] == 'C' else (500 if s[-1] == 'D' else 1000)))))
        return ans