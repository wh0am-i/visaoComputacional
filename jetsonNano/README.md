# Visão Computacional – YOLOv8 no Jetson Nano

Projeto de **visão computacional em tempo real** utilizando **YOLOv8** com diferentes formatos de modelo (`.pt`, `.onnx`, `.engine`) executando no **NVIDIA Jetson Nano**, com foco em **performance, benchmark e inferência otimizada**.

---
### Estrutura do código

jetsonNano/ <br>
├── setup.sh # Script de start do container Docker da Nvidia <br>
├── run.sh # Script de execução com tmux para verificação de performance (rodar com index2.py ou indexGUILess.py) <br>
├── save.sh # Script para salvar alterações dentro do container <br>
├── GUIMode.sh # Execução em modo gráfico (GUI) <br>
└── terminalMode.sh # Execução em modo headless (sem interface gráfica) <br>


---
### Estrutura do código do container (não usar)

codigosContainer/ <br>
├── convert.py # Script para conversão de modelos (PT → ONNX → Engine) <br>
├── index.py # Inferência padrão com YOLOv8 <br>
├── index2.py # Inferência alternativa com métricas de desempenho <br>
├── indexGUILess.py # Inferência sem interface gráfica (headless); substituir número de IP pelo da rede na linha 78 <br>
├── log.txt # Log de métricas (FPS, latência, CPU) <br>
├── yolov8n.pt # Modelo YOLOv8 original (PyTorch) <br>
├── yolov8n.onnx # Modelo exportado para ONNX <br>
├── yolov8n.engine # Modelo otimizado (TensorRT / ncnn) <br>
└── venv/ # Ambiente virtual Python; iniciar com venv/bin/activate <br>
---

### Requisitos
- JetPack 4.6
- Flask
- Psutil
- OpenCV
obs: já instalados no container Docker

### Instalação e uso
- rodar setup.sh
- dentro do container navegar até a pasta visaoComputacional/
- rodar run.sh
- se desejado utilizar o indexGUILess.py, faz-se necessário executar o terminalMode.sh fora do container antes e alterar o index.py para indexGUILess.py dentro do run.sh de executar o run.sh
