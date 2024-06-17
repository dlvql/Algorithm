def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    r, n, d = numer % denom, numer, denom
    print(r, n, d)
    while r != 0 :
        n, d = d, r
        r = n % d
        print(numer, denom, r)
    return [numer // d, denom // d]