def solution(food):
    answer = ''
    rev_ans = ''
    for i in range(1, len(food)):
        food[i] -= food[i] % 2
        for j in range(food[i] // 2):
            answer += str(i)
    answer += '0'
    for i in answer[::-1]:
        rev_ans += i
    return answer + rev_ans[1:]