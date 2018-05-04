import os
import requests

state = "Alpha"
version = 1.0
fullVersion = state + " " + str(version)

def checkDir(path, dirname):
    dir_ = os.listdir(path)
    if dirname in dir_:
        return False
    return True

print("Python Project Manager", fullVersion, "(Linux, tested on Lubuntu)\n")
print("Currently doesn't support large python projects with frameworks (for example Django projects).")
print("NOTE THAT IF YOU DO NOT SPECIFY HTTPS THE PROGRAM WILL USE HTTP")
print("Please enter the URL for a RAW file containing the code.")

url = input(": ")
if not url.startswith("http"):
    url = "http://" +  url

name = input("Please name the package (When adding spaces, please add \\'s).")
fullPath = "usr/share/" + name
if not name.endswith(".py"):
    fileName = name + ".py"

print("Downloading file...")
fullFile = requests.get(url)
file_ = fullFile.text


if checkDir("/usr/share/", name):
    os.chdir("/usr/share/")
    os.mkdir(name)
    os.chdir(fullPath)
    with open(fileName, "w") as pyFile:
        pyFile.write(file_)

else:
    print("The directory already exists.")


