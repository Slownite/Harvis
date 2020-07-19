import glob
import pathlib
import json

class Io:

	def __init__(self):
		pass

	def get_images(self, path : str) -> list:
		d = glob.glob(path)
		if len(d) == 0:
			raise Exception("Path does not exist.")
		return d

	def write_data_to_file(self, data : tuple, path : str ="results.txt"):
		result_file = open(path, 'w')
		for var in data:
			result_file.write(json.dumps(var) + '\n')
		result_file.close()

	def get_data_from_file(self, path : str = "results.txt") -> list:
		a = []
		result_file = open(path, 'r')
		for line in result_file:
			a.append(json.loads(line.strip('\n')))
		result_file.close()
		return a

#b = Io()
#i = b.get_images("./*.py")
#b.write_data_to_file(( [{"x": 0, "y": 0, "z": 0}, {'z': -1}],  ["o", 9],  [[1, 2, 3], [0, 5]] ))
#a = b.get_data_from_file()
#print(a)