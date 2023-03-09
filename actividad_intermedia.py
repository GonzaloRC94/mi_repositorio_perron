
# Acciones: Crear, modificar, mostrar
# Caracteristicas: Nombre, Cantidad de Alumnos, Estado(No Iniciado / Activo), cantidad de clases.
# Funciones adicionales:
#   - Mostar todos los cursos existentes
#   - Mostrar toda la información del curso seleccionado



#=================================================================================
# FUNCIONES
#=================================================================================
def agregar_curso(lst: list):
    print("-" * 22)
    print("Agrega nuevo curso")
    print("-" * 22)
    c_nombre = input("Nombre del curso: ")
    n_alumn = input("Ingresa cantidad de alumnos: ")
    status = input("Estado del curso: ")
    n_clases = input("Ingresa el número de clases: ")

    nueva_entrada = {
        "nombre":c_nombre,
        "cantidad":n_alumn,
        "estado":status,
        "cantidad clases":n_clases
    }
    lst.append(nueva_entrada)

def mostrar_curso(lst: list):
    for key in lst:
        print("-", key.get("nombre"))

    select_curso = input("Qué curso quieres checar?")

    for curso in lst:
        if curso.get("nombre") == select_curso:
            print("\nEsta es la información del curso... \n")
            for i in curso:
                print(f" {i}: {curso[i]}")



def modificar_curso(lst:list):

    print("\nEstos son los cursos disponibles...\n")
    for key in lst:
        print("-", key.get("nombre"))

    mod_curso = input("\nQué curso quieres modificar su estado?")

    for curso in lst:
        if curso.get("nombre") == mod_curso:

            viejo_estado = curso.get("estado")
            print(f"\nEstado actual del curso: {curso.get('estado')}")
            nuevo_estado = input("Ingresa el nuevo estado del curso: ")
            curso["estado"] = nuevo_estado
            modificado = curso
            break

    if nuevo_estado == viejo_estado:
        print("\n\tEl estado quedo igual que antes.")
    else:
        print(f"""
        ¡Cambio Exitoso!
        Estado del curso:  {modificado['estado']}
        """)




#=================================================================================
# MAIN
#=================================================================================

#Un curso agregado por default
lista_cursos = [{"nombre":"python", "cantidad":15,"estado":"activo", "cantidad clases":50}]

acciones = ("crear", "modificar", "mostrar", "salir")     # Tupla

if not lista_cursos:
    print("=" * 70)
    print("No hay cursos archivados. Prosigue con el proceso de crear uno.")
    print("=" * 70)
    agregar_curso(lista_cursos)

while True:
    lista_acciones = " | ".join(acciones)
    accion = input(f"\nSelecciona la opción que desees utilizar:  {lista_acciones} \n")

    if accion == acciones[0]: agregar_curso(lista_cursos)           # Crear
    elif accion == acciones[1]: modificar_curso(lista_cursos)       # Modificar estado
    elif accion == acciones[2]: mostrar_curso(lista_cursos)         # Mostrar
    elif accion == acciones[3]: break                               # Salir del bucle