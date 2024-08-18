def solution(chicken):
    ans = chicken
    while chicken > 9:
        chicken /= 10
        ans += chicken
    return ans // 10