Visão Computacional – YOLOv8 no Raspberry Pi 5

Projeto de visão computacional em tempo real utilizando YOLOv8 com diferentes formatos de modelo (.pt, .onnx, OpenVINO, NCNN) executando no Raspberry Pi 5, com foco em performance, benchmark e inferência otimizada.

### Estrutura do Projeto

RPi5/v2/ <br>
├── convert.py # Script para conversão de modelos (PT → ONNX → OpenVINO / NCNN) <br>
├── index.py # Inferência padrão com YOLOv8 <br>
├── GUIMode.sh # Execução em modo gráfico (GUI) <br>
├── terminalMode.sh # Execução em modo headless (sem interface gráfica) <br>
├── setup.sh # Script de configuração do ambiente <br>
├── run.sh # Script de execução para verificação de performance <br>
├── log.txt # Log de métricas (FPS, latência, CPU) <br>
├── yolov8n.pt # Modelo YOLOv8 original (PyTorch) <br>
├── yolov8n.onnx # Modelo exportado para ONNX <br>
├── yolov8n_openvino_model/ # Modelo otimizado OpenVINO <br>
├── yolov8n_ncnn_model/ # Modelo otimizado NCNN <br>
└── venv/ # Ambiente virtual Python; iniciar com venv/bin/activate <br>

### Requisitos
- Raspbian OS
- OpenVINO
- NCNN
- Flask
- Psutil
- OpenCV

### Instalação e uso
- source venv/bin/activate para iniciar o venv
- Rodar o setup.sh
- Usar o GUIMode.sh ou terminalMode.sh conforme o modo desejado (normalmente o sistema já está no GUIMode)
- Usar o run.sh para coletar métricas de performance ou algum dos index (alterar caminho do index.py para indexGUILess.py dentro do run.sh caso desejado usar o terminalMode)
