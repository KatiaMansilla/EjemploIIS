def divisores_propios(n):
    # Retorna una lista de divisores propios de un número n (excluyendo al propio n)
    return [i for i in range(1, n) if n % i == 0]

def son_amigos(num1, num2):
    # Calcula la suma de los divisores propios de cada número
    suma_divisores_num1 = sum(divisores_propios(num1))
    suma_divisores_num2 = sum(divisores_propios(num2))
    
    # Verifica si son amigos :3
    return suma_divisores_num1 == num2 and suma_divisores_num2 == num1

# Solicitamos los dos números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Verificar si son números amigos
if son_amigos(numero1, numero2):
    print(f"{numero1} y {numero2} son números amigos.")
else:
    print(f"{numero1} y {numero2} no son números amigos.")
