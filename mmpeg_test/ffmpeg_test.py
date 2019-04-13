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
input_files = ['cat.mp4']

index = 1
for i in input_files:
    if os.path.exists(path_name+str(index)):
        deletePath(path_name+str(index))

    createPath(path_name+str(index))

    command = 'ffmpeg -i ' + i + ' -qscale:v 2 '+path_name+str(index)+'/frame%03d.jpg'
    subprocess.call(command, shell=True)

    index += 1
