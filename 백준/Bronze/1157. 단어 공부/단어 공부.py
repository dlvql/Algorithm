arr = input().upper()
category = list(set(arr))
count = []
for i in range(len(category)):
    count.append(arr.count(category[i]))
maxCount = max(count)
if(count.count(maxCount) > 1):
    print('?')
else:
    print(category[count.index(maxCount)])