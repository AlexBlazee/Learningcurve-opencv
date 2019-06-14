import numpy as np
import cv2

img = cv2.imread('images.jpg',0)

##res = cv2.resize(img , None , fx = 2 , fy = 2 , interpolation = cv2.INTER_CUBIC)
##cv2.imshow('res', res )
##rese = cv2.resize(img , None , fx = 2 , fy = 2 , interpolation = cv2.INTER_AREA)
##resc = cv2.resize(img , None , fx = 2 , fy = 2 , interpolation = cv2.INTER_LINEAR)
##cv2.imshow('rese', rese )
##cv2.imshow('resc', resc )


##
##rows,cols = img.shape
##
##M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
##dst = cv2.warpAffine(img,M,(cols,rows))
##cv2.imshow('dst',dst)

