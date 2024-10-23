#EDICION - COMENTARIOS A MAYUSCULAS
def divisores_propios(n):
    # RETORNA UNA LISTA DE DIVISORES PROPIOS DE UN NUMERO N (EXCLUYENDO EL PROPIO N)
    return [i for i in range(1, n) if n % i == 0]

def son_amigos(num1, num2):
    # CALCULA LA SUMA DE LOS DIVISORES PROPIOS DE CADA NUMERO
    suma_divisores_num1 = sum(divisores_propios(num1))
    suma_divisores_num2 = sum(divisores_propios(num2))
    
    # VERIFICA SI SON AMIGOS :3
    return suma_divisores_num1 == num2 and suma_divisores_num2 == num1

# SOLICITMOS AL USUARIO LOS 2 NUEVOS NUMEROS
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# AQUI VERIFICAMOS SI SON AMIGOS
if son_amigos(numero1, numero2):
    print(f"{numero1} y {numero2} son números amigos.")
else:
    print(f"{numero1} y {numero2} no son números amigos.")

#EDICION COMPLETA
