
"""
QA Minds Labs estaría necesitando de una agenda que permita guardar a sus alumnos del curso de Python. En este sentido el sistema debe contar con la posibilidad de crear un  Alumno, las cuales tendrán un nombre, apellido, un mail y un estado. Los Alumnos pueden tener los estados de: Activo, Mora, Retirado Egresado y  Certificado.
Los Alumnos por defecto se crearán en estado Activo.
El sistema debe poder dar de alta un Alumno.
El sistema debe permitir buscar un alumno y poder modificar su estado (Ejemplo: de Activo a Egresado)
El sistema debe permitir mostrar TODOS los Alumnos existentes, como también la posibilidad de mostrar todos los alumnos por un estado definido.
"""

########################################################################
# FUNCTIONS
########################################################################

class Student:
    default_status = "Active"
    available_statuses = ["Active", "Mora", "Retired", "Graduate", "Certified"]

    def __init__(self, name: str, last_name: str, email: str, status: str):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.status = status

    def __str__(self):
        pass
    def __repr__(self):
        pass


def add_student():
    print("ADD STUDENT")
    name = input("Enter Student's Name: ")
    last_name = input("Enter Student's last name: ")
    email = input("Enter Student's email: ")

    student = Student(name, last_name, email)
    STUDENTS.append(student)


def update():
    pass
def search_name():
    pass
def show_exist():
    pass
def show_status():
    pass



########################################################################
# MAIN
########################################################################

STUDENTS = []
MENU = {
    "add": add_student,
    "update": update,
    "search by name": search_name,
    "show existing": show_exist,
    "show by status": show_status,
}

while True:
    action = input(f"Que accion deases realizar: {' | '.join(MENU.keys())}\n")
    if action in MENU.keys():
        MENU[action](STUDENTS)
    else:
        print(f"Action not supported: {action}")