def suma_divisores_propios(n):
    return sum([i for i in range(1, n) if n % i == 0])

def son_amigos(num1, num2):
    return suma_divisores_propios(num1) == num2 and suma_divisores_propios(num2) == num1

numero1 = int(input("INTRODUCE EL PRIMER NÚMERO: "))
numero2 = int(input("INTRODUCE EL SEGUNDO NÚMERO: "))

if son_amigos(numero1, numero2):
    print(f"{numero1} y {numero2} SON AMIGOS!")
else:
    print(f"{numero1} y {numero2} NO SON AMIGOS!")
  
