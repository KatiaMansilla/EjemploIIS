# Función para calcular la suma de los divisores propios de un número
def suma_divisores_propios(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

# Pedir los dos números al usuario
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Calcular la suma de los divisores propios de ambos números
suma1 = suma_divisores_propios(numero1)
suma2 = suma_divisores_propios(numero2)

# Determinar si son amigos
if suma1 == numero2 and suma2 == numero1:
    print(f"{numero1} y {numero2} son números amigos.")
else:
    print(f"{numero1} y {numero2} no son números amigos.")
