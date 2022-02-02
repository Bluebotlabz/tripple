# Import os and stuff
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup

# List files in current folder
files = [f for f in listdir("./") if isfile(join("./", f))]

# Get files
for fileName in files:
    # Open file
    with open("./" + fileName, "r", encoding="utf8") as file:
        try:
            # Read content
            content = file.read()
            # Initialise BS4
            soup = BeautifulSoup(content, "html.parser")
            # remove certain elements
            for script in soup(["script", "style", "noscript", "a"]):
                script.decompose()
            
            foundInFile = False
            for line in soup:
                if(str(line).find("<h1>") != -1):
                    foundInFile = True
            if foundInFile and ".html" in fileName:
                print(fileName)
        except Exception as e:
            pass
