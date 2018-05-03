import json  
import xlwt  
from collections import OrderedDict 

student_txt = open('numbers.txt','r')

count = student_txt.read()
print(count)
d = json.loads(count, object_pairs_hook=OrderedDict)  
print(d)
#创建工作薄
xlw_book = xlwt.Workbook(encoding='utf-8') 
#创建一张工作表
xlw_sheet = xlw_book.add_sheet('hello')

for row ,i in enumerate(d):   #读取所有字典，row为序号，i为字典关键字key    
    for col,j in enumerate(i):    
        xlw_sheet.write(row,col,j)

#保存
xlw_book.save('numbers_test.xls')