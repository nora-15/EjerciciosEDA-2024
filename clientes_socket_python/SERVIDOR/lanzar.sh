#!/bin/bash

# Verificar si el entorno virtual ya existe
if [ ! -d "venv" ]; then
   
    python3 -m venv venv
fi

# Activar el entorno virtual

source venv/bin/activate

# Instalar las dependencias

pip install -r requirements.txt

# Ejecutar el script principal

python main.py
