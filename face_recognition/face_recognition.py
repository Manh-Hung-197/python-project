import cv2
import dlib 

img = cv2.imread("backpink.jpg") #cho hinh anh vao

#chuyen sang mau den/trang
gray = cv2.cvtColor(src = img, code = cv2.COLOR_BGR2GRAY)

#su dung thu vien dlib de load face reconition
face_detector = dlib.get_frontal_face_detector()

#tim khuon mat
faces = face_detector(gray)
#print(len(faces))

for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()

    #ve duong vien xung quanh mat
    cv2.rectangle(img = img, pt1 = (x1, y1), pt2 = (x2, y2), color = (0, 255, 0), thickness= 1)

#show
cv2.imshow(winname = "face Recognition App", mat = img)

cv2.waitKey(delay = 0) #dung key bat ki de exit

cv2.destroyAllWindows()