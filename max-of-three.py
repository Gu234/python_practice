def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= c and b >= a:
        return b
    if c >= a and c >= b:
        return c
