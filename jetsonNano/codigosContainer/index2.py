import cv2
from ultralytics import YOLO

# CARREGUE A PASTA EXPORTADA, NÃO O ARQUIVO .PT
model = YOLO('yolov8n.engine', task='detect')

cap = cv2.VideoCapture(0)
soma=0
count=0
while cap.isOpened():
    success, frame = cap.read()
    if success:
        # Aqui está o segredo: para ncnn, device='cpu' usa NEON (CPU) 
        # e ncnn com suporte interno usará a GPU se detectada.
        # No Ultralytics + ncnn, ele tenta usar Vulkan automaticamente se disponível.
        results = model.predict(frame, imgsz=640, half=True, verbose=False)

        soma += results[0].speed["inference"]+results[0].speed["preprocess"]+results[0].speed["postprocess"]
        count+=1
        cv2.imshow("RPi5 GPU+CPU", results[0].plot())
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
print(count/(soma/1000))
cap.release()
cv2.destroyAllWindows()
