

mes = int(input("Ingresa el No. del mes: "))

if mes in [12, 1, 2]:
    print("Estás en Invierno")
elif mes in [3, 4, 5]:
    print("Estás en Primavera")
elif mes in [6, 7, 8]:
    print("Estás en Verano")
elif mes in [9, 10, 11]:
    print("Estás en Otoño")
else:
    print("""   
    El mes ingresado no existe.
    Por favor, verifique e intente de nuevo.
    Atte: 'La Gerencia' 
    """)