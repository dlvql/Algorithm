a = int(input(), 2)
b = int(input(), 2)

l = 100000

ans = [a & b, a | b, a ^ b, ~a, ~b]

print(bin(a&b)[2:].zfill(l))
print(bin(a|b)[2:].zfill(l))
print(bin(a^b)[2:].zfill(l))
print(bin(a^(2**l-1))[2:].zfill(l))
print(bin(b^(2**l-1))[2:].zfill(l))