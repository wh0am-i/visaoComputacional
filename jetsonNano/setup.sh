#!/bin/bash

IMAGE="n0n4mee/yolo_jetson:v1"
CONTAINER="container_visao_computacional"

# Puxa a imagem mais recente
docker pull $IMAGE

# Checa se o container já existe
if docker container inspect "$CONTAINER" >/dev/null 2>&1; then
    echo " Container existente encontrado. Iniciando..."
    sudo docker start -ai "$CONTAINER"
else
    echo " Criando novo container..."
    sudo docker run -it \
      --name "$CONTAINER" \
      -p 8080:8080 \
      --ipc=host \
      --runtime=nvidia \
      --device /dev/video0:/dev/video0 \
      -e DISPLAY=$DISPLAY \
      -v /tmp/.X11-unix:/tmp/.X11-unix \
      -v /usr/src/app:/usr/src/app \
      "$IMAGE"
fi

