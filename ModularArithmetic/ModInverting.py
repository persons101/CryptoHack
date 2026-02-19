def extended_gcd(a: int, b: int) -> tuple:
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a: int, b: int) -> int:
    gcd, x, _ = extended_gcd(a, b)
    if gcd != 1:
        raise ValueError('Inverse does not exist')
    return x % b


print(mod_inverse(3, 13))