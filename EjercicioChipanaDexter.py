def suma_divisores(n):
    """Función que calcula la suma de los divisores propios de un número n."""
    return sum(i for i in range(1, n) if n % i == 0)

def son_numeros_amigos(num1, num2):
    """Verifica si num1 y num2 son números amigos."""
    return suma_divisores(num1) == num2 and suma_divisores(num2) == num1

# Leer dos números
numero1 = int(input("INGRESA EL PRIMER NUMERO: "))
numero2 = int(input("INGRESA EL SEGUNDO NUMERO: "))

# Verificar si son amigos
if son_numeros_amigos(numero1, numero2):
    print(f"{numero1} Y {numero2} SON NUMEROS AMIGOS.")
else:
    print(f"{numero1} Y {numero2} NO SON NUMEROS AMIGOS.")
