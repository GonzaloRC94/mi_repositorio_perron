def suma(a, b):
    suma = a + b
    return suma
def resta(a, b):
    resta = a - b
    return resta
def multiplicacion(a, b):
    multiplicacion = a * b
    return multiplicacion
def division(a, b):
    division = a / b
    return division
def modulo(a, b):
    modulo = b % a
    return modulo
def conversion_float(a):
    cambio = float(a)
    return cambio
def celciuas_fahrenheit(a):
    resultado = a * 1.8 + 32
    return resultado


var1 = float(input("Ingresa el valor del primer número: "))
var2 = float(input("Ingresa el valor del segundo número: "))
var3 = float(input("Ingresa valor para cambiar a flotante: "))
var_temp = float(input("Ingresa valor para converitr de Celcius a Fahrenheit: "))

print(f"""
    El resultado de la suma es: {suma(var1, var2)}
    El resultado de la resta es: {resta(var1, var2)}
    El resultado de la multiplicacion es: {multiplicacion(var1, var2)}
    El resultado de la división es: {division(var1, var2)}
    El resultado de la módulo es: {modulo(var1, var2)}

    El número entero es {conversion_float(var3)}
    La conversión de C° a F° es: {celciuas_fahrenheit(var_temp)}F°""")

