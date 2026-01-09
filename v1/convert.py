from ultralytics import YOLO
model = YOLO('yolov8n.pt')
# Isso cria a pasta 'yolov8n_ncnn_model' com suporte a Vulkan
model.export(format='ncnn', half=True)
