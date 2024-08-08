def solution(s):
    s = list(map(ord, s))
    s.sort(reverse=True)
    return("".join(list(map(chr, s))))