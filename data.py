from torch.utils.data import DataLoader, Dataset
import numpy as np
import torch
import os
import subprocess
from sklearn.model_selection import train_test_split
import re



class Sign:
    def __init__(self, signdir, label, transforms=None):
        frames = []
        # print(signdir)
        # subprocess.run(['python', 'txt.py', '--image_dir', signdir])
        for i in range(1, len(os.listdir(signdir))):
            # print('{:04d}.jpg'.format(i))
            if (not os.path.isfile(os.path.join(signdir,'{:04d}.jpg'.format(i)))):
                break
                # pass
            ff = os.path.join(signdir, '{:04d}.jpg.txt'.format(i))
            frame = torch.from_numpy(np.loadtxt(ff))
            # print(frame)
            frames.append(frame)
            
        self.label = label
        self.transforms = transforms
        self.frames = frames
        # print('frames:\n' + str(frames))

class SignDataset(Dataset):

    def __init__(self, signs):
        self.signs = signs

    def __getitem__(self, idx):
        return self.signs[idx].frames, self.signs[idx].label

    def __len__(self):
        return len(self.signs)

class SignsGenerator():

    def __init__(self, dir, trn_pct, val_pct, tst_pct, bs):
        self.signs = []
        self.bs = bs
        iterdir = iter(os.walk(dir))
        next(iterdir)
        for x in iterdir:
            iterx = iter(os.walk(x[0]))
            next(iterx)
            # print(os.)
            self.signs = self.signs + [Sign(y[0],  re.sub(r'\d+', '', os.path.basename(y[0]))) for y in iterx]

        self.split_data(trn_pct, val_pct, tst_pct)

    def split_data(self, trn_pct, val_pct, tst_pct):
        np.random.shuffle(self.signs)
        n = len(self.signs)
        trn_last_idx = int(trn_pct * n)
        val_last_idx = int( (trn_pct + val_pct) * n)

        self.train = self.signs[:trn_last_idx]
        self.val = self.signs[trn_last_idx+1: val_last_idx]
        self.test = self.signs[val_last_idx + 1:]

        
    def getTrainLoader(self):
        return DataLoader(SignDataset(self.train), batch_size=self.bs, shuffle=True)
