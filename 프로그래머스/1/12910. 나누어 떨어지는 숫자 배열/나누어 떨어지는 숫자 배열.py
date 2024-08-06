def solution(arr, divisor):
    ans = list(sorted(filter(lambda x: x % divisor == 0, arr)))
    return ans if ans else [-1]