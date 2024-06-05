import os
import shutil

path = '/Users/shijunshen/Documents/Code/dataset/Baseball/Side'
Annotation_path = '/VOCdevkit/VOC2007/Annotations'
JPEGImages_path = '/Users/shijunshen/Documents/Code/PycharmProjects/faster-rcnn-pytorch-master/VOCdevkit/VOC2007/JPEGImages'

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.xml'):
            src_file = os.path.join(root, file)
            dst_file = os.path.join(Annotation_path, file)
            shutil.copy(src_file, dst_file)
        elif file.endswith('.jpg'):
            src_file = os.path.join(root, file)
            dst_file = os.path.join(JPEGImages_path, file)
            shutil.copy(src_file, dst_file)