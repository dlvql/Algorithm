def solution(friends, gifts):
    friend = {}
    f_gift = {}
    for f in friends:
        friend[f] = {}
        f_gift[f] = 0
        for f1 in friends:
            friend[f][f1] = 0
    for g in gifts:
        a, b = g.split()
        friend[a][b] += 1
    met = []
    for a in friends:
        for b in friends:
            if a == b or (f"{a} {b}" in met) or (f"{b} {a}" in met):
                break
            if friend[a][b] > friend[b][a]:
                f_gift[a] += 1
            elif friend[b][a] > friend[a][b]:
                f_gift[b] += 1
            else:
                gave_a = sum(friend[a].values())
                gave_b = sum(friend[b].values())
                get_a, get_b = [0, 0]
                for f in friend.values():
                    get_a += f[a]
                    get_b += f[b]
                if (gave_a - get_a) > (gave_b - get_b):
                    f_gift[a] += 1
                elif (gave_a - get_a) < (gave_b - get_b):
                    f_gift[b] += 1
            met.append(f"{a} {b}")
    return max(f_gift.values())