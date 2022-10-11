def z_i(x, y):
    osszeg = 0
    for i in range(x, y):
        osszeg += i
    return osszeg

print(z_i(10, 20))