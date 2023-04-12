## WISTE

This is the code for paper "Water Index Swin Transformer Ensemble (WISTE) for Water Body Extraction from Multispectral Remote Sensing Image"

This code is based on Swin Transformer.


### Installation

Please refer to [MMSegmentation](https://github.com/open-mmlab/mmsegmentation) for installation and dataset preparation.

### Inference
```
# single-gpu testing
python tools/test.py <CONFIG_FILE> <SEG_CHECKPOINT_FILE> --eval mIoU

# multi-gpu testing
tools/dist_test.sh <CONFIG_FILE> <SEG_CHECKPOINT_FILE> <GPU_NUM> --eval mIoU

# multi-gpu, multi-scale testing
tools/dist_test.sh <CONFIG_FILE> <SEG_CHECKPOINT_FILE> <GPU_NUM> --aug-test --eval mIoU
```

### Pretrained model

Pretrained model can be download here: [pretrained model](https://download.openmmlab.com/mmsegmentation/v0.5/swin/upernet_swin_base_patch4_window12_512x512_160k_ade20k_pretrain_384x384_22K/upernet_swin_base_patch4_window12_512x512_160k_ade20k_pretrain_384x384_22K_20210531_125459-429057bf.pth)

### WISTE model

WISTE model can be download by [Baidunetdisk.](https://pan.baidu.com/s/1Rh-80oB6Ojbdsm72FuLTdg?pwd=3z3j)

### Training

To train with pre-trained models, run:
```
# single-gpu training
python tools/train.py <CONFIG_FILE> --options model.pretrained=<PRETRAIN_MODEL> [model.backbone.use_checkpoint=True] [other optional arguments]

# multi-gpu training
tools/dist_train.sh <CONFIG_FILE> <GPU_NUM> --options model.pretrained=<PRETRAIN_MODEL> [model.backbone.use_checkpoint=True] [other optional arguments] 
```

### PME

To use PME module, please run:
```
python ./pme.py
```
