# Visão Computacional – YOLOv8 no Jetson Nano

Projeto de **visão computacional em tempo real** utilizando **YOLOv8** com diferentes formatos de modelo (`.pt`, `.onnx`, `.engine`) executando no **NVIDIA Jetson Nano**, com foco em **performance, benchmark e inferência otimizada**.

---

### Estrutura do Projeto

jetsonNano/
├── convert.py # Script para conversão de modelos (PT → ONNX → Engine)
├── index.py # Inferência padrão com YOLOv8
├── index2.py # Inferência alternativa com métricas de desempenho
├── indexGUILess.py # Inferência sem interface gráfica (headless)
├── run.sh # Script de execução com tmux para verificação performance
├── log.txt # Log de métricas (FPS, latência, CPU)
├── yolov8n.pt # Modelo YOLOv8 original (PyTorch)
├── yolov8n.onnx # Modelo exportado para ONNX
├── yolov8n.engine # Modelo otimizado (TensorRT / ncnn)
└── venv/ # Ambiente virtual Python; iniciar com venv/bin/activate
---

### Requisitos
- Ubuntu (JetPack instalado)
- Python 3.8+
- CUDA + cuDNN
- TensorRT (ou backend compatível)
- OpenCV

