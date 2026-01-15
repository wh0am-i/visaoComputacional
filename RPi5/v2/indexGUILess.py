import cv2
import time
import numpy as np
import psutil
from ultralytics import YOLO
from flask import Flask, Response

app = Flask(__name__)

# Configurações do Modelo
model = YOLO('yolov8n_ncnn_model/', task='detect')
cap = cv2.VideoCapture(0)

# Variáveis de Log e FPS
prevTime = 0
logFps, logInference, logLatency, logCPU = [], [], [], []

def generate_frames():
    global prevTime
    while cap.isOpened():
        startCycle = time.time()
        success, frame = cap.read()
        
        if not success:
            break
        
        # Inferência
        results = model.predict(frame, imgsz=640, half=True, verbose=False)
        
        # Métricas
        infTime = results[0].speed['inference']
        logInference.append(infTime)
        
        currentTime = time.time()
        timeDiff = currentTime - prevTime
        fps = 1 / timeDiff if timeDiff > 0 else 0
        prevTime = currentTime
        
        logFps.append(fps)
        logLatency.append((currentTime - startCycle) * 1000)
        logCPU.append(psutil.cpu_percent())

        # Anotação do Frame
        annotatedFrame = results[0].plot()
        text = f"FPS: {fps:.2f}"
        font, fontScale, thickness = cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2
        pos = (5, 20)
        
        (w, h), baseline = cv2.getTextSize(text, font, fontScale, thickness)
        cv2.rectangle(annotatedFrame, (pos[0] - 5, pos[1] - h - 5), 
                      (pos[0] + w + 5, pos[1] + baseline + 5), (0, 0, 0), -1)
        cv2.putText(annotatedFrame, text, pos, font, fontScale, (0, 255, 0), thickness)

        # Redimensionamento
        annotatedFrame = cv2.resize(annotatedFrame, (0, 0), fx=1.3, fy=1.3)
        
        # Encode para JPG para o Stream
        ret, buffer = cv2.imencode('.jpg', annotatedFrame)
        frame_bytes = buffer.tobytes()
        
        # Formato de stream MJPEG
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    # Página simples para visualizar o vídeo
    return '<html><body><h1>YOLOv8 Stream</h1><img src="/video_feed" width="800"></body></html>'

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    try:
        # Inicia o servidor no seu IP e porta 8080
        app.run(host='10.0.0.110', port=8080, threaded=True)
    except KeyboardInterrupt:
        pass
    finally:
        # Salva os logs ao fechar
        cap.release()
        if logFps:
            avgFps, avgInf = np.mean(logFps), np.mean(logInference)
            avgLat, avgCPU = np.mean(logLatency), np.mean(logCPU)
            with open("log.txt", "w") as f:
                f.write(f"FPS Medio: {avgFps:.2f}\nInferencia Media: {avgInf:.2f} ms\n")
            print(f"\nStream encerrado. Log salvo. FPS Médio: {avgFps:.2f}")