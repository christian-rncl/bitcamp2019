import subprocess
import os
from shutil import rmtree

def createPath(s):
    #assert (not os.path.exists(s)), "The filepath "+s+" already exists. Don't want to overwrite it. Aborting."

    try:  
        os.mkdir(s)
    except OSError:  
        assert False, "Creation of the directory %s failed."


for filename in os.listdir('test_data'):
    path_name = 'test_data_frames/' + filename + '_frames'

    if not os.path.exists(path_name):
        createPath(path_name)

        command = 'ffmpeg -i test_data/' + filename + ' -qscale:v 2 ' + path_name + '/frame%03d.jpg'
        subprocess.call(command, shell=True)
