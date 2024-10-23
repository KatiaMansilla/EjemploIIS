# Función para obtener la suma de los divisores propios de un número
def suma_divisores_propios(n):
    suma = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            suma += i
    return suma

# Función para verificar si dos números son amigos
def son_amigos(num1, num2):
    return suma_divisores_propios(num1) == num2 and suma_divisores_propios(num2) == num1

# Programa principal
def main():
    # Leer los dos números
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

    # Verificar si son amigos
    if son_amigos(num1, num2):
        print(f"{num1} y {num2} son números amigos.")
    else:
        print(f"{num1} y {num2} no son números amigos.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
