import json
import os
from PIL import Image
'''
coco_annotation = dict(
    info="spytensor created",
    license=["license"],
    images=[
        {
            "height": img_h,
            "width": img_w,
            "id": image_id,
            "file_name": file_name + ".jpg"
        }
    ],
    annotations=[
        {
            id= box_id,
            image_id = image_id,
            category_id= 1,
            segmentation=[[round(X, 2)  ,round(Y, 2),round(X+1, 2),round(Y, 2),round(Y+1, 2),round(X, 2),round(X+1, 2),round(Y+1, 2)]], # 随便标记的
            bbox=[X,Y,W,H],
            iscrowd= 0,
            area=1.0
        }
    ],
    categories=[
        {
            "id": 1,
            "name": "yolk"
        }, ]
)
'''
def yolov3_anno_To_coco(annos_path,imgs_path,test = 0):

    coco_annotation = dict(
        info="spytensor created",
        license=["license"],
        images=[],
        annotations=[],
        categories=[
              {
               "id": 1,
               "name": "yolk"
              },]
    )
    yolo_txt_file_list = os.listdir(annos_path)
    max_file_count = len(yolo_txt_file_list)
    # 训练集数量  当前test参数 暂不起作用
    train_len = max_file_count * (1 - test)
    val_len = max_file_count * test
    n = 1
    box_id = 1
    for no_use in yolo_txt_file_list:
        image_id = n
        file_name = 'X' + str(image_id)
        anno_file_path = annos_path + file_name + '.txt'
        img_file_path = imgs_path + file_name +'.jpg'
        # 1、加入当前图片信息到coco_annotation字典的images字段列表里
        img = Image.open(img_file_path)
        img_w = img.size[0] #图片宽 横轴
        img_h = img.size[1] #图片长 纵轴
        image = dict({
            "height": img_h,
            "width": img_w,
            "id": image_id,
            "file_name": file_name + ".jpg"
        })
        coco_annotation['images'].append(image)

        # 2、读取当前图片信息的txt标注文件
        img_boxes_list = []
        with open(anno_file_path, 'r') as f:
            for line in f:
                img_boxes_list.append(list(line.strip('\n').split(' ')))

        # 3、将yoloV3的txt标注格式信息 转换成 coco的格式
        for box_label in img_boxes_list:
            # yoloV3 txt注释
            # 类别中心点X(比列) 中心点Y(比列) box(宽比列) box高(比列)
            x = float(box_label[1])
            y = float(box_label[2])
            w = float(box_label[3])
            h = float(box_label[4])

            # 转换成coco格式 box = [横轴-x,纵轴-y,横轴方向-w,纵轴方向-h]
            x1 = (x - w / 2) * img_w
            y1 = (y - h / 2) * img_h
            x2 = (x + w / 2) * img_w
            y2 = (y + h / 2) * img_h
            X = x1
            Y = y1
            W = x2 - x1
            H = y2 - y1

            bbox_anno = dict(
            id= box_id,
            image_id = image_id,
            category_id= 1,
            segmentation=[[round(X, 2)  ,round(Y, 2),round(X+1, 2),round(Y, 2),round(Y+1, 2),round(X, 2),round(X+1, 2),round(Y+1, 2)]], # 随便标记的
            bbox=[X,Y,W,H],
            iscrowd= 0,
            area=1.0
            )
            coco_annotation['annotations'].append(bbox_anno)
            box_id = box_id + 1
        n = n + 1
        if(n > train_len):
            break
    return coco_annotation

def save_coco_anno(coco_annotation,save_path):
    #保存到json文件
    with open(save_path,'w') as fp:
        json.dump(coco_annotation,fp)
def main():
    annos_path = './xiao_yolo_txt/annotation/'
    imgs_path = './xiao_yolo_txt/img/'
    coco_annotation = yolov3_anno_To_coco(annos_path,imgs_path,test=0)
    save_path = 'instances_train2017.json'
    save_coco_anno(coco_annotation,save_path)
main()
