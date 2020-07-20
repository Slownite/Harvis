import glob
import pathlib
import json
import numpy as np

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
	def write_data_to_file(data : tuple, path : str ="results.txt"):
		result_file = open(path, 'w')
		for var in data:
			if type(var) is np.ndarray:
				var = var.tolist()
			result_file.write(json.dumps(var) + '\n')
		result_file.close()

	@staticmethod
	def get_data_from_file(path : str = "results.txt") -> list:
		a = []
		result_file = open(path, 'r')
		for line in result_file:
			a.append(json.loads(line.strip('\n')))
		result_file.close()
		return a


if __name__ == "__main__":
	ar = np.array([1, 2, 3])
	sec_arr = np.array([[1, 2, 3], [0, 5, 8]])
	b = Io()
	i = b.get_images("./*.py")
	b.write_data_to_file((ar, sec_arr, [1, 2, 3], {'Ok': 1, 'oook': 9}))
	a = b.get_data_from_file()
	print(a)