import subprocess

#get all files into filelist
subprocess.run(["ls | grep '.HEIC' > files.txt"], shell=True)
files = open("files.txt", "r")
fileList = files.read().split(".HEIC\n")

for str in fileList:
	if (str):
		subprocess.run(["heif-convert " + str + ".HEIC " + str + ".jpg"], shell=True)

subprocess.run(["rm *.HEIC"], shell=True)
