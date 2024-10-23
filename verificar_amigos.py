def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def son_amigos(num1, num2):
    return suma_divisores(num1) == num2 and suma_divisores(num2) == num1

# Leer dos números
n1 = int(input("INGRESA EL PRIMER NÚMERO: "))
n2 = int(input("INGRESA EL SEGUNDO NÚMERO: "))

# Verificar si son amigos
if son_amigos(n1, n2):
    print(f"{n1} Y {n2} SON NÚMEROS AMIGOS.")
else:
    print(f"{n1} Y {n2} NO SON NÚMEROS AMIGOS.")
