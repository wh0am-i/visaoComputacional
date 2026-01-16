#!/bin/bash

set -e

IMAGE="n0n4mee/yolo_jetson:v1"
CONTAINER="container_visao_computacional"

echo "🔹 Atualizando sistema..."
sudo apt update && sudo apt upgrade -y

echo "🔹 Instalando dependências..."
sudo apt install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    x11-xserver-utils  # necessário para xhost

echo "🔹 Instalando Docker..."
if ! command -v docker &> /dev/null; then
    curl -fsSL https://get.docker.com | sudo sh
else
    echo "Docker já instalado."
fi

echo "🔹 Habilitando Docker no boot..."
sudo systemctl enable docker
sudo systemctl start docker

echo "🔹 Adicionando usuário ao grupo docker..."
sudo usermod -aG docker $USER

echo "⚠️  Faça logout/login após este script para usar docker sem sudo."

echo "🔹 Puxando imagem Docker..."
sudo docker pull $IMAGE

# Não iniciar container ainda, só criar
echo "🔹 Criando container..."
sudo docker create -it \
  --name "$CONTAINER" \
  -p 8080:8080 \
  --ipc=host \
  --runtime=nvidia \
  --device /dev/video0:/dev/video0 \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /usr/src/app:/usr/src/app \
  "$IMAGE"

echo "✅ Setup concluído!"

