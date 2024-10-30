from geopy.geocoders import Nominatim # type: ignore

# Clase para obtener la dirección a partir de la latitud y longitud usando Nominatim
class Localizador:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        self.direccion = None

    def obtener_direccion(self):
        try:
            geolocator = Nominatim(user_agent="test")
            location = geolocator.reverse(f"{self.latitud}, {self.longitud}")
            self.direccion = location.address if location else "Dirección no encontrada"
        except Exception as e:
            print(f"Error al obtener la dirección: {e}")
            self.direccion = "Error al obtener la dirección"
        return self.direccion