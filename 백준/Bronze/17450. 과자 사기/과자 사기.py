s = list(map(int, input().split()))
n = list(map(int, input().split()))
u = list(map(int, input().split()))

sp = s[0] * 10
np = n[0] * 10
up = u[0] * 10

sp = sp if sp < 5000 else sp - 500
np = np if np < 5000 else np - 500
up = up if up < 5000 else up - 500

arr = [s[1] / sp, n[1] / np, u[1] / up]


print(['S', 'N', 'U'][arr.index(max(arr))])