
# Ejemplo de uso
from GestorDeDatosClimaticos.funciones_gestordedatos import GestorDeDatosClimaticos


if __name__ == "__main__":
    # Coordenadas del usuario
    latitud = input("inserta la latitud ")
    longitud = input("inserta la longitud ")

    # Crear el gestor de datos y obtener la información
    gestor = GestorDeDatosClimaticos(latitud, longitud)
    gestor.obtener_informacion()