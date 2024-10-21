def suma_factores(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    return suma

def son_amigos(num1, num2):
    return suma_factores(num1) == num2 and suma_factores(num2) == num1

# Entrada de los números por teclado
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Verificación si son amigos
if son_amigos(num1, num2):
    print(f"{num1} y {num2} son números amigos.")
else:
    print(f"{num1} y {num2} no son números amigos.")
