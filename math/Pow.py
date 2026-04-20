def myPow(base: float, power: int) -> float:
    if power == 0:
        return 1

    # base**(-n) = 1 / base ** n
    if power < 0:
        return myPow(1 / base, -power)

    # base**n = base * base**(n-1) <- if n is odd, take 1 base out and make n even
    if power % 2 == 1:
        return base * myPow(base, power - 1)
    else: # base**n = (base**2)**(n/2) <- repeatedly square result, halving amount of operations
        # instead of 2 * 2 * 2 * 2 (3 ops)
        # 2^4 = (2^2)^2 = 4^2 = 16 (2 ops)
        return myPow(base * base, power // 2)

base, power = map(float, input().split())
print(myPow(base, int(power)))
