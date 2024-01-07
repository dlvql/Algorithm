a, b = map(lambda x: int("".join(reversed(list(x)))), input().split())

print(a if a > b else b)