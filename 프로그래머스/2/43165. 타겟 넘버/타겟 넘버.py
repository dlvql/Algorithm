def solution(numbers, target):
    global c # 반환하는 count값
    c = 0
    def dfs(idx, v): # 재귀 함수를 이용해 DFS를 구현 - idx: Depth / v: 현재 값 (value)
        if(idx == len(numbers)): # 재귀 탈출 조건은 Depth가 numbers 배열의 길이와 같을 때
            global c
            c += 1 if v == target else 0
            return v
        dfs(idx + 1, v + numbers[idx]) # + / - 연산을 한 번씩 돌 수 있도록 작성
        dfs(idx + 1, v - numbers[idx])
        return v
    dfs(0, 0) # 재귀의 시작은 0번 인덱스 / 현재 값 0
    return c # 최종적으로 count를 반환함