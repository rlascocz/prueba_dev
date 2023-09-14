# Función para realizar una suma
def suma(a, b):
    return a + b

# Función para realizar una resta
def resta(a, b):
    return a - b

# Función para realizar una multiplicación
def multiplicacion(a, b):
    return a * b

# Función para realizar una división
def division(a, b):
    if b == 0:
        return "No es posible dividir por cero."
    return a / b

# Crea un diccionario que mapea opciones a funciones
operaciones = {
    1: suma,
    2: resta,
    3: multiplicacion,
    4: division,
}

# Mostrar un menú de opciones al usuario
print("Selecciona una opción:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Solicitar al usuario que ingrese su elección
opcion = input("Ingresa el número de la opción que deseas ejecutar: ")

# Convierte la entrada del usuario a un entero
opcion = int(opcion)

# Verificar si la opción seleccionada está en el diccionario y llamar a la función correspondiente
if opcion in operaciones:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = operaciones[opcion](num1, num2)
    print(f"El resultado es: {resultado}")
else:
    print("Opción no válida. Por favor, selecciona una opción válida.")

# Aquí puedes continuar con el flujo de tu programa después de ejecutar la operación seleccionada.
