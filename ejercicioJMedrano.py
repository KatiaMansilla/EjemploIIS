def suma_divisores_propios(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def son_amigos(num1, num2):
    return suma_divisores_propios(num1) == num2 and suma_divisores_propios(num2) == num1

# Solicitar los números al usuario
try:
    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el segundo número: "))

    if son_amigos(numero1, numero2):
        print("SON AMIGOS!!")
    else:
        print("NO SON AMIGOS!!")
except ValueError:
    print("Por favor, introduce números válidos.")
