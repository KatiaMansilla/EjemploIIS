#ANDRES WILFREDO BALDIVIEZO FARFAN
def suma_divisores_propios(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def sonAmigos(num1, num2):
    
    return suma_divisores_propios(num1) == num2 and suma_divisores_propios(num2) == num1


a = int(input("INTRODUCE EL NUMERO 1: "))
b = int(input("INTRODUCE EL NUMERO 2: "))

# VERIFICAR SI SON AMIGOS
if sonAmigos(a, b):
    print(f"{a} Y {b} SON AMIGOS")
else:
    print(f"{a} Y {b} NO SON AMIGOS")
