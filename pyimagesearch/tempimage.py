# import the necessary packages
import uuid
import os
 
class TempImage:
	def __init__(self, timestamp,basePath="/media/network/protected/homesurv", ext=".jpg"):
		# construct the file path
		self.path = "{base_path}/{rand}{ext}".format(base_path=basePath,
			rand=timestamp.replace(" ","_"), ext=ext)
 
	def cleanup(self):
		# remove the file
		os.remove(self.path)
		
