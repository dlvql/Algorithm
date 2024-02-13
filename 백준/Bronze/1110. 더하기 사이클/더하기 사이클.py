n = int(input())
num = n % 10 * 10 + (n // 10 + n % 10) % 10
count = 1

while num != n:
    fir = num // 10
    sec = num % 10
    num = sec * 10 + (fir + sec) % 10
    count += 1

print(count)