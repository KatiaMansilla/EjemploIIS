# solucion.py

def son_amigos(num1, num2):
    suma_divisores_num1 = sum(i for i in range(1, num1) if num1 % i == 0)
    suma_divisores_num2 = sum(i for i in range(1, num2) if num2 % i == 0)
    return suma_divisores_num1 == num2 and suma_divisores_num2 == num1

# Lectura de números
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

if son_amigos(n1, n2):
    print(f"{n1} y {n2} son números amigos.")
else:
    print(f"{n1} y {n2} no son números amigos.")
