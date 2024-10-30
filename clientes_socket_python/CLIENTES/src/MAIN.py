from cliente.funciones_cliente import iniciar_client

# Configuración del servidor
# HOST = '127.0.0.1'  # Dirección IP local (localhost)
# PORT = 12345        # Puerto del servidor
if __name__ == "__main__":
    
    HOST = input("Introduce el HOST: ")
    PORT= input("Introduce el PORT: ")

    PORT = int(PORT)
    iniciar_client(HOST,PORT)