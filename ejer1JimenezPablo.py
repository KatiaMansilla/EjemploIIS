a = int(input("Ingrese numero de la persona 1: "))
b = int(input("Ingrese numero de la persona 2: "))
suma = 0
for i in range(1, a):
    if a % i == 0: 
        suma += i
if suma == b:
    print("Los numeros son amigos")
else:
    print("Los numeros son enemigos")
