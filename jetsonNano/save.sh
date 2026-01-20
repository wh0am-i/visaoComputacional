#!/bin/bash

CONTAINER_NAME="container_visao_computacional"
NOVO_NOME="container_teste_yolo"

# 1. Identifica o ID do container pelo nome
CONTAINER_ID=$(sudo docker ps --filter "name=$CONTAINER_NAME" --format "{{.ID}}")

if [ -z "$CONTAINER_ID" ]; then
    echo "❌ Erro: Nenhum container '$CONTAINER_NAME' foi encontrado rodando."
    exit 1
fi

echo "✅ Container encontrado: $CONTAINER_ID"

# 2. Realiza o commit
echo "💾 Salvando alterações em '$NOVO_NOME'..."
sudo docker commit $CONTAINER_ID $NOVO_NOME

if [ $? -eq 0 ]; then
    echo "🚀 Sucesso! Imagem '$NOVO_NOME' criada com as suas edições."
    echo "Para rodar ela no futuro: sudo docker run -it --runtime=nvidia $NOVO_NOME"
else
    echo "❌ Erro ao tentar realizar o commit."
fi

