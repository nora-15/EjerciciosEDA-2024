# Configuración del servidor
# HOST = '127.0.0.1'  # Dirección IP local (localhost)
# PORT = 12345        # Puerto del servidor

from servidor.funciones_servidor import iniciar_servidor


if __name__ == "__main__":
    
    serv_ip = input('ip del servidor: ')
    serv_port = input('puerto del servidor: ')

    print("Servidor iniciado en http://{}:{}".format(serv_ip,serv_port))

    iniciar_servidor(serv_ip,int(serv_port))

