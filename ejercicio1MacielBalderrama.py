def suma_divisores(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    return suma

def son_amigos(num1, num2):
    return suma_divisores(num1) == num2 and suma_divisores(num2) == num1

# aqui leemos los números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if son_amigos(num1, num2):
    print(f"{num1} y {num2} son números amigos.")
else:
    print(f"{num1} y {num2} no son números amigos.")
