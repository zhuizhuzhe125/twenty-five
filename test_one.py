from PIL import Image,ImageDraw,ImageFont,ImageColor
'''
 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
'''
'''
使用的库: PILLOW 
'''

#获取图片
def open_image():
	img = Image.open('image/123.png')
	add_number(img)

#制作图片并保存图片
def add_number(img):
	draw_test = ImageDraw.Draw(img)
	font = ImageFont.truetype('Arial.ttf', size=50) # 设置字体
	font_Color = ImageColor.colormap.get('red')	# 设置字体颜色
	width, height = img.size
	draw_test.text((width-30,0), '6', font = font, fill = font_Color) # 设置字体图片显示位置
	img.save('image/only_one.png', 'png') 	

open_image()

