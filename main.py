from src.Camera import Camera
import cv2

if "__main__" == __name__:
    c = Camera()
    c.Calibration("images/", (6,9))
    img = cv2.imread('new_calibration_image.png')
    c.imgCamToWorld(img)