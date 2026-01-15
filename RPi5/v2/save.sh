#!/bin/bash

# 1. Identifica o ID do container que está rodando a imagem da Ultralytics
CONTAINER_ID=$(sudo docker ps --filter "ancestor=ultralytics/ultralytics:latest-jetson-jetpack4" --format "{{.ID}}")

if [ -z "$CONTAINER_ID" ]; then
    echo "❌ Erro: Nenhum container da Ultralytics foi encontrado rodando."
    exit 1
fi

echo "✅ Container encontrado: $CONTAINER_ID"

NOVO_NOME="container_teste_yolo"

# 3. Realiza o commit
echo "💾 Salvando alterações em '$NOVO_NOME'..."
sudo docker commit $CONTAINER_ID $NOVO_NOME

if [ $? -eq 0 ]; then
    echo "🚀 Sucesso! Imagem '$NOVO_NOME' criada com as suas edições."
    echo "Para rodar ela no futuro: sudo docker run -it --runtime=nvidia $NOVO_NOME"
else
    echo "❌ Erro ao tentar realizar o commit."
fi
