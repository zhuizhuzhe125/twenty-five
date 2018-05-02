'''
敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
'''

user_input=input('Leave your comments:  ')
name = open('filtered_words.txt')
for filter_word in name:
    fw=filter_word.rstrip()
    if fw in user_input:
        print('Freedom')
        break
else:
    print('Human Rights')

'''
首先调用文件：
然后去掉空格
rstrip：指定删除的字符（默认为空格）
循环遍历， 进行匹配
'''