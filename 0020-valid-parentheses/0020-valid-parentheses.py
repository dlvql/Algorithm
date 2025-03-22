class Solution(object):
    def isValid(self, s):
        arr = [s[0]]
        result = True
        for c in s[1:]:
            if c in [")", "]", "}"]:
                if len(arr) <= 0:
                    result = False
                    break
                elif (c == ")" and arr[-1] == "(") or (c == "]" and arr[-1] == "[") or (c == "}" and arr[-1] == "{"):
                    arr.pop(-1)
                else:
                    result = False
                    break
            else:
                arr.append(c)
        if len(arr) != 0:
            result = False
        return result