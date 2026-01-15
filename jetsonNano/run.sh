#!/bin/bash

# Cria uma nova sessão do tmux
tmux new-session -d -s monitoramento 'python3 index.py'

# Divide a tela horizontalmente para o sensors
tmux split-window -h 'watch -n 1 sensors'

# Divide a tela verticalmente para o htop
tmux split-window -v 'htop'

# Abre a sessão para visualização
tmux attach-session -t monitoramento
