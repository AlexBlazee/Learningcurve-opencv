import numpy as np
import cv2
import matplotlib.pyplot as  plt

# image input 
''''
img = cv2.imread('images.jpg',0)
cv2.imshow('img',img)
plt.imshow(img , cmap = 'gray' , interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
'''

# vidoe input

cap = cv2.VideoCapture(0)

while(True):
    # capture the frame by frame 
    ret , frame = cap.read()

    # converting to gray scale
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





'''
k = cv2.waitKey(0) & 0xFF
if k == 27 :
    cv2.destroyAllWindows()
elif k == ord('s') :
    cv2.imwrite('img.png',img)
    cv2.destroyAllWindows()
'''

                        
