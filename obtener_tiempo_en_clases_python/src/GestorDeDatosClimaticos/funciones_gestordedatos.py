

# Clase GestorDeDatosClimaticos para manejar el flujo de datos y presentación
from GestorDeDatosClimaticos.clase_LOCALIZADOR.funciones_clase_localizador import Localizador
from MAIN import Clima


class GestorDeDatosClimaticos:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        self.localizador = Localizador(latitud, longitud)
        self.clima = Clima(latitud, longitud)

    def obtener_informacion(self):
        # Obtener la dirección
        direccion = self.localizador.obtener_direccion()
        print(f"Dirección: {direccion}")
        
        # Obtener los datos climáticos
        temperatura, velocidad_viento = self.clima.obtener_datos_climaticos()
        print(f"Temperatura: {temperatura}°C")
        print(f"Velocidad del viento: {velocidad_viento} km/h")
