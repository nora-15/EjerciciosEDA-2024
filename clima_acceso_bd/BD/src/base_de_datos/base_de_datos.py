from pymongo import MongoClient
from clases.localizador import Localizador
class basedatos: 
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.dbname = "localizaciones"
        self.collectionname = "info"
        print("base de datos creada")

    def numerolocalizaciones(self):
        bd = self.client[self.dbname][self.collectionname] #accedemos a las localizaaciones y lo alacenamos en la bd
        numerototal = bd.count_documents({})
        return numerototal 
    
    #es una funcion que lo que hace es insertar la localizacion
    def insertarubicacion(self,localizacion):
        self.client[self.dbname][self.collectionname].insert_one(localizacion)

    def buscarporlatlong(self,latitud,longitud):
        resultado = self.client[self.dbname][self.collectionname].find_one({"latitud":latitud,"longitud":longitud}) #que busque en la base de datos si ya está una localcizacion con esa lati y long
        if (resultado!=None):
            localizacion = Localizador(resultado["latitud"],resultado["longitud"])
            return localizacion
        else: 
            return None