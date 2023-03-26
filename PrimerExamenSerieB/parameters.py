import pymongo

cliente = pymongo.MongoClient("mongodb://localhost:27017")

db=cliente["PrimerExamen"]
collections = db["Libros"]