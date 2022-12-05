import os #libreria para amanejar archivos

CARPETA = 'contactos/' #carpeta de contactos
EXTENSION = '.txt' #extension

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria
# funcion principal
def app():
    mostrar_menu() #muestra el menu de opciones)
    crear_directorio() #revisa si la carpeta existe o no
    
    # preguntar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion: \r\n')
        opcion = int(opcion)
        # ejecutar opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False #para que o siga preguntando
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida, intente de nuevo')

def agregar_contacto():
    print('Escribe los datos del nuevo Contacto')
    nombre_contacto = input('Nombre:\r\n')

    # validar nombre (isfile revisa si un archivo ya existe)
    existe = existe_contacto(nombre_contacto)
    if not existe:
    
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo: #crea el archivo contactos/'nombre_contacto'
            #campos
            telefono_contacto = input('Numero de Telefono: \r\n')
            categoria_contacto = input('Categoria del Contacto: \r\n')

            # intstaciamos la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # escribir el archivo
            archivo.write('Nombre: ' + nombre_contacto + '\r\n')
            archivo.write('Telefono: ' + telefono_contacto + '\r\n')
            archivo.write('Categoria: ' + categoria_contacto + '\r\n')

            # mensaje de exito
            print('\r\n Contacto creado Correctamente \r\n')
    else:
        print('Ese Contacto ya existe')
    # reiniciar la app
    app()

def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')
     # validar nombre 
    existe = existe_contacto(nombre_anterior)
    
    if existe:
        # abrimos el archivo
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            # editamos los campos
            nombre_contacto = input('Nuevo Nombre del Contacto: \r\n')
            telefono_contacto = input('Nuevo Numero de Telefono: \r\n')
            categoria_contacto =  input('Nueva Categoria de Contacto: \r\n')

            # instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            # escribimos en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

        # cambiamos el nombre del archivo (fuera del with porque debe estar cerrado el archivo)
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
        print('Contacto Editado con Exito')
    else:
        print('Contacto Inexistente')
    app()

def mostrar_contactos():
    # lisdtdir lista los archivos de un ditrectorio
    archivos = os.listdir(CARPETA)
    # recorremos solo que termina en .txt
    archivos_txt =  [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                # imprime los contenidos
                print(linea.rstrip())
            # imprime un separador
            print('\r\n')

def buscar_contacto():
    nombre = input('Que Contacto desea Buscar?: \r\n')
    # no usar mucho el rty porque consume mucha memoria y demas
    try: #trata de abrir el archivo:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError: #si ocurre un error o no existe
        print('El archivo no existe')
        print(IOError)
    
    # reiniciar la app
    app()

def eliminar_contacto():
    nombre = input('Que contacto desea Eliminar?: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Contacto eliminado exitosamente')
    except IOError: #si ocurre un error o no existe
        print('El Contacto no existe')
        print(IOError)

def existe_contacto(nombre):
    # (isfile revisa si un archivo ya existe)
    return os.path.isfile(CARPETA + nombre + EXTENSION)

def mostrar_menu():
    print('Seleccione del Menu lo que desea hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contacto')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')

def crear_directorio(): 
    if not os.path.exists(CARPETA): #si esta carpeta no existe existe...
        os.makedirs(CARPETA) #crea la carpeta

app()