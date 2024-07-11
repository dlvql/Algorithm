n, m = map(int, input().split())
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

dif = a.difference(b)
print(len(dif))
print(" ".join(list(map(str, list(sorted(dif))))))