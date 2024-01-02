string = input()
result = ''

for i in list(string):
    result += i.upper() if i.islower() else i.lower()

print(result)