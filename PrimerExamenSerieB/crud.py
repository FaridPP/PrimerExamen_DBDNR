from parameters import collections

def MostrarLibros(titulo=None):
    if titulo is None:
        documents = collections.find()
        for document in documents:
            print("ID:",document["_id"])
            print("Título:",document["Titulo"])
            print("Autor:",document["Autor"])
            print("Publicacion:", document["Publicacion"])
            print("Género:",document["Genero"])
            print("**************************")
    else:
        query = {"Titulo":titulo}
        document = collections.find_one(query)
        print("ID:",document["_id"])
        print("Título:",document["Titulo"])
        print("Autor:",document["Autor"])
        print("Publicacion:", document["Publicacion"])
        print("Género:",document["Genero"])
        print("**************************")

def MostrarLibrosPublicacion(publicacion):
    query = {"Publicacion":publicacion}
    documents = collections.find(query)
    for document in documents:
        print("ID:",document["_id"])
        print("Título:",document["Titulo"])
        print("Autor:",document["Autor"])
        print("Publicacion:", document["Publicacion"])
        print("Género:",document["Genero"])
        print("**************************")

def CrearLibro(Libro):
    resultado = collections.insert_one(Libro)
    print(resultado.inserted_id)

def ActualizarLibro(titulo, LibroJson):
    query = {"Titulo": titulo}
    new_value = {"$set": LibroJson}
    resultado = collections.update_one(query, new_value)
    print(resultado.modified_count)

def EliminarLibro(titulo):
    query = {"Titulo": titulo}
    resultado = collections.delete_one(query)
    print(resultado.deleted_count)
