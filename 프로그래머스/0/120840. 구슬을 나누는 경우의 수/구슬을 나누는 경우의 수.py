def factorial(n):
    if(n == 0):
        return 1
    return factorial(n - 1) * n

def solution(balls, share):
    return factorial(balls) // (factorial(balls - share) * factorial(share))