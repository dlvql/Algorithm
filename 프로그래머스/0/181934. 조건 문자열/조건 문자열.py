def solution(ineq, eq, n, m):
    isTrue = 10
    if(ineq == ">"):
        isTrue = 1 if eq == "!" and n > m else (1 if n >= m else 0)
    else:
        isTrue = 1 if eq == "!" and n < m else (1 if n <= m else 0)
    return isTrue