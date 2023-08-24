from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
results = model.train(data="D:\Program Code\microbubble\code\Program\config.yaml", epochs=1)  # train the model