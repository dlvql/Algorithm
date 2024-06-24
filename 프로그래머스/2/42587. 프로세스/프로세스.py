from collections import deque

def solution(priorities, location):
    ans = 0 # 반환값
    arr = deque([0 for _ in range(len(priorities))]) # 종료 조건 판단용 덱 생성
    arr[location] = 1 # 기본 설정 : 타겟 위치의 원소가 1
    queue = deque(priorities) # 주어진 배열을 그대로 덱으로 생성
    while True:
        if(not arr or max(arr) == 0): # 종료조건
            break
        if(max(queue) == queue[0]): # 배열의 최댓값이 최우선순위(첫 번째 자리)에 있는 경우
            queue.popleft() # 배열에서 삭제
            arr.popleft()
            ans += 1 # 동작 횟수 올림
        else: # 아닌 경우
            queue.append(queue.popleft()) # 첫 번째 자릿값을 맨 뒤로 이동
            arr.append(arr.popleft())
    return ans