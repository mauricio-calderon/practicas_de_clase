def f(x, y):
    a = 1
    b = 2
    if x > y:
        print("x es mayor")
    else:
        print("y es mayor")
    for i in range(5):
        print(i)
    return a + b

resultado = f(10,3)
print(resultado)