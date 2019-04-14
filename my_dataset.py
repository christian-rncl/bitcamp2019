from torch.utils.data.dataset import Dataset
import numpy as np
import torch
import os
import txt
import subprocess


class Sign:
    def __init__(self, signdir, label, transforms=None):
        frames = []
        subprocess.run(['python', 'txt.py', 'image_dir', 'signdir'])
        for i in range(1, 31):
            ff = os.path.join(signdir, 'frame{:03d}.jpg.txt'.format(i))
            frame = torch.from_numpy(np.loadtxt(ff))
            frames.append(frame)
        self. label = label
        self.transforms = transforms
        print('frames:\n' + str(frames))


class MyCustomDataset(Dataset):
    signs = []

    def __init__(self, dir):
        iterdir = iter(os.walk(dir))
        next(iterdir)

        signs = [Sign(x[0], os.path.basename(x[0])) for x in iterdir]

    def __getitem__(self, index):
        return self.signs[index]

    def __len__(self):
        return len(self.signs)
