
def suma(a, b, C):
    return a + b + C

def resta(a, b, C):
    return a - b - C

def multiplicacion(a, b, C):
    return a * b * C

def division(a, b, C):
    if b == 0:
        return "Error: no se puede dividir entre 0"
    return a / b / C
def potencia( a, b, C):
    return a ** b ** C
print("Calculadora básica")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. potencia")

opcion = input("Elige una opción (1/2/3/4/5): ")

num1 = float(input("Ingresa el primer número:"))
num2 = float(input("Ingresa el segundo número:"))
num3 = float(input("ingrese el tercer nùmero:"))

if opcion == "1":
    print("Resultado:", suma(num1, num2, num3))
elif opcion == "2":
    print("Resultado:", resta(num1, num2, num3))
elif opcion == "3":
    print("Resultado:", multiplicacion(num1, num2, num3))
elif opcion == "4":
    print("Resultado:", division(num1, num2))
elif opcion =="5":
    print("resultado:", potencia(num1,num2, num3 ))
else:
    print("Opción no válida") 