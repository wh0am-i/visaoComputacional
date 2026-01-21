from ultralytics import YOLO

model = YOLO("../models/yolov8n.pt")

model.train(
    data="../data.yaml",
    epochs=2,
    imgsz=640,
    batch=4,
    device='cpu',
    workers=8,
    name="yolov8n_finetune",
    pretrained=True,
    classes=[0, 1, 2, 3]
)
