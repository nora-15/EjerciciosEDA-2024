from pymongo import MongoClient

# Clase GestorDeDatosClimaticos para manejar el flujo de datos y presentación



import json
from clases.localizador import Localizador


class GestorDeDatosClimaticos:

    ubicaciones = []


    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        print("Iniciando gestor de datos climaticos")
        print(f"Numero de ubicaciones actuales: {self.get_numero_ubicaciones()}")


    def get_numero_ubicaciones(self):
        return len(self.ubicaciones)

    def mostrar_codigos_postales_y_provincias_almacenadas(self):
        provincias_codigos_postales = {}
        for ubicacion in self.ubicaciones:
            if ubicacion.provincia in provincias_codigos_postales:
                provincias_codigos_postales[ubicacion.provincia].append(ubicacion.codigo_postal)
            else:
                provincias_codigos_postales[ubicacion.provincia] = [ubicacion.codigo_postal]

        if provincias_codigos_postales:
            print(json.dumps(provincias_codigos_postales, indent=2, ensure_ascii=False))
        else:
            print("No hay ubicaciones almacenadas")

    # metodos necesarios
    def insertar_nueva_ubicacion(self,latitud, longitud):
        ubicacion_encontrada = False
        for ubicacion in self.ubicaciones:
            if ubicacion.check_lat_lng(latitud, longitud):
                ubicacion_encontrada = True
                print("================================================")
                print("Ubicación ya existe")
                print(ubicacion.mostrar_informacion())
                print("================================================")
                break
        
        if not ubicacion_encontrada:
            p=Localizador(latitud,longitud)#con esto obtenemos ciudad, cp, barrio; a traves de la clase localizador dandoles solo la long y lat
            self.ubicaciones.append(p)#esto lo que hace es añadir lo que esta almacenado en p al la lista de ubicaciones 
            tabla=p.to_dict()# y con esto, convertimos a tabla hash
            self.client['localizaciones']['hola'].insert_one(tabla) # con esto, lo que hace es insertar la tabla en el database del mongo
            #almacenar en la base de datos la tabla hash de la clase p
            print("Ubicación agregada correctamente")
        else:
            print("Ubicación ya existe")
        return ubicacion_encontrada

    def buscar_por_codigo_postal(self,codigo_postal):
        ubicacion_encontrada = None
        for ubicacion in self.ubicaciones:
            if ubicacion.codigo_postal == codigo_postal:
                ubicacion_encontrada = ubicacion
                break
        return ubicacion_encontrada
    
    def buscar_por_provincia(self,provincia):
        lista_ubicaciones = []
        for ubicacion in self.ubicaciones:
            if ubicacion.provincia == provincia:
                lista_ubicaciones.append(ubicacion)
        return lista_ubicaciones