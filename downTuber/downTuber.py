#!/usr/bin/python
# -*- coding: utf-8 -*-

# Enable unicode and stuff
from __future__ import unicode_literals
# Import YouTube "scraper"
import pafy
# Import video downloader
import youtube_dl
# Import OS and shutil
import os
# Import time
import time
# Import CGI library
import cgi, cgitb
# Import random library
import random
# Import sys
import sys

print("Content-type:text/html\r\n\r\n")

debug = False
version = "0.0.1"

if(int(version[0]) < 1):
    print("TST-" + version)

os.system("export LANG=en_US.UTF-8")

cgitb.enable(display=0, logdir="../../logs/")
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
try:
    URL = form.getvalue('URL')
except:
    sys.exit(1)

try:
    audioOnly  = bool(int(form.getvalue('audioOnly')))
except:
    audioOnly = False

if(debug):
    print("\n\n-----------------------------------")
    print("             Copyright             |")
    print("|     Bluebotlaboratories 2020     |")
    print("|       Downtuber    v" + version +"        |")
    print("-----------------------------------")

def pasteURL(event):
    try:
        if(debug):
            print("pasting")
        
        data = clipboard.paste()

        if("https://www.youtube.com/watch?v=" in data):
            if(debug):
                print("Clipboard is YouTube")
            videoUrl.delete(0, END)
            videoUrl.insert(0, str(data))
    except:
        if(debug):
            print(sys.exc_info()[1])

class callbacks(object):
    def __init__(self, video):
        self.video = video
    
    def debug(self, msg):
        global videos
        info = msg.split()

        if("[download]" in info):
            print("\r")
            # Set table
            if("ETA" in info):
                print("<script>")
                print("  document.getElementById(\"progress\").innerHTML = \"" + self.video.title.encode("ascii","ignore") + " | " + str(info[1]) + " - " + str(info[7]) +"\";")
                print("</script>")

                if(debug):
                    print(self.video.title.encode("ascii","ignore") + " | " + str(info[1]) + " - " + str(info[7]))
            else:
                if(debug):
                    print(self.video.title.encode("ascii","ignore") + " | " + str(info[1]), " - N/A\r")

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        if(debug):
            print("Error:")
            print(msg)

def progressHook(stats):
    if(debug):
        if stats["status"] == "finished":
            if(debug):
                print("Download complete!")

def downloadVideo(URL, downloadLocation, audioOnly = False):    
    global videos
    global downloading

    try:
        video = pafy.new(URL)
    except:
        return(-1, "./videoCache/")


    # Set options
    videoFile = u'' + video.title.encode("ascii", "ignore").replace('\\', '').replace('/', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
    if(audioOnly):
        videoFormat = "mp3"
    else:
        videoFormat = video.getbest().extension
    videoFormat = video.getbest().extension
    actualVideoFile = downloadLocation + videoFile + "." + videoFormat

    if(os.path.isfile(actualVideoFile) and audioOnly != True):
        return(0, actualVideoFile)
    
    if(audioOnly):
        ydl_opts = {
            "format": "best",
            "outtmpl": actualVideoFile,
            "logger": callbacks(video),
            "progress_hooks": [progressHook],
            'ffmpeg_location': './ffmpeg/',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
        
    else:
        ydl_opts = {
            "format": "best",
            "outtmpl": actualVideoFile,
            "logger": callbacks(video),
            "progress_hooks": [progressHook],
            'ffmpeg_location': './ffmpeg/'
        }

    # Download
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])

    # Change button image
    
    return(0, actualVideoFile)


#URL = input("Enter URL >>> ")
#random.seed(time.time())
#downloadLocation = "./" + str(random.randint(-sys.maxsize - 1, sys.maxsize)) + "/"


downloadLocation = "./videoCache/"

print("<html>")
print("  <head>")
print("    <title>Bluebotlaboratories - downtuber</title>")
print("  </head>")
print("  <body>")
print("    <p>Downloading video...</p>")
print("    <p id=\"progress\"></p>")

try:
    output = downloadVideo(URL, downloadLocation, audioOnly)

    if(output[0] == 0):
        print("<script>window.location = \"https://www.bluebotlaboratories.com/downTuber/" + output[1].replace("./", "") + "\";</script>")
        #print("    <meta http-equiv=\"refresh\" content=\"0;url=https://www.bluebotlaboratories.com/downTuber/" + output[1].replace("./", "") +  "/>")
        print(output[1])
    elif(output[0] == -1):
        print("Error: invalid URL")
        print(sys.exc_info)

except Exception as error:
    print("Error: BIG BOI ERROR, msg below for admins and stuff")
    print(error)
    print(sys.exc_info())

#print("    <a href=\"https://www.bluebotlaboratories.com/reviewthing/review\">Click here if you are not redirected</a>")
print("  </body>")
print("</html>")
