import os
import requests
import time

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
fullPath = "/usr/share/" + name + "/"
shortcutName = name + ".sh"
desktopPath = "~/Desktop/" + shortcutName

if not name.endswith(".py"):
    fileName = name + ".py"

print("Downloading file...\n0% ||||||||||", end="")
fullFile = requests.get(url)
file_ = fullFile.text
print("Downloaded file.\n25% ///|||||||", end="")

if not os.path.exists(fullPath) and not os.path.exists(desktopPath):
    os.chdir("/usr/share/")
    print("Making Directory\n25% ///|||||||", end="")
    os.makedirs(name)
    print("Made Directory\n50% /////|||||", end="")
    os.chdir(name)
    print("Dropping file...\n50% /////|||||")
    with open(fileName, "w") as pyFile:
        pyFile.write(file_)
    print("Dropped file.\n75% ////////||")

    os.chdir("~/Desktop/")
    print("Writing shortcut...\n75% ////////||")
    with open(fileName, "w") as shFile:
        shFile.write("python3 " + fullPath + """
        exit""")
    print("Complete!")
    

else:
    print("The directory already exists.")


