def Crear_JsonLibro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    publicacion = int(input("Ingrese el año de publicación: "))
    genero = input("Ingrese el género del libro: ")

    Libro = {
        "Titulo": titulo,
        "Autor": autor,
        "Publicacion": publicacion,
        "Genero": genero
    }
    return Libro

def Crear_JsonActulizar():
    print("Menu de opciones")
    print("[1] Modificar todo el documento.")
    print("[2] Moficar un elemento del documento.")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        return Crear_JsonLibro()
    elif opcion ==2:
        indice = input("Ingrese el indice a buscar: ")
        if indice == "Publicacion":
            valor = int(input("Ingrese el valor a sustituir: "))
            Libro = {indice: valor}
        else:
            valor = input("Ingrese el valor a sustituir: ")
            Libro = {indice: valor}
        return Libro