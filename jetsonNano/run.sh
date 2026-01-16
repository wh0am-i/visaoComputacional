#!/bin/bash

CONTAINER="container_visao_computacional"

# Permitir que o container acesse a tela do host
xhost +local:root

if docker container inspect "$CONTAINER" >/dev/null 2>&1; then
    echo "🚀 Iniciando container com GUI..."
    docker start -ai "$CONTAINER"
else
    echo "❌ Container não encontrado."
    echo "Execute o setup.sh primeiro."
fi

