import airsim
import cv2
import numpy as np
import torch

client = airsim.MultirotorClient()
client.confirmConnection()

main_window_name = "Shidqi work"
cv2.namedWindow(main_window_name, cv2.WINDOW_NORMAL)

cv2.resizeWindow(main_window_name, 1280, 720)

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

target_labels = ['car', 'person']

print("Mulai deteksi... Tekan 'q' untuk keluar.")

while True:
    responses = client.simGetImages([
        airsim.ImageRequest("FrontCenterRGB", airsim.ImageType.Scene, False, False)
    ])
    
    if responses[0].height == 0 or responses[0].width == 0:
        print("gagal")
        continue

    img1d = np.frombuffer(responses[0].image_data_uint8, dtype=np.uint8)
    img_rgb = img1d.reshape(responses[0].height, responses[0].width, 3).copy()

    results = model(img_rgb)

    df = results.pandas().xyxy[0]

    for _, row in df.iterrows():
        label = row['name']
        if label in target_labels:
            x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
            conf = row['confidence']

            if label == 'car':
                color = (0, 0, 255)   # merah (BGR)
            elif label == 'person':
                color = (255, 0, 0)   # biru (BGR)
            else:
                color = (0, 255, 0)   # hijau 

            cv2.rectangle(img_rgb, (x1, y1), (x2, y2), color, 2)
            cv2.putText(img_rgb, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    
    cv2.imshow(main_window_name, img_rgb) 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()