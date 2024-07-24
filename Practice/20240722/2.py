a, b = 0, 1
while a < 10:
    print(a, end=', ' if a < 8 else '')
    a, b = b, a+b
