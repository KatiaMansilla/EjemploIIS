def suma_divisores_propios(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    return suma
 
def son_amigos(num1, num2):
    return suma_divisores_propios(num1) == num2 and suma_divisores_propios(num2) == num1
 
# SOLICITAR 2 NÚMEROS AL USUARIO 
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
 
# VERIFICAR SI SON AMIGOS 
if son_amigos(num1, num2):
    print(f"{num1} y {num2} son números amigos.")
else:
    print(f"{num1} y {num2} no son números amigos.")
