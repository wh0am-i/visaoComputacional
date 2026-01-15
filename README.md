#  Visão Computacional – YOLOv8

Projeto de **visão computacional em tempo real** utilizando **YOLOv8**, focado em **benchmark, inferência otimizada e comparação de hardware embarcado**.

Este repositório reúne implementações do mesmo pipeline em diferentes placas para **análise de desempenho, consumo e viabilidade de Edge AI**.

---

##  Plataformas suportadas

###  NVIDIA Jetson Nano
Implementação utilizando **TensorRT + Docker NVIDIA** 

📁 Local:
jetsonNano/

📄 README:
jetsonNano/README.md

---

###  Raspberry Pi 5
Implementação utilizando **PyTorch, ONNX, OpenVINO e NCNN** para benchmark em ARM.

📁 Local:
RPi5/v2/

📄 README:
RPi5/v2/README.md


---

##  Objetivo do projeto

- Executar **YOLOv8 em tempo real** em hardware de baixo consumo  
- Comparar:
  - FPS  
  - Latência  
  - Uso de CPU/GPU  
- Avaliar:
  - PyTorch vs ONNX vs TensorRT vs OpenVINO vs NCNN  

---

##  Estrutura geral

visaoComputacional/ <br>
├── jetsonNano/ # Implementação NVIDIA (TensorRT, Docker) <br>
└── RPi5/ # Implementação Raspberry Pi <br>


Cada plataforma possui seu próprio README com instruções de uso, instalação e benchmark.






