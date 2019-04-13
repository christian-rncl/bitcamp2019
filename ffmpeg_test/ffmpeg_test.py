import subprocess
import os

def createPath(s):
    try:  
        os.mkdir(s)
    except OSError:  
        assert False, "Creation of the directory %s failed."

for filename in os.listdir('test_data/on'):
    path_name = 'test_data_frames/on/' + filename

    if not os.path.exists(path_name):
        createPath(path_name)

        command = 'ffmpeg -i test_data/on/' + filename + ' -qscale:v 2 ' + path_name + '/%04d.jpg'
        subprocess.call(command, shell=True)

for filename in os.listdir('test_data/off'):
    path_name = 'test_data_frames/off/' + filename

    if not os.path.exists(path_name):
        createPath(path_name)

        command = 'ffmpeg -i test_data/off/' + filename + ' -qscale:v 2 ' + path_name + '/%04d.jpg'
        subprocess.call(command, shell=True)

for filename in os.listdir('test_data/up'):
    path_name = 'test_data_frames/up/' + filename

    if not os.path.exists(path_name):
        createPath(path_name)

        command = 'ffmpeg -i test_data/up/' + filename + ' -qscale:v 2 ' + path_name + '/%04d.jpg'
        subprocess.call(command, shell=True)

for filename in os.listdir('test_data/down'):
    path_name = 'test_data_frames/down/' + filename

    if not os.path.exists(path_name):
        createPath(path_name)

        command = 'ffmpeg -i test_data/down/' + filename + ' -qscale:v 2 ' + path_name + '/%04d.jpg'
        subprocess.call(command, shell=True)

for filename in os.listdir('test_data/music_on'):
    path_name = 'test_data_frames/music_on/' + filename

    if not os.path.exists(path_name):
        createPath(path_name)

        command = 'ffmpeg -i test_data/music_on/' + filename + ' -qscale:v 2 ' + path_name + '/%04d.jpg'
        subprocess.call(command, shell=True)