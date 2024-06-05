import os
import random

Annotation_path = '/VOCdevkit/VOC2007/Annotations'

filename = []
for _, _, files in os.walk(Annotation_path):
    for file in files:
        filename.append(file.replace('.xml', ''))

# print(filename)
train_size = int(len(filename) * 0.9)
val_size = len(filename) - train_size

train_list = random.sample(filename, train_size)
val_list = [item for item in filename if item not in train_list]
trainval_path = '/Users/shijunshen/Documents/Code/PycharmProjects/faster-rcnn-pytorch-master/VOCdevkit/VOC2007/ImageSets/Main/trainval.txt'
with open(trainval_path, 'w') as f:
    for item in filename:
        f.write(item + '\n')


print(len(train_list))
train_path = '/Users/shijunshen/Documents/Code/PycharmProjects/faster-rcnn-pytorch-master/VOCdevkit/VOC2007/ImageSets/Main/train.txt'
with open(train_path, 'w') as f:
    for item in train_list:
        f.write(item + '\n')


print(len(val_list))
val_path = '/Users/shijunshen/Documents/Code/PycharmProjects/faster-rcnn-pytorch-master/VOCdevkit/VOC2007/ImageSets/Main/val.txt'
with open(val_path, 'w') as f:
    for item in val_list:
        f.write(item + '\n')
