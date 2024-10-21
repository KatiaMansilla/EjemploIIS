def suma_divisores(n):
    """Calcula la suma de los divisores propios de un número."""
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

def son_amigos(num1, num2):
    """Verifica si dos números son amigos."""
    return suma_divisores(num1) == num2 and suma_divisores(num2) == num1

def main():
    # Leer dos números del usuario
    try:
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))

        # Verificar si son amigos
        if son_amigos(numero1, numero2):
            print(f"{numero1} y {numero2} son números amigos.")
        else:
            print(f"{numero1} y {numero2} no son números amigos.")
    except ValueError:
        print("Por favor, ingrese solo números enteros.")

if __name__ == "__main__":
    main()
