import cv2
import numpy as np
import time

FPS = 10
prev_time = 0


# 웹캠 신호 받기
#VideoSignal = cv2.VideoCapture(1)

#이미지 가져오기
img = cv2.imread("46412.jpg")
img = cv2.resize(img, None, fx=1., fy=1.)
height, width, channels = img.shape

'''
네트워크에서 이미지를 바로 사용할 수 없기때문에 먼저 이미지를 Blob으로 변환해야 한다.
YOLO가 허용하는 세가지 크기
320 × 320 : 작고 정확도는 떨어지지 만 속도 빠름
609 × 609 : 정확도는 더 높지만 속도 느림
416 × 416 : 중간
Blob은 이미지에서 특징을 잡아내고 크기를 조정하는데 사용된다.
'''

# YOLO 가중치 파일과 CFG 파일 로드
YOLO_net = cv2.dnn.readNet("yolov2-tiny.weights","yolov2-tiny.cfg")

# YOLO NETWORK 재구성
classes = []
with open("yolo.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = YOLO_net.getLayerNames()

'''
아래 코드를 사용하면 에러가 발생함. layer_names안에 인텍스 처리가 파이썬에서 잘못됐다고 나옴. 
output_layers = [layer_names[i[0] - 1] for i in YOLO_net.getUnconnectedOutLayers()]
'''
output_layers = [layer_names[i - 1] for i in YOLO_net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes),3))

# YOLO 입력
# detecting objects
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
YOLO_net.setInput(blob)
outs = YOLO_net.forward(output_layers)

class_ids = []
confidences = []
boxes = []

for out in outs:

    for detection in out:

        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        #신뢰도가 0.5 이상이라면 물체가 정확이 감지되었다고 간주한다.
        if confidence > 0.5:
            # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            dw = int(detection[2] * width)
            dh = int(detection[3] * height)
            # Rectangle coordinate
            x = int(center_x - dw / 2)
            y = int(center_y - dh / 2)
            boxes.append([x, y, dw, dh])
            confidences.append(float(confidence))
            class_ids.append(class_id)

        #노이즈 제거
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.45, 0.4)

        font = cv2.FONT_HERSHEY_PLAIN
       
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                score = confidences[i]

                # 경계상자와 클래스 정보 이미지에 입력
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, label, (x, y + 30), font, 3, color, 3)

        cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
