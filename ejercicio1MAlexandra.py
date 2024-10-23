def suma_divisores_propios(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def son_amigos(num1, num2):
    return suma_divisores_propios(num1) == num2 and suma_divisores_propios(num2) == num1

# Leer los dos números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Verificar si son amigos
if son_amigos(numero1, numero2):
    print(f"{numero1} y {numero2} son números amigos.")
else:
    print(f"{numero1} y {numero2} no son números amigos.")
