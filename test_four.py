'''
任一个英文的纯文本文件，统计其中的单词出现的个数
'''
import re
#获取文本类容
def read_txt():
	with open('test_four.txt', 'r') as f: #
		s = f.read()
		count(s)

def count(txt_x):
	# \b 单词边界
	num = len(re.findall(r'[a-zA-Z\'\b]+',txt_x))
	print(num) 


read_txt()