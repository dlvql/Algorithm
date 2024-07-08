import sys

n = int(input().rstrip())

nums = sys.stdin.readlines()
nums = list(map(lambda x: list(map(int, x.split())), nums))

while n > 1:
  n //= 2
  nums = list(map(lambda x: x[:n] + list(reversed(x[n:])), nums))
  arr = []
  for j in nums:
    l = []
    for i in range(n):
      l.append(j[i] + j[i + n])
    arr.append(l)
  nums = arr[:n] + list(reversed(arr[n:]))
  arr = []
  for i in range(n):
    l = []
    for j in range(n):
      l.append(nums[j][i] + nums[j + n][i])
    arr.append(l)
  nums = arr
print(nums[0][0])