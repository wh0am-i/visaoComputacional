from ultralytics import YOLO

model = YOLO("../models/yolov8n.pt")

model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    device=0,
    workers=8,
    name="yolov8n_finetune",
    pretrained=True
)
