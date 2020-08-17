import cv2

def draw_boxes (image , cordonnate ) :

    (x,y ,w , h) = cordonnate

    color = (255,0,0)
    thickness = 2


    cv2.rectangle( image , (x,y) , (x+w , y+h) , color= color , thickness= thickness)

    cv2.VideoCapture

