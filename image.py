import cv2
import numpy as np
print("Enter 1 to make a low resolution image to high resolution image")
print("Enter 2 to make a high resolution image to low resolution image")
value=int(input())
if(value==1):
    image=cv2.imread("C:\\Users\\ahpat\\OneDrive\\Pictures\\Screenshots\\flower.jpg")
    cv2.imshow("original image",image)
    uwidth=1080
    uheight=4000
    upoints=(uwidth,uheight)
    uresized=cv2.resize(image,upoints,interpolation=cv2.INTER_LINEAR)
    cv2.imshow("UpScale Resized Image",uresized)
    cv2.waitkey()
    cv2.destroyAllWindows()
else:
    image=cv2.imread("C:\\Users\\ahpat\\OneDrive\\Pictures\\Screenshots\\flower.jpg")
    cv2.imshow("original image",image)
    dwidth=480
    dheight=720
    dpoints=(dwidth,dheight)
    dresized=cv2.resize(image,dpoints,interpolation=cv2.INTER_LINEAR)
    cv2.imshow("DownScale  Resized Image",dresized)
    cv2.waitkey()
    cv2.destroyAllWindows()
    
    

