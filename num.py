from ultralytics import YOLO
import cv2

model = YOLO("/home/ubuntu/Downloads/best.pt")
model.predict(source = '/home/ubuntu/Desktop/2 Wheel Test-20230220T081215Z-001/2 Wheel Test/', show = True, save_crop = True, save=True)
cv2.waitKey(0)