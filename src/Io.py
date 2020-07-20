import glob
import pathlib
import json
import numpy as np
import pickle

class Io:
    def __init__(self):
        pass

    @staticmethod
    def get_images(path : str) -> list:
        d = glob.glob(path)
        if len(d) == 0:
            raise Exception("Path does not exist.")
        return d

    @staticmethod
    def write_data_to_file(data : tuple, path : str ="results.npy"):
        np.save(path, data)

    @staticmethod
    def get_data_from_file(path : str = "results.npy") -> list:
        a = np.load(path)
        return a


if __name__ == "__main__":
    ar = np.array([1, 2, 3])
    sec_arr = np.array([[1, 2, 3], [0, 5, 8]])
    b = Io()
    i = b.get_images("./*.py")
    b.write_data_to_file((ar, sec_arr, [np.array([[ 5.7347458 ],
       [-2.70714913],
       [14.02886978]]), np.array([[ 5.09454526],
       [-2.62515634],
       [14.86642347]]), np.array([[ 3.05927455],
       [-2.48136364],
       [ 9.46724591]])]))
    a = b.get_data_from_file()
    print(a)