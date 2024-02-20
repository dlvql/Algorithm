import math
d, h, w = map(int, input().split())

imsi = math.pow(d, 2) / (h ** 2 + w ** 2)
rh = int(math.sqrt(imsi * (h ** 2)))
rw = int(math.sqrt(imsi * (w ** 2)))

print(rh, rw)