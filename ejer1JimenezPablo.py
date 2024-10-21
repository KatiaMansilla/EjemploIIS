a = int(input("INGRESE EL NUMERO 1: "))
b = int(input("INGRESE EL NUMERO 2: "))
suma = 0
for i in range(1, a):
    if a % i == 0: 
        suma += i
if suma == b:
    print("LOS NUMEROS SON AMIGOS")
else:
    print("LOS NUMEROS SON ENEMIGOS")
