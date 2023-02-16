var1 = int(input("Ingresa el primer número entero:"))
var2 = int(input("Ingresa el segundo número entero: "))
suma = var1+var2
resta = var2 - var1
multiplicacion = var1 * var2
division_entera = var2 // var2
resto_division = var2%var1

print(f""" 
        La variable suma es : {suma}
        La variable resta es: {resta}
        La variable multiplicación es: {multiplicacion}
        La variable division_entera es: {division_entera}
        La variable resto_division es: {resto_division}""")
