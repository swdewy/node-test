import cv2

# image
img = cv2.imread('ss.jpg')
cv2.imshow('image', img)
cv2.waitKey()

'''
# video and webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, img = cap.read()
    if not success:
        continue

    cv2.imshow('image', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
'''