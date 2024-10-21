def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def son_amigos(num1, num2):
    return suma_divisores(num1) == num2 and suma_divisores(num2) == num1

# Leer dos números
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))

# Verificar si son amigos
if son_amigos(n1, n2):
    print(f"{n1} y {n2} son números amigos.")
else:
    print(f"{n1} y {n2} no son números amigos.")
