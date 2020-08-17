import cv2
cap = cv2.VideoCapture(0)
videocap = cv2.VideoCapture("Recording #7.mp4")
dir_path = "Known faces"
count = 0
while True :
    ret , frame = videocap.read()



    im_path = dir_path + str(count ) +'.png'
    im = cv2.imwrite(im_path, frame)
    count += 1

    cv2.putText(frame, str(count) , (50,50) , cv2.FONT_HERSHEY_COMPLEX ,1, (255,0,0) , 2 )
    cv2.imshow('smiiiiiiiiiiiiiiiiiiiiiiile' , frame)

    if cv2.waitKey(20) & 0xFF == ord('q')  :
        break



