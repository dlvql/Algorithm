def solution(abss, signs):
    for i in range(len(abss)):
        abss[i] = int(f"{'' if signs[i] == True else '-'}{abss[i]}")
    return sum(abss)