
def mi_funcion(a, b, c=None):                                           #Valor "None" para cuando quieras evadir un parametro
    suma = a+b                                                          #  adicional que no se necesite para la función.
    resta = a-b
    multiplicacion = a*b
    division = a/b
    print(f"""
    La suma es: {suma}
    La resta es: {resta}
    La multiplicacion {multiplicacion}
    La division es: {division}""")


var1 = int(input("Ingresa el primer número entero:"))
var2 = int(input("Ingresa el segundo número entero: "))

mi_funcion(var1, var2)

comparacion_1 = var1 > var2
comparacion_2 = var1 < var2
comparacion_3 = var1 == var2
comparacion_4 = var1 != var2

print(f"""
    El primer número es mayor que el segundo: {comparacion_1}
    El primer número es menor que el segundo: {comparacion_2}
    El primer número es igual al segundo: {comparacion_3}
    El primer número es diferente al segundo {comparacion_4}""")


