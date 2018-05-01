'''
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
1316*640
'''
import os
from PIL import Image
import glob
# 一张图片
'''
ing = Image.open('image/oioui.png')
print(ing.format, ing.size, ing.mode)
ing.thumbnail((640, 359))
print(ing.format, ing.size, ing.mode)
ing.save('image/inina.png')
'''

image_name = glob.glob(r'image/*.png') #获取image路径下所以图片名,并返回以列表形式返回
for xx in image_name: #遍历列表
	name = os.path.join(xx) #将图片名提取出来
	ing = Image.open(xx) #打开图片
	ing.thumbnail((240, 240)) #更改图片像素
	print(ing.format, ing.size, ing.mode)
	ing.save(name)# 保存图片
