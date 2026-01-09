from ultralytics import YOLO
model = YOLO('yolov8n.pt')
# cria a pasta 'yolov8n_ncnn_model' com suporte a Vulkan
model.export(format='ncnn', imgsz=640, half=True)
