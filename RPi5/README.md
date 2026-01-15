# Visão Computacional – YOLOv8 no Raspberry Pi 5

Projeto de **visão computacional em tempo real** utilizando **YOLOv8** com diferentes formatos de modelo (`.pt`, `.onnx`, OpenVINO, NCNN) executando no **Raspberry Pi 5**, com foco em **performance, benchmark e inferência otimizada em CPU/GPU (Vulkan)**.

---

### Estrutura do Projeto

RPi5/v2/
├── convert.py                 # Script para conversão de modelos (PT → ONNX → OpenVINO / NCNN)
├── index.py                   # Inferência padrão com YOLOv8
├── indexGUILess.py             # Inferência sem interface gráfica (headless)
├── run.sh                     # Script principal de execução
├── GUIMode.sh                 # Execução com interface gráfica
├── terminalMode.sh            # Execução via terminal (sem GUI)
├── save.sh                    # Script para salvar logs/resultados
├── setup.sh                   # Script de preparação do ambiente
├── log.txt                    # Log de métricas (FPS, latência, CPU)
├── yolov8n.pt                 # Modelo YOLOv8 original (PyTorch)
├── yolov8n.onnx               # Modelo exportado para ONNX
├── yolov8n_openvino_model/    # Modelo otimizado para OpenVINO
└── yolov8n_ncnn_model/        # Modelo otimizado para NCNN
---

### Requisitos
- Raspberry Pi 5
- Raspberry Pi OS (64-bit) ou Ubuntu
- Python 3.8+
- OpenCV
- Ultralytics YOLOv8
- OpenVINO (para CPU otimizada)
- NCNN + Vulkan (para aceleração gráfica)

