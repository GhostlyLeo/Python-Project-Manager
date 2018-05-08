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

name = input("Please name the package (When adding spaces, please add \\'s).") # Name for the app
fullPath = "/usr/share/" + name + "/" # The full path to the dir of the app
shortcutName = name + ".desktop" # The name for the shortcut
desktopPath = "~"

if not name.endswith(".py"):
    fileName = name + ".py"

# THIS IS THE SHORTCUT CONTENT
shortcutContent = """[Desktop Entry]
Name=""" + name + """
Comment=Installed via Python Package Manager
Exec=python3 /usr/share/""" + name + "/" + fileName + """
Terminal=true
Type=Application
"""

os.system("clear") # All os.system("clear")'s means that I clear the terminal so it looks nicer.
print("\nDownloading file...\n0% ||||||||||", end="")
fullFile = requests.get(url) # Get the info from the URL.
file_ = fullFile.text # Get the contents from the URL
os.system("clear") # Clear
print("\nDownloaded file.\n25% ///|||||||", end="")

if not os.path.exists(fullPath): 
    os.chdir("/usr/share/") # Change directory to /usr/share
    os.system("clear")
    print("\nMaking Directory\n25% ///|||||||", end="")
    os.makedirs(name) # Make a directory called the input you inputted before
    os.system("clear")
    print("\nMade Directory\n50% /////|||||", end="")
    os.chdir(name) # Change directory to that file
    os.system("clear")
    print("\nDropping file...\n50% /////|||||", end="")
    with open(fileName, "w") as pyFile: # Create a new .py file
        pyFile.write(file_) # Write the info to that new .py file
    os.system("clear") 
    print("\nDropped file.\n75% ////////||", end="")

    os.chdir(os.path.expanduser("~")) # Change directory to the home directory
    os.chdir("Desktop") # Change directory to the desktop directory
    os.system("clear")
    print("\nWriting shortcut...\n75% ////////||", end="")
    with open(shortcutName, "w") as shFile: # Write the shortcut using the content from above.
        shFile.write(shortcutContent)
    os.system("clear")
    print("\rComplete! 100% //////////") # Done!
else:
    print("The directory already exists.")


