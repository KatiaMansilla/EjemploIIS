#ANDRES WILFREDO BALDIVIEZO FARFAN
def suma_divisores_propios(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def sonAmigos(num1, num2):
    
    return suma_divisores_propios(num1) == num2 and suma_divisores_propios(num2) == num1


a = int(input("Introduce el numero 1: "))
b = int(input("Introduce el numero 2: "))

# VERIFICAR SI SON AMIGOS
if sonAmigos(a, b):
    print(f"{a} y {b} son amigos")
else:
    print(f"{a} y {b} no son amigos")
