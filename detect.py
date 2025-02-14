import cv2
face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if face.empty():
    print("Haarcascade file not found!")
    exit()

image = cv2.imread(r"C:\Users\91861\OneDrive\Desktop\others\hero.png")

if image is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(r"C:\Users\91861\OneDrive\Desktop\others\hero.png",image)
print("Face detected properly.")