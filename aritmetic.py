
def suma(a, b):
    return a+b


def resta(a, b):
    return a-b


def multiplica(a, b):
    ac = 0
    for i in range(1, b+1):
        ac = suma(ac, a)
    return ac


def divide(D, d):
    """bard answer to "un codigo python que implemente el C de la division entera repitiendo restas"
    """
    if D < d:
        return 0
    C = 0
    while D >= d:
        D = resta(D, d)  # D -= d  
        C = suma(C, 1)   # C += 1
    return C


if __name__ == "__main__":

    a = 2
    b = 3
    print(suma(a, b))  # 5
    print(resta(a, b))    # -1

    a = 6
    b = 4
    print(multiplica(a, b))  # 24
    print(divide(a, b))  # 1
    print(divide(b, a))   # 0
