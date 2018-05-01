'''
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
'''
import os
import glob

name = glob.glob(r'*.py')
count_null = 0 #空格
count_zs = 0 #注释
count_code = 0 # 代码
for xx in name:
	fiel_name = open(xx,'r')
	while True:
		line = fiel_name.readline()
		count_code += 1
		if not line:
			break
		if line[0] == '#':
			count_zs += 1
		if len(line)==line.count('\n'):
			count_null +=1
        
print('代码总共{0} 行' .format(count_code))
print('空行总共{0} 行' .format(count_null))
print('注释总共{0} 行' .format(count_zs))