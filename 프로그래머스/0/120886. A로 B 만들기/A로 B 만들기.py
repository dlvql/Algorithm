def solution(before, after):
    after = list(after)
    ans = 1
    for i in before:
        if i in after:
            after.remove(i)
        else:
            ans = 0
            break
    return ans