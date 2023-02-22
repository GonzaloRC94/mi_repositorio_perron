
altura_min = 1.62                                                           # >1.62
edad_min = 14                                                               # >14
usuario_altura = float(input("Ingresa tu altura: "))
usuario_edad = int(input("Ingresa tu edad:"))

if usuario_edad > edad_min and usuario_altura > altura_min:
    print("Súbete, viejón!!!")
elif usuario_edad < edad_min:
    print("Tas bien joven. No puedes.")
elif usuario_altura < altura_min:
    print("Tas muy chaparro. No puedes.")


