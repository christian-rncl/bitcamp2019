import torch.utils.data as data

from os import listdir
from os.path import join
from PIL import Image


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in [".png", ".jpg", ".jpeg"])


def load_img(filepath):
    img = Image.open(filepath).convert('YCbCr')
    y, _, _ = img.split()
    return y

class Sign:
    def __init__(self, signdir, label, transforms=None):
        self.filenames = [join(signdir, x) for x in listdir(signdir) if is_image_file(x)]
        self. label = label
        self.transforms = transforms

    def get_sign(self):
        seq =[]
        seq = [load_img(img) for img in self.filenames]

        for img in self.filenames:
            if self.transforms:
                seq.append(transforms(load_img(img)))
            else:
                seq.append(load_img(img))

        return seq, self.label

class DatasetFromFolder(data.Dataset):
    def __init__(self, dir, transforms=None):
        super(DatasetFromFolder, self).__init__()
        self.signs = [s.get_sign() for s in self.loadSignsDir(dir, transforms)]
        # self.transforms = transforms

    def loadSignsDir(self, dir, transforms):
        signs = []
        for signdir in listdir(dir):
            signdir = join(dir, signdir)
            label = dir.split('/')[-2] 
            signs.append(Sign(signdir, label, transforms=transforms))
        
        return signs

    def __getitem__(self, index):
        return self.signs[index]

    def __len__(self):
        return len(self.image_filenames)
