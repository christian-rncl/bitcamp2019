import subprocess
import os
from shutil import rmtree

def createPath(s):
    #assert (not os.path.exists(s)), "The filepath "+s+" already exists. Don't want to overwrite it. Aborting."

    try:  
        os.mkdir(s)
    except OSError:  
        assert False, "Creation of the directory %s failed."

def deletePath(s):
    try:  
        rmtree(s,ignore_errors=False)
    except OSError:  
        print ("Deletion of the directory %s failed" % s)
        print(OSError)

path_name = 'frames'
input_file = 'cat.mp4'

if os.path.exists(path_name):
    deletePath(path_name)

createPath(path_name)

command = 'ffmpeg -i ' + input_file + ' -qscale:v 2 frames/frame%03d.jpg'
subprocess.call(command, shell=True)
