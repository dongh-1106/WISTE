# coding:utf-8
from time import time
import os
import numpy as np
import torch
from skimage import io
import os

def generate_pme(swin_path, ndwi_path, out_path):

    for i in os.listdir(swin_path):
        swin = io.imread(os.path.join(swin_path, i))
        ndwi = io.imread(os.path.join(ndwi_path, i))       # note that the file name of swin and ndwi should be same.
        ndwi = (ndwi >= 0.5).astype(np.uint8)              # Pixels which NDWI > 0.5 are considered as water pixels.

        ndwi[ndwi < -1] = -1
        ndwi[ndwi > 1] = 1

        pme = (swin + ndwi) / 2
        pme = np.expand_dims(pred, axis=2)
        pme = np.concatenate((pred,pred,pred),axis=2)

        io.imsave(os.path.join(out_path + i), pme)

if __name__ == '__main__':

    swin_path = ''   # path to your swin output results
    ndwi_path = ''   # path to your ndwi output results
    out_path = ''    # path to save your final results
    generate_pme(swin_path, ndwi_path, out_path)

