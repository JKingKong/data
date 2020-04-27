
import os
img_path1='D:\\JKingKong\\_毕业论文\\yolk_data\\A学长中筛选-肖\\img\\'
anno_path1='D:\\JKingKong\\_毕业论文\\yolk_data\\A学长中筛选-肖\\annotation\\'
img_path2='D:\\JKingKong\\_毕业论文\\yolk_data\\A自己的筛选-肖\\img\\'
anno_path2='D:\\JKingKong\\_毕业论文\\yolk_data\\A自己的筛选-肖\\annotation\\'
#获取该目录下所有文件，存入列表中

def rename(img_path,anno_path):
    imgs_list = os.listdir(img_path)
    n=0
    for i in imgs_list:
        #获取名字
        img_name = imgs_list[n].split('.')[0]

        img_file_old_path = img_path + img_name + '.jpg'
        img_file_new_path = img_path + 'X'+ str(n+2480+1) + '.jpg'
        os.rename(img_file_old_path, img_file_new_path)

        anno_file_old_path = anno_path + img_name + '.txt'
        anno_file_new_path = anno_path + 'X'+ str(n+2480+1) +  '.txt'
        os.rename(anno_file_old_path, anno_file_new_path)

        print(img_name)
        print(img_file_old_path)
        print(img_file_new_path)
        print(anno_file_old_path)
        print(anno_file_new_path)
        print()

        n+=1
    print("len:",len(imgs_list))
rename(img_path2,anno_path2)

