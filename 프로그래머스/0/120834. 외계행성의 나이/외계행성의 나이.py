def solution(age):
    return "".join(list(map(lambda x: chr(x + 97), map(int, list(str(age))))))