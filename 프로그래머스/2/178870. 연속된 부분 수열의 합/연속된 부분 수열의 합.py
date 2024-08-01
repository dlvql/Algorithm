# def solution(seq, k):
#     sp, fp = [0, 1]
#     l = len(seq)
#     s = seq[0]
#     ans = [0, l]
#     while fp <= l and sp < l:
#         if s > k:
#             s -= seq[sp]
#             sp += 1
#         elif s <= k:
#             if s == k and ans[1] - ans[0] > fp - 1 - sp:
#                 ans = [sp, fp - 1]
#             s += seq[fp]
#             fp += 1
#     for i in range(l):
#         if sum(seq[i:]) == k and ans[1] - ans[0] > l - 1 - i:
#             ans = [i, l - 1]
#     return ans

def solution(seq, k):
    sp, fp = 0, 0  # 시작 포인터와 끝 포인터 초기화
    l = len(seq)
    s = 0
    ans = [-1, -1]  # 초기 값을 -1로 설정하여 결과가 없을 경우를 처리

    while fp < l:
        s += seq[fp]
        while s > k and sp <= fp:
            s -= seq[sp]
            sp += 1
        if s == k:
            if ans == [-1, -1] or fp - sp < ans[1] - ans[0]:
                ans = [sp, fp]
        fp += 1

    return ans
