#Ingreso de números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
#Crear las listas
factNum1 = []
factNum2 = []
#Ver si los números son amigos
for i in range (1, num1):
  if (num1%i = 0):
    factNum1.append(i)
sum1 = factNum1.sum()
for i in range (1, num2):
  if (num2%i = 0):
    factNum2.append(i)
sum2 = factNum2.sum()
#Mostrar mensaje
if (num1 == sum2 and num2 == sum1):
  print("Los números son amigos.")
else:
  print("Los números no son amigos.")