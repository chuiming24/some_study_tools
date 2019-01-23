from piexif import remove as exif_remove
from glob import glob as find
from os import path

if __name__ == '__main__':
    # exif_info = piexif.load(fileName)
    # print(exif_info)
    PATH = input(r"请输入存放图片的文件夹路径，比如：C:\text" + "\n")
    SUFF = input(r"请输入要批量去除EXIF的图片后缀名，比如：jpg" + "\n")
    paths = find(path.join(PATH, '*.'+SUFF))
    for fileName in paths:
        exif_remove(fileName)
    print("清除完成")
