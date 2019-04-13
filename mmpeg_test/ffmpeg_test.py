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



for filename in os.listdir('test_data'):
    path_name = filename + '_frames'
    if os.path.exists(path_name):
        deletePath(path_name)

    createPath(path_name)

    command = 'ffmpeg -i ' + i + ' -qscale:v 2 ' + path_name + '/frame%03d.jpg'
    subprocess.call(command, shell=True)
