n = int(input())

for i in range(n):
    scan = input().split()
    print(f'Case #{i + 1}: {" ".join(list(reversed(scan))).rstrip()}')