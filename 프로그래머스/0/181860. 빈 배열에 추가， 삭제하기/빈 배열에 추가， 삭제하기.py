def solution(arr, flag):
    ans = []
    for idx, val in enumerate(flag):
        if(val):
            ans += [arr[idx]] * (arr[idx] * 2)
        else:
            ans = ans[:len(ans) - arr[idx]]
    return ans