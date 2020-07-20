import sys
from src.Camera import Camera
import cv2
class Command:
    def __init__(self):
        self.verbose = False
    def parse(self):
        args = sys.argv
        for i in range(len(args)):
            if args[i] == "-h":
                help()
            elif args[i] == "-t":
                camera = Camera()
                checkboard = (6,9)
                winSize = (5,5)
                print(args)
                camera.Calibration(args[i+1], checkboard, winSize)
                camera.save()
            elif args[i] == "i":
                if not args[i + 1]:
                    raise Exception("need path after -i type -h for more information")
                camera = Camera()
                camera.load()
                img = cv2.imread(args[i + 1])
                camera.imgCamToWorld(img)
    
    def help():
        print("""
            calibration_tool usage
            calibration:
            -t path checkboard dimension window size dimension
            save result in result.txt
            apply calibration on image:
            -i path to image
        """)