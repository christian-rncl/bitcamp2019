import subprocess

input_file = 'cat.mp4'

command = 'ffmpeg -i ' + input_file + ' -qscale:v 2 frame%06d.jpg'
subprocess.call(command, shell=True)
