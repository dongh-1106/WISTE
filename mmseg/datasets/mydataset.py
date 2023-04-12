import os.path as osp

import mmcv
import numpy as np
from mmcv.utils import print_log
from PIL import Image

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class mydata(CustomDataset):
    CLASSES = ('background', 'water')
    PALETTE = [[0,0,0], [255, 255, 255]]
    def __init__(self, **kwargs):
        super(mydata, self).__init__(
            img_suffix='.png',       #tif
            seg_map_suffix='.png',   #tif
            reduce_zero_label=False,
            **kwargs)
        assert osp.exists(self.img_dir)