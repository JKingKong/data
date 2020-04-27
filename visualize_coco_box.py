import json
import os
import cv2

images_path = "./coco/train2017/" # 必须全英文路径，无空格，无非法字符
json_file = './coco/annotations/instances_train2017.json' # coco格式的json文件

with open(json_file) as annos:
    coco_json = json.load(annos)

images = coco_json['images']
for img in images:
    image_id = img['id']
    image_name = img['file_name']
    annotations = coco_json['annotations']
    image_path = images_path + image_name
    image = cv2.imread(image_path)
    for anno in annotations:
        if anno['image_id'] == image_id:
            bbox = anno['bbox']
            x, y, w, h = bbox[0],bbox[1],bbox[2],bbox[3]
            # 参数为(图像，左上角坐标，右下角坐标，边框线条颜色，线条宽度)
            # 注意这里坐标必须为整数，还有一点要注意的是opencv读出的图片通道为BGR，所以选择颜色的时候也要注意
            cv2.rectangle(image, (int(x), int(y)), (int(x + w), int(y + h)), (0, 0, 255), 2)
            # 参数为(显示的图片名称，要显示的图片)  必须加上图片名称，不然会报错
    # cv2.imshow('demo.jpg', image)
    save_path = "draw_jking_img_bbox/" + image_name
    cv2.imwrite(save_path,image)
