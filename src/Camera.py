import numpy as np
import cv2
from src.Io import Io

class Camera:
    def __init__(self):
        self.criteria = None
        self.ThreeDPoints = []
        self.TwoDPoints = []
        self.h = None
        self.w = None
        self.ThreeDpoint = None
        self.TwoDpoint = None
        self.mtx = None
        self.rvecs = None
        self.tvecs = None
        self.dist = None

    def Calibration(self, path, checkboard, winSize = (5, 5)):
        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,  30, 0.001)
        self.ThreeDpoint = np.zeros((1, checkboard[0] * checkboard[1], 3), np.float32)
        self.ThreeDpoint[0,:, :2] = np.mgrid[0:checkboard[0], 0:checkboard[1]].T.reshape(-1, 2)

        images = Io.get_images(path+"*")
        for img in images:
            image = cv2.imread(img)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            refine, corners = cv2.findChessboardCorners(gray, checkboard, cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
            if refine == True:
                self.ThreeDPoints.append(self.ThreeDpoint)
                self.TwoDpoint = cv2.cornerSubPix(gray, corners, (winSize[0] * 2 + 1, winSize[1] * 2), (-1, -1), self.criteria)
                self.TwoDPoints.append(self.TwoDpoint)
        #         image = cv2.drawChessboardCorners(image,checkboard, self.TwoDpoint, refine)
        #         cv2.imshow('image', image)
        #         cv2.waitKey(0)
        # cv2.destroyAllWindows()
        self.h, self.w = image.shape[:2]
        ret, self.mtx, self.dist, self.rvecs, self.tvecs = cv2.calibrateCamera(self.ThreeDPoints, self.TwoDPoints, gray.shape[::-1],None,None)
        return (self.mtx, self.dist, self.rvecs, self.tvecs)

    def imgCamToWorld(self, img):
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(self.mtx, self.dist, (self.w, self.h), 1, (self.w, self.h))
        dst =  cv2.undistort(img, self.mtx, self.dist, newcameramtx)
        cv2.imwrite('calibresult.png', dst)
    def save(self):
        data = (self.mtx, self.tvecs, self.rvecs,  self.dist, self.h, self.w)
      #  print(data)
        Io.write_data_to_file(data)
    def load(self):
      datas = Io.get_data_from_file()
      self.mtx = datas[0]
      self.tvecs = datas[1]
      self.rvecs = datas[2]
      self.dist = datas[3]
      self.h = datas[4]
      self.w = datas[5]
   #   print(self.w)

if "__main__" == __name__:
    checkboard = (6, 9)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,  30, 0.001)
    ThreeDpoint = np.zeros((1, checkboard[0] * checkboard[1], 3), np.float32)
    ThreeDpoint[0,:, :2] = np.mgrid[0:checkboard[0], 0:checkboard[1]].T.reshape(-1, 2)

    print(ThreeDpoint)