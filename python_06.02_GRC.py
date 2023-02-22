
print("Ingresa tu fecha de nacimiento...")
usuario_dia = int(input("Día: "))
usuario_mes = int(input("Mes: "))
usuario_año = int(input("Año: "))

actual_dia = 21
actual_mes = 2
actual_año = 2023

GEN_SILENT = range(1920,1939)
GEN_BOOMERS = range(1940, 1959)
GEN_X = range(1960, 1979)
GEN_Y = range(1980, 1989)
GEN_Z = range(1990, 2023)

print(f"\nTienes {actual_año-usuario_año} años")

if usuario_mes <= actual_mes and usuario_dia < actual_dia:
    print("Ya fue tu cumple, perrillo.")
else:
    print("Todavía no cumples años.")


if usuario_año in GEN_SILENT:
    print("Eres de la Generación Silenciosa")
elif usuario_año in GEN_BOOMERS:
    print("Eres un Baby Boomer")
elif usuario_año in GEN_X:
    print("Eres de la Generación X")
elif usuario_año in GEN_Y:
    print("Eres de la Generación Y")
elif usuario_año in GEN_Z:
     print("Eres de la Generación Z")
else:
    print("\nNo te pases!!! Ya eres longevo")