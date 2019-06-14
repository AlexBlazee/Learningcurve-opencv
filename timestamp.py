import picamera
import cv2
from subprocess import call
from datetime import datetime
from time import sleep

#OUR file path
filepath = "C:/Users/Royale121/Desktop/lane dec/"

#grabbing present time 
currentTime = datetime.now()
#creating file name for pic 
picTIme = currentTime.strftime("%Y.%m.%d-%H%M%S")
picName = picTime + '.jpg'
completeFilePath = filePath + picName

#Take picture using new filepath
with picamera.Picamera() as camera :
    camera.resolution = (1280,720)
    camera.capture(completeFilePath)
    print("We have taken the picture ")

#Create our stamp variable
timestampMessage = currentTime.strftime("%Y.%m.%d - %H:%M:%S")
# create time stamp command to have executed
timestampCommand = "/usr/bin/convert " + completeFilePath + " -pointsize 36 -fill red \
-annotate +700+650 '" + timestampMessage + "' " + completeFilePath


#Execute the commmand
call([timestampCommand] , shell = True )
print("We have timestamped our picture!")

