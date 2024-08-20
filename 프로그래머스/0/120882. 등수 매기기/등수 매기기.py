def solution(score):
    l = len(score)
    score = list(sorted(map(lambda x: list(x), enumerate(map(lambda x: (x[0] + x[1]) / 2, score))), key=lambda x: x[1], reverse=True))
    print(score)
    ans = [(score[idx - 1] + [idx]) for idx in range(1, l)]
    ans.append(score[-1] + [l])
    for idx in range(l):
        print(ans[idx - 1], ans[idx])
        if idx == 0:
            continue
        if ans[idx - 1][1] == ans[idx][1] and ans[idx - 1][2] != ans[idx][2]:
            if ans[idx - 1][2] < ans[idx][2]:
                ans[idx][1:] = ans[idx - 1][1:]
            else:
                ans[idx - 1][1:] = ans[idx][1:]
    ans = list(map(lambda x: x[1:], sorted(ans, key=lambda x: x[0])))
    return list(map(lambda x: x[1], ans))