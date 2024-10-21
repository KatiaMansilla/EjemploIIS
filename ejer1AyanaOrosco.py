def suma_divisores_propios(n):
    """Calcula la suma de los divisores propios de n."""
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def son_numeros_amigos(num1, num2):
    """Verifica si num1 y num2 son números amigos."""
    return suma_divisores_propios(num1) == num2 and suma_divisores_propios(num2) == num1

#LEER DOS NÚMEROS DEL USUARIO
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

#VERIFICAR SI SON NUMEROS AMIGOS
if son_numeros_amigos(numero1, numero2):
    print(f"{numero1} y {numero2} son números amigos.")
else:
    print(f"{numero1} y {numero2} no son números amigos.")
