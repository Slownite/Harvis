import sys
from src.Camera import Camera
import cv2
class Command:
    def __init__(self):
        self.verbose = false
    def parse(self):
        args = sys.argv
        args.pop()
        for i in args:
            if arg[i] == "-h":
                help()
            else if args[i] == "-t":
                if not args[i + 1]:
                    raise Exception("need path after -t type -h for more information")
                if not args[i + 2]:
                    raise Exception("need the checkboard size (x, y) after the path")
                if not args[i + 3]:
                    raise Exception("need the window size size (x, y) after the checkboard dimension")
                camera = Camera()
                checkboard = tuple(map(int, args[i+2].split(', ')))
                winSize = tuple(map(int, args[i+3].split(', ')))
                camera.Calibration(args[i+1], checkboard, winSize)
                camera.save()
            else if args[i] == "i"
                if not args[i + 1]:
                    raise Exception("need path after -i type -h for more information")
                camera = Camera()
                camera.load()
                img = cv2.imread(args[i + 1])
                camera.imgCamToWorld(img)
    
    def help():
        print("""
            
        """)