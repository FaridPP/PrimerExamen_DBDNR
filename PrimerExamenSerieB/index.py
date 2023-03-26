from crud import *
from function_basic import *

while True:
    print("Seleccione una opción del menú: \n"
          "[1] Ver todos los libros de la base de datos.\n"
          "[2] Ver los libros publicados en cierto año.\n"
          "[3] Buscar libro por su título.\n"
          "[4] Agregar un libro.\n"
          "[5] Modificar un libro.\n"
          "[6] Eliminar un libro.\n"
          "[7] Salir.\n")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        MostrarLibros()
    elif opcion == 2:
        anio = int(input("Ingrese el año: "))
        MostrarLibrosPublicacion(anio)

    elif opcion == 3:
        titulo = input("Ingrese el título del libro: ")
        MostrarLibros(titulo)

    elif opcion == 4:
        Libro = Crear_JsonLibro()
        CrearLibro(Libro)

    elif opcion == 5:
        titulo = input("Ingrese el titulo del libro a modificar: ")
        Libro = Crear_JsonActulizar()
        ActualizarLibro(titulo, Libro)

    elif opcion == 6:
        titulo = input("Ingrese el titulo del libro a eliminar: ")
        EliminarLibro(titulo)

    elif opcion == 7:
        break
    else:
        print("Seleccione un número entero entre 1 y 7.")


