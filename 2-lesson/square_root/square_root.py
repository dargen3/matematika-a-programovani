def n_power(n, root):
    power = 1
    for x in range(root):
        power *= n
    return power

def root_binary(n, root):
    error = 0.00000001
    a = 0
    b = n
    c = (a + b) / 2
    p = n_power(c, root)
    while abs(p - n) > error:
        if p > n:
            b = c
        else:
            a = c
        c = (a + b) / 2
        p = n_power(c, root)
    return c

def power(n, a, b):
    print(root_binary(n_power(n, a), b))

power(2, 5, 3)

