def solution(numLog):
    # 해시 테이블을 이용, 키에 차이 / 값에 w|a|s|d 넣어두기
    wasd = {
        1: 'w',
        -1: 's',
        10: 'd',
        -10: 'a'
    }
    ans = ""
    for i in range(len(numLog) - 1):
        dif = wasd[numLog[i + 1] - numLog[i]]
        ans += dif
    return ans
        