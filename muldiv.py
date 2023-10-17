import sumres

def multiplica(a, b):
    ac = 0
    for i in range(1, b+1):
        ac = sumres.suma(ac, a)
    return ac


def divide(D, d):
    """bard answer to "un codigo python que implemente el C de la division entera repitiendo restas"
    """
    if D < d:
        return 0
    if D == d:
        return 1
    C = 0
    while D >= d:
        D = sumres.resta(D, d) 
        C = sumres.suma(C,1)
    return C


if __name__ == "__main__":

    a = 6
    b = 4
    print(multiplica(a, b))  # 24
    print(divide(a, b))  # 1
    print(divide(b,a))   # 0
