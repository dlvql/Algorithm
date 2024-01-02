import sys
result = ''
try:
    while True:
        result += input() + '\n'
except Exception:
    print(result.rstrip())