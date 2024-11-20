#!/bin/bash

# Activar el entorno virtual si existe
if [ -d ".venv" ]; then
  source .venv/bin/activate
  echo "Entorno virtual activado"
else
  echo "Entorno virtual no encontrado, ejecutando sin él"
fi

# Ejecutar el script principal
python3 src/GestorDeDatosClimaticos/MAIN.py