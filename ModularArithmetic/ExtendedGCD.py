import Mathematics


a = 26513
b = 32321
z, x, y = Mathematics.extended_gcd(a, b)

print(f"({a})*({x}) + ({b})*({y}) = gcd({a},{b}) = {z}")
print(f"{x if x < y else y}")