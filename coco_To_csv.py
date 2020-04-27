import json
import csv

'''
该模块将coco-json类型的注释改为 csv类型,从而使用csv类型进行数据增强
'''
path = "./coco_167train_0 val/annotations/instances_train2017.json"
with open(path) as fp:
    coco_anno = json.load(fp)
images = coco_anno['images']
annotations = coco_anno['annotations']
train_labels_csv = open("./coco_167train_0 val/annotations/train_labels.csv","a+")
for img in images:
    image_id = img['id']
    image_name = img['file_name']
    for one_bbox_anno in annotations:
        if(one_bbox_anno['image_id'] == image_id):
            # bbox=[X,Y,W,H]
            bbox = one_bbox_anno['bbox']
            min_max_XY_bbox = [bbox[0],bbox[1],bbox[0]+bbox[2],bbox[1]+bbox[3]]
            image_path = "./data/raw/images/" + image_name
            one_bbox_record = image_path + "," + str(min_max_XY_bbox[0]) + "," + str(min_max_XY_bbox[1]) + "," \
                                 + str(min_max_XY_bbox[2])+ "," + str(min_max_XY_bbox[3]) + "," + "yolk" + "\n"
            train_labels_csv.write(one_bbox_record)
