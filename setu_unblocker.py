# coding=utf-8
# 批量修改图片尺寸
# imageResize(r"D:\tmp", r"D:\tmp\3", 0.7)
 
from PIL import Image
import os
truepath = os.getcwd()
def imageResize(input_path, output_path, scale):
    # 获取输入文件夹中的所有文件/夹，并改变工作空间
    files = os.listdir(input_path)
    os.chdir(input_path)

    output_path = truepath + "\\" + output_path
    
    # 判断输出文件夹是否存在，不存在则创建
    if(not os.path.exists(output_path)):
        os.makedirs(output_path)
    for file in files:
        # 判断是否为文件，文件夹不操作
        if(os.path.isfile(file)):
            img = Image.open(file)
            width = int(img.size[0]*2)
            height = int(img.size[1]*2)
            output_img = Image.new("RGB", (width,height),(151,204,118))
            output_img.paste(img, (round(img.size[0]*0.5),round(img.size[1]*0.5)))
            output_img.save(os.path.join(output_path, "New_" + file))
                                   
print("===========================")
print("|setu_unblocker by *******|")
print("===========================")
print("注意:请用同目录的文件夹作为输入与输出")
input_path = input("请输入需要处理的整个文件夹: ")
output_path = input("请输入处理后的图片存放的文件夹: ")
imageResize(input_path,output_path,scale=2)

input("已处理完成!")
        
