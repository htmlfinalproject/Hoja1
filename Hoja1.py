numero = int(input("Ingrese la altura del triangulo"))
for i in range(numero):
    for j in range(i+1):
        print("*", end="")
    print("")

n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end=", ")

    n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")