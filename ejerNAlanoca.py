def calcular(n):
   i=1
   suma=0
   while i<n:
     if n%i==0:
        suma+=i
     i+=1
   return suma

a= int(input("Ingrese el primer numero: "))
b= int(input("Ingresw el segundo numero: "))

if calcular(a)==b and calcular(b)==a:
   print("Los numeros son amigos")
else:
   print("Los numeros no son amigos")
