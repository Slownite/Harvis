import glob
import pathlib

class Io:

	def __init__(self):
		pass

	def get_images(path : str) -> list:
		d = glob.glob(path)
		if len(d) == 0:
			raise Exception("path does not exist.")
		return d

	def write_data_to_file(self, data : tuple, path : str ="results.txt"):
		result_file = open(path, 'w')
		result_file.write("mtx : " + str(data[0]))
		result_file.close()

#b = Io()
#i = b.get_images("./*.py")
#b.write_data_to_file(({'x': 0, 'y': 0, 'z': 0}, {}))