#!/bin/bash

CONTAINER="container_visao_computacional"
TARGET_DIR="/ultralytics/visaoComputacional/container"

# Permitir que o container acesse a tela do host
xhost +local:root

# Verifica se o container existe
if docker container inspect "$CONTAINER" >/dev/null 2>&1; then
    echo "🚀 Iniciando container com GUI..."

    # Inicia o container e abre um shell direto na pasta TARGET_DIR
    docker start -ai "$CONTAINER" \

else
    echo "❌ Container não encontrado."
    echo "Execute o setup.sh primeiro."
fi

