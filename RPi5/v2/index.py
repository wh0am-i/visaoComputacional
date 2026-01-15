import cv2
import time
import numpy as np
import psutil
from ultralytics import YOLO

model = YOLO('yolov8n.engine', task='detect')
cap = cv2.VideoCapture(0)

prevTime = 0
fps = 0

logFps = []
logInference = []
logLatency = []
logCPU = []

while cap.isOpened():
    startCycle = time.time()
    success, frame = cap.read()
    
    if success:
        results = model.predict(frame, imgsz=640, half=True, verbose=False)
        
        infTime = results[0].speed['inference']
        logInference.append(infTime)
        
        currentTime = time.time()
        timeDiff = currentTime - prevTime
        if timeDiff > 0:
            fps = 1 / timeDiff
        prevTime = currentTime
        
        logFps.append(fps)
        logLatency.append((currentTime - startCycle) * 1000)
        logCPU.append(psutil.cpu_percent())

        annotatedFrame = results[0].plot()
        
        text = f"FPS: {fps:.2f}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 0.6
        thickness = 2
        textColor = (0, 255, 0)      # verde
        bgColor = (0, 0, 0)         # preto
        pos = (5, 20)                # posição x e y
        
        (w, h), baseline = cv2.getTextSize(text, font, fontScale, thickness) # calcula o tamanho do texto para o backframe
        
        cv2.rectangle(annotatedFrame,(pos[0] - 5, pos[1] - h - 5), (pos[0] + w + 5, pos[1] + baseline + 5), bgColor, -1)

        cv2.putText(annotatedFrame, text, pos, font, fontScale, textColor, thickness) # plota o fps

        annotatedFrame = cv2.resize(annotatedFrame, (0, 0), fx=1.3, fy=1.3) # redimensionamento
        cv2.imshow("RPi5 GPU+CPU", annotatedFrame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()

if logFps:
    avgFps = np.mean(logFps)
    avgInf = np.mean(logInference)
    avgLat = np.mean(logLatency)
    avgCPU = np.mean(logCPU)
    
    with open("log.txt", "w") as f:
        f.write(f"FPS Medio: {avgFps:.2f}\n")
        f.write(f"Inferencia Media: {avgInf:.2f} ms\n")
        f.write(f"Latencia Media: {avgLat:.2f} ms\n")
        f.write(f"Uso CPU Medio: {avgCPU:.2f}%\n")
    
    print(f"\nFPS Medio: {avgFps:.2f}")
    print(f"Inferencia Media: {avgInf:.2f} ms")
    print(f"Latencia Media: {avgLat:.2f} ms")
    print(f"Uso CPU Medio: {avgCPU:.2f}%")
