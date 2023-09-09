list_prestamos = []
list_registro = []
login_exitoso = False

def formulario():
    print("FORMULARIO PRESTAMO: ")
    nombre = input("Ingrese su nombre: ")
    origen = input("Ingrese su origen: ")
    destino = input("Ingrese su destino: ")
    tarjeta = input("ingrese el número de tarjeta: ")
    list_prestamos.append({"nombre": nombre, "origen": origen, "destino": destino, "tarjeta": tarjeta})
    print("Su codigo de prestamo es:", tarjeta)

def registro():
    print("REGISTRO DE USUARIOS:")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    tarjeta = (input("Ingrese su codigo de prestamo: "))
    correo = input("Ingrese su correo electrónico: ")
    telefono = input("Ingrese su número de teléfono: ")
    list_registro.append({"nombre": nombre, "apellido": apellido, "tarjeta": tarjeta, "correo": correo, "telefono": telefono})

def login():
    print("LOGIN DE USUARIO:")
    global login_exitoso
    nombre = input("Ingrese su nombre: ")
    for registro in list_registro:
        if registro["nombre"] == nombre:
            login_exitoso = True
            menu()
            return
    print("Nombre no encontrado")

def menu():
    print("MENU CONSULTAS:")
    opcion = int(input("Elija una opción:\n1. Consulte su información\n2. Consulte sus préstamos\n"))
    if opcion == 1:
        consultar_informacion()
    elif opcion == 2:
        consultar_prestamos()

def consultar_informacion():
    nombre = input("Ingrese su nombre: ")
    for registro in list_registro:
        if registro["nombre"] == nombre:
            print("Nombre:", registro["nombre"])
            print("Apellido:", registro["apellido"])
            print("Número de codigo prestamo:", registro["tarjeta"])
            print("Correo electrónico:", registro["correo"])
            print("Número de teléfono:", registro["telefono"])
            return
    print("Nombre no encontrado")

def consultar_prestamos():
    nombre = input("Ingrese su nombre: ")
    for prestamo in list_prestamos:
        if prestamo["nombre"] == nombre:
            print("INFORMACION PRESTAMO:")
            print("Número de tarjeta:", prestamo["tarjeta"])
            print("Origen:", prestamo["origen"])
            print("Destino:", prestamo["destino"])
            return
    print("Nombre no encontrado")

formulario()
registro()
login()

if login_exitoso:
    menu()